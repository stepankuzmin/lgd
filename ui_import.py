# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_import.ui'
#
# Created: Fri May 17 15:16:05 2013
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
        importDialog.resize(473, 460)
        self.verticalLayout_2 = QtGui.QVBoxLayout(importDialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.layerSettingsGroupBox = QtGui.QGroupBox(importDialog)
        self.layerSettingsGroupBox.setObjectName(_fromUtf8("layerSettingsGroupBox"))
        self.formLayout = QtGui.QFormLayout(self.layerSettingsGroupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.layerNameLabel = QtGui.QLabel(self.layerSettingsGroupBox)
        self.layerNameLabel.setObjectName(_fromUtf8("layerNameLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.layerNameLabel)
        self.layerNameLineEdit = QtGui.QLineEdit(self.layerSettingsGroupBox)
        self.layerNameLineEdit.setMinimumSize(QtCore.QSize(300, 0))
        self.layerNameLineEdit.setObjectName(_fromUtf8("layerNameLineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.layerNameLineEdit)
        self.layerTypeLabel = QtGui.QLabel(self.layerSettingsGroupBox)
        self.layerTypeLabel.setObjectName(_fromUtf8("layerTypeLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.layerTypeLabel)
        self.layerTypeComboBox = QtGui.QComboBox(self.layerSettingsGroupBox)
        self.layerTypeComboBox.setMinimumSize(QtCore.QSize(300, 0))
        self.layerTypeComboBox.setObjectName(_fromUtf8("layerTypeComboBox"))
        self.layerTypeComboBox.addItem(_fromUtf8(""))
        self.layerTypeComboBox.addItem(_fromUtf8(""))
        self.layerTypeComboBox.addItem(_fromUtf8(""))
        self.layerTypeComboBox.addItem(_fromUtf8(""))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.layerTypeComboBox)
        self.verticalLayout_2.addWidget(self.layerSettingsGroupBox)
        self.querySettingsGroupBox = QtGui.QGroupBox(importDialog)
        self.querySettingsGroupBox.setObjectName(_fromUtf8("querySettingsGroupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.querySettingsGroupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.SparqlEndpointFormLayout = QtGui.QFormLayout()
        self.SparqlEndpointFormLayout.setObjectName(_fromUtf8("SparqlEndpointFormLayout"))
        self.SparqlEndpointLabel = QtGui.QLabel(self.querySettingsGroupBox)
        self.SparqlEndpointLabel.setObjectName(_fromUtf8("SparqlEndpointLabel"))
        self.SparqlEndpointFormLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.SparqlEndpointLabel)
        self.SparqlEndpointLineEdit = QtGui.QLineEdit(self.querySettingsGroupBox)
        self.SparqlEndpointLineEdit.setMinimumSize(QtCore.QSize(300, 0))
        self.SparqlEndpointLineEdit.setObjectName(_fromUtf8("SparqlEndpointLineEdit"))
        self.SparqlEndpointFormLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.SparqlEndpointLineEdit)
        self.verticalLayout.addLayout(self.SparqlEndpointFormLayout)
        self.QueryTextLabel = QtGui.QLabel(self.querySettingsGroupBox)
        self.QueryTextLabel.setObjectName(_fromUtf8("QueryTextLabel"))
        self.verticalLayout.addWidget(self.QueryTextLabel)
        self.plainTextEdit = QtGui.QPlainTextEdit(self.querySettingsGroupBox)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.verticalLayout_2.addWidget(self.querySettingsGroupBox)
        self.buttonBox = QtGui.QDialogButtonBox(importDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(importDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), importDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), importDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(importDialog)

    def retranslateUi(self, importDialog):
        importDialog.setWindowTitle(QtGui.QApplication.translate("importDialog", "Import LinkedGeoData", None, QtGui.QApplication.UnicodeUTF8))
        self.layerSettingsGroupBox.setTitle(QtGui.QApplication.translate("importDialog", "Layer settings", None, QtGui.QApplication.UnicodeUTF8))
        self.layerNameLabel.setText(QtGui.QApplication.translate("importDialog", "Layer name", None, QtGui.QApplication.UnicodeUTF8))
        self.layerNameLineEdit.setText(QtGui.QApplication.translate("importDialog", "Linked geodata layer", None, QtGui.QApplication.UnicodeUTF8))
        self.layerTypeLabel.setText(QtGui.QApplication.translate("importDialog", "Layer type", None, QtGui.QApplication.UnicodeUTF8))
        self.layerTypeComboBox.setItemText(0, QtGui.QApplication.translate("importDialog", "Automatic", None, QtGui.QApplication.UnicodeUTF8))
        self.layerTypeComboBox.setItemText(1, QtGui.QApplication.translate("importDialog", "Point", None, QtGui.QApplication.UnicodeUTF8))
        self.layerTypeComboBox.setItemText(2, QtGui.QApplication.translate("importDialog", "Line", None, QtGui.QApplication.UnicodeUTF8))
        self.layerTypeComboBox.setItemText(3, QtGui.QApplication.translate("importDialog", "Polygon", None, QtGui.QApplication.UnicodeUTF8))
        self.querySettingsGroupBox.setTitle(QtGui.QApplication.translate("importDialog", "Query settings", None, QtGui.QApplication.UnicodeUTF8))
        self.SparqlEndpointLabel.setText(QtGui.QApplication.translate("importDialog", "SPARQL endpoint", None, QtGui.QApplication.UnicodeUTF8))
        self.SparqlEndpointLineEdit.setText(QtGui.QApplication.translate("importDialog", "http://linkedgeodata.org/sparql", None, QtGui.QApplication.UnicodeUTF8))
        self.QueryTextLabel.setText(QtGui.QApplication.translate("importDialog", "Query text", None, QtGui.QApplication.UnicodeUTF8))
        self.plainTextEdit.setPlainText(QtGui.QApplication.translate("importDialog", "Prefix lgd:<http://linkedgeodata.org/>\n"
"Prefix lgdo:<http://linkedgeodata.org/ontology/>\n"
"\n"
"Select * From <http://linkedgeodata.org> \n"
"{ \n"
"  ?s\n"
"  ?p\n"
"  ?o .\n"
"}", None, QtGui.QApplication.UnicodeUTF8))

