# -*- coding: utf-8 -*-
"""
/***************************************************************************
 lgd
                                 A QGIS plugin
 Linked geodata tool
                              -------------------
        begin                : 2013-04-28
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
from lgdimportdialog import lgdImportDialog
from lgdexportdialog import lgdExportDialog

import sparql

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
        self.importDialog = lgdImportDialog()
        self.exportDialog = lgdExportDialog()

    def initGui(self):
        # Create action that will start plugin configuration
        self.importAction = QAction(QIcon(":/plugins/lgd/icon.png"), u"Import", self.iface.mainWindow())
        self.exportAction = QAction(QIcon(":/plugins/lgd/icon.png"), u"Export", self.iface.mainWindow())

        # connect the actions to the methods
        QObject.connect(self.importAction, SIGNAL("triggered()"), self.importLGD)
        QObject.connect(self.exportAction, SIGNAL("triggered()"), self.exportLGD)

        # Add the plugin menu item and icon
        if hasattr(self.iface, "addPluginToWebMenu"):
          self.iface.addWebToolBarIcon(self.importAction)
          self.iface.addWebToolBarIcon(self.exportAction)
          self.iface.addPluginToWebMenu("&LinkedGeoData", self.importAction)
          self.iface.addPluginToWebMenu("&LinkedGeoData", self.exportAction)
        else:
          self.iface.addToolBarIcon(self.importAction)
          self.iface.addToolBarIcon(self.exportAction)
          self.iface.addPluginToMenu("&LinkedGeoData", self.importAction)
          self.iface.addPluginToMenu("&LinkedGeoData", self.exportAction)

    def unload(self):
        # Remove the plugin menu item and icon
        if hasattr(self.iface, "addPluginToRasterMenu"):
          self.iface.removePluginWebMenu("&LinkedGeoData", self.importAction);
          self.iface.removePluginWebMenu("&LinkedGeoData", self.exportAction);
          self.iface.removeWebToolBarIcon(self.importAction)
          self.iface.removeWebToolBarIcon(self.exportAction)
        else:
          self.iface.removePluginMenu(u"&LinkedGeoData", self.importAction)
          self.iface.removePluginMenu(u"&LinkedGeoData", self.exportAction)
          self.iface.removeToolBarIcon(self.importAction)
          self.iface.removeToolBarIcon(self.exportAction)

    def importLGD(self):
      self.importDialog.show()
      result = self.importDialog.exec_()
      if result == 1:
        print "okay"
        pass

    def exportLGD(self):
      self.exportDialog.show()
      result = self.exportDialog.exec_()
      if result == 1:
        pass
