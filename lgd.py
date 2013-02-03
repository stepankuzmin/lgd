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
from fyzz.yappsparser import parse

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
      print "Make point layer"
      return QgsVectorLayer("Point", layerName, "memory")

    def LineString(self, layerName):
      print "Make linestring layer"
      return QgsVectorLayer("Line", layerName, "memory")

    def Polygon(self, layerName):
      print "Make poligon layer"
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
      layerName = str(self.dlg.ui.layerNameLineEdit.text())
      endpoint = str(self.dlg.ui.endpointLineEdit.text())
      query = str(self.dlg.ui.queryPlainTextEdit.toPlainText())

      #ast = parse(query)
      #print ast.where

#      triples = rdfextras.sparql.parser.parse(query).query.whereClause.parsedGraphPattern.triples
#
#      for triple in triples:
#        for propVal in triple.propVals:
#          for obj in propVal.objects:
#            print "object: ", obj.title(), "type: ", type(obj.title())
#        print "property: ", propVal.property.title(), "type: ", type(propVal.property.title())
#
#        # Is there any geometry field?
#        if propVal.property.title() == u"Geo:Geometry":
#          print obj.title(), " is Geo:Geometry!"
#
#      result = sparql.query(endpoint, query)

      pattern = re.compile('^\s*([\w\s]+)\s*\(\s*(.*)\s*\)\s*$')
      
      result = sparql.query(endpoint, query).fetchall()
      firstRow = sparql.unpack_row(result[0])

      # Define geometry field
      for index in range(len(firstRow)):
        matches = pattern.match(firstRow[index])
        if matches:
          geometryType, geometry = matches.groups() # something like erlang's _ instead of geometry
          geometryType = geometryType.lower().strip()
          try:
            layer = self.parsers[geometryType](layerName)
            geometryIndex = index

            pr = layer.dataProvider()
            layer.startEditing()
            
            for row in result:
              values = sparql.unpack_row(row)
              fet = QgsFeature()
              fet.setGeometry(QgsGeometry.fromWkt(values[index]))
              #fet.setAttributeMap() # Add attributes to all Geometry layers?
              pr.addFeatures([fet])

            layer.commitChanges()
            layer.updateExtents()
            QgsMapLayerRegistry.instance().addMapLayer(layer)
          except KeyError:
            raise NotImplementedError, "Unsupported WKT Type: %s" % geometryType # + QMessageBox


      #rows = result.fetchall()
      #for row in rows:
      #  values = sparql.unpack_row(row)
      #  for value in values:
      #    matches = pattern.match(value)
      #    if matches:
      #      geometryType, geometry = matches.groups() # something like erlang's _ instead of geometry
      #      geometryType = geometryType.lower().strip()


      #vl = QgsVectorLayer("Point", layerName, "memory")
      #pr = vl.dataProvider()
      #vl.startEditing()

      #pr.addAttributes([QgsField(result.variables[0], QVariant.String), QgsField(result.variables[1],  QVariant.String)])

      #for row in result:
      #  values = sparql.unpack_row(row)
      #  fet = QgsFeature()
      #  fet.setGeometry(QgsGeometry.fromWkt(values[2]))
      #  fet.setAttributeMap({0 : QVariant(values[0]), 1 : QVariant(values[1])})
      #  pr.addFeatures([fet])
     # 
     # vl.commitChanges()
     # vl.updateExtents()
     # QgsMapLayerRegistry.instance().addMapLayer(vl)
