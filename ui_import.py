# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_import.ui'
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

class Ui_importDialog(object):
    def setupUi(self, importDialog):
        importDialog.setObjectName(_fromUtf8("importDialog"))
        importDialog.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(importDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(importDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), importDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), importDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(importDialog)

    def retranslateUi(self, importDialog):
        importDialog.setWindowTitle(QtGui.QApplication.translate("importDialog", "Import LinkedGeoData", None, QtGui.QApplication.UnicodeUTF8))

