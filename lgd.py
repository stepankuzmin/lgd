# -*- coding: utf-8 -*-
"""
/***************************************************************************
 lgd
                                 A QGIS plugin
 A LinkedGeoData SPARQL query tool
                              -------------------
        begin                : 2013-01-20
        copyright            : (C) 2013 by Stepan Kuzmin
        email                : to.stepan.kuzmin@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import re

# Import plugin dependencies
import sparql

import rdfextras
from rdfextras.sparql import parser

# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

# Initialize Qt resources from file resources.py
import resources_rc

# Import the code for the dialog
from lgddialog import lgdDialog


class lgd:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = QFileInfo(QgsApplication.qgisUserDbFilePath()).path() + "/python/plugins/lgd"
        # initialize locale
        localePath = ""
        locale = QSettings().value("locale/userLocale").toString()[0:2]

        if QFileInfo(self.plugin_dir).exists():
            localePath = self.plugin_dir + "/i18n/lgd_" + locale + ".qm"

        if QFileInfo(localePath).exists():
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = lgdDialog()
        
        self.parsers = {}
        self.parsers['point'] = self.Point
        self.parsers['linestring'] = self.LineString
        self.parsers['polygon'] = self.Polygon
        
    def Point(self, layerName):
      return QgsVectorLayer("Point", layerName, "memory")

    def LineString(self, layerName):
      return QgsVectorLayer("Line", layerName, "memory")

    def Polygon(self, layerName):
      return QgsVectorLayer("Polygon", layerName, "memory")

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/lgd/icon.png"),
            u"LinkedGeoData query tool", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&LinkedGeoData", self.action)
        QObject.connect(self.dlg.ui.queryPushButton, SIGNAL("clicked()"), self.runQuery)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&LinkedGeoData", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code)
            pass

    def runQuery(self):
      # Get input data
      layerName = str(self.dlg.ui.layerNameLineEdit.text())
      endpoint = str(self.dlg.ui.endpointLineEdit.text())
      query = str(self.dlg.ui.queryPlainTextEdit.toPlainText())

      # Predefine geometry field as None
      # NB: How to deal with multiple geometry fields?
      geometryField = None

      # Parse SPARQL query to get Geo:Geometry field
      triples = rdfextras.sparql.parser.parse(query).query.whereClause.parsedGraphPattern.triples
      for triple in triples:
        for propVal in triple.propVals:
          for obj in propVal.objects:
            # Is there any geometry field?
            if propVal.property.title() == u"Geo:Geometry":
              geometryField = obj.title().lower()

      if geometryField is None:
        QMessageBox.warning(self.iface.mainWindow(), "Warning", "There is no Geo:Geometry field in this query", QMessageBox.Ok)
        return
      
      result = sparql.query(endpoint, query)
      variables = result.variables
      geometryFieldIndex = variables.index(geometryField)

      geometry = []
      attributes = []
      result = result.fetchall()

      # Get geometry and attributes
      for row in result:
        values = sparql.unpack_row(row)
        geometry.append(values[geometryFieldIndex])
        values.remove(values[geometryFieldIndex])
        attributes.append(values)

      # Determine layer geometry type
      pattern = re.compile('^\s*([\w\s]+)\s*\(\s*(.*)\s*\)\s*$') # from OpenLayers WKT.js
      matches = pattern.match(geometry[0])
      if matches:
        geometryType = matches.groups()[0]
        geometryType = geometryType.lower().strip()
        try:
          # Create in-memory layer
          layer = self.parsers[geometryType](layerName)
          pr = layer.dataProvider()
          layer.startEditing()
          
          # Layer attributes
          layerAttributes = []
          variables.remove(geometryField)
          for index in range(len(attributes[0])):
            layerAttributes.append(QgsField(variables[index], QVariant.String))
          pr.addAttributes(layerAttributes)

          # Add features to layer
          for index in range(len(geometry)):
            fet = QgsFeature()
            fet.setGeometry(QgsGeometry.fromWkt(geometry[index]))

            # Add feature attributes
            fetAttr = {}
            for subIndex in range(len(attributes[index])):
              fetAttr[subIndex] = QVariant(attributes[index][subIndex])
            fet.setAttributeMap(fetAttr)
            pr.addFeatures([fet])

          # Save and display layer
          layer.commitChanges()
          layer.updateExtents()
          QgsMapLayerRegistry.instance().addMapLayer(layer)
        except KeyError:
          QMessageBox.warning(self.iface.mainWindow(), "Warning", "Unsupported WKT type %s" % geometryType, QMessageBox.Ok)
          raise NotImplementedError, "Unsupported WKT type: %s" % geometryType
