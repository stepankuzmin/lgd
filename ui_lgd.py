# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_lgd.ui'
#
# Created: Sun Jan 20 23:03:27 2013
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_lgd(object):
    def setupUi(self, lgd):
        lgd.setObjectName(_fromUtf8("lgd"))
        lgd.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(lgd)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(lgd)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), lgd.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), lgd.reject)
        QtCore.QMetaObject.connectSlotsByName(lgd)

    def retranslateUi(self, lgd):
        lgd.setWindowTitle(QtGui.QApplication.translate("lgd", "lgd", None, QtGui.QApplication.UnicodeUTF8))

