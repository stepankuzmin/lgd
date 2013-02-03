# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_lgd.ui'
#
# Created: Tue Jan 22 22:16:01 2013
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
        lgd.resize(600, 500)
        self.verticalLayout_2 = QtGui.QVBoxLayout(lgd)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.layerSettingsGroupBox = QtGui.QGroupBox(lgd)
        self.layerSettingsGroupBox.setObjectName(_fromUtf8("layerSettingsGroupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layerSettingsGroupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.layerNameLabel = QtGui.QLabel(self.layerSettingsGroupBox)
        self.layerNameLabel.setObjectName(_fromUtf8("layerNameLabel"))
        self.verticalLayout_3.addWidget(self.layerNameLabel)
        self.layerNameLineEdit = QtGui.QLineEdit(self.layerSettingsGroupBox)
        self.layerNameLineEdit.setObjectName(_fromUtf8("layerNameLineEdit"))
        self.verticalLayout_3.addWidget(self.layerNameLineEdit)
        self.verticalLayout_2.addWidget(self.layerSettingsGroupBox)
        self.querySettingsGroupBox = QtGui.QGroupBox(lgd)
        self.querySettingsGroupBox.setObjectName(_fromUtf8("querySettingsGroupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.querySettingsGroupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.endpointLabel = QtGui.QLabel(self.querySettingsGroupBox)
        self.endpointLabel.setObjectName(_fromUtf8("endpointLabel"))
        self.verticalLayout.addWidget(self.endpointLabel)
        self.endpointLineEdit = QtGui.QLineEdit(self.querySettingsGroupBox)
        self.endpointLineEdit.setObjectName(_fromUtf8("endpointLineEdit"))
        self.verticalLayout.addWidget(self.endpointLineEdit)
        self.queryLabel = QtGui.QLabel(self.querySettingsGroupBox)
        self.queryLabel.setObjectName(_fromUtf8("queryLabel"))
        self.verticalLayout.addWidget(self.queryLabel)
        self.queryPlainTextEdit = QtGui.QPlainTextEdit(self.querySettingsGroupBox)
        self.queryPlainTextEdit.setObjectName(_fromUtf8("queryPlainTextEdit"))
        self.verticalLayout.addWidget(self.queryPlainTextEdit)
        self.queryPushButton = QtGui.QPushButton(self.querySettingsGroupBox)
        self.queryPushButton.setObjectName(_fromUtf8("queryPushButton"))
        self.verticalLayout.addWidget(self.queryPushButton)
        self.verticalLayout_2.addWidget(self.querySettingsGroupBox)
        self.buttonBox = QtGui.QDialogButtonBox(lgd)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(lgd)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), lgd.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), lgd.reject)
        QtCore.QMetaObject.connectSlotsByName(lgd)

    def retranslateUi(self, lgd):
        lgd.setWindowTitle(QtGui.QApplication.translate("lgd", "LinkedGeoData query tool", None, QtGui.QApplication.UnicodeUTF8))
        self.layerSettingsGroupBox.setTitle(QtGui.QApplication.translate("lgd", "Layer settings", None, QtGui.QApplication.UnicodeUTF8))
        self.layerNameLabel.setText(QtGui.QApplication.translate("lgd", "Layer name", None, QtGui.QApplication.UnicodeUTF8))
        self.layerNameLineEdit.setText(QtGui.QApplication.translate("lgd", "LinkedGeoDataLayer", None, QtGui.QApplication.UnicodeUTF8))
        self.querySettingsGroupBox.setTitle(QtGui.QApplication.translate("lgd", "Query", None, QtGui.QApplication.UnicodeUTF8))
        self.endpointLabel.setText(QtGui.QApplication.translate("lgd", "SPARQL Endpoint", None, QtGui.QApplication.UnicodeUTF8))
        self.endpointLineEdit.setText(QtGui.QApplication.translate("lgd", "http://linkedgeodata.org/sparql", None, QtGui.QApplication.UnicodeUTF8))
        self.queryLabel.setText(QtGui.QApplication.translate("lgd", "Query text", None, QtGui.QApplication.UnicodeUTF8))
        self.queryPlainTextEdit.setPlainText(QtGui.QApplication.translate("lgd", "PREFIX lgdo: <http://linkedgeodata.org/ontology/>\n"
"SELECT *\n"
"FROM <http://linkedgeodata.org>\n"
"{\n"
"    ?s a lgdo:Amenity .\n"
"    ?s rdfs:label ?l .\n"
"    ?s geo:geometry ?g .\n"
"    Filter(bif:st_intersects (?g, bif:st_point (56.833333, 60.583333), 1000)) .\n"
"} LIMIT 10", None, QtGui.QApplication.UnicodeUTF8))
        self.queryPushButton.setText(QtGui.QApplication.translate("lgd", "Run query", None, QtGui.QApplication.UnicodeUTF8))

