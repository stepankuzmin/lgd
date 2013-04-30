# -*- coding: utf-8 -*-
"""
/***************************************************************************
 lgdExportDialog
                                 A QGIS plugin
 LinkedGeoData tool
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

from PyQt4 import QtCore, QtGui
from ui_export import Ui_exportDialog
# create the dialog for zoom to point


class lgdExportDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_exportDialog()
        self.ui.setupUi(self)
