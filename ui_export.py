# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_export.ui'
#
# Created: Mon Apr 29 00:34:08 2013
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_exportDialog(object):
    def setupUi(self, exportDialog):
        exportDialog.setObjectName(_fromUtf8("exportDialog"))
        exportDialog.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(exportDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(exportDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), exportDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), exportDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(exportDialog)

    def retranslateUi(self, exportDialog):
        exportDialog.setWindowTitle(QtGui.QApplication.translate("exportDialog", "Export LinkedGeoData", None, QtGui.QApplication.UnicodeUTF8))

