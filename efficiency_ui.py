# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'efficiency_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(745, 798)
        self.actionAbout_the_GUI = QAction(MainWindow)
        self.actionAbout_the_GUI.setObjectName(u"actionAbout_the_GUI")
        self.actionLoad_config = QAction(MainWindow)
        self.actionLoad_config.setObjectName(u"actionLoad_config")
        self.actionSave_config = QAction(MainWindow)
        self.actionSave_config.setObjectName(u"actionSave_config")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 10, 151, 71))
        font = QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setPixmap(QPixmap(u"../../../../../Users/EChen3/.designer/backup/IFX_LOGO_RGB.jpg"))
        self.label_10.setScaledContents(True)
        self.label_23 = QLabel(self.centralwidget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(190, 10, 511, 71))
        font1 = QFont()
        font1.setPointSize(16)
        self.label_23.setFont(font1)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 90, 701, 461))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 189, 171))
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox_6 = QGroupBox(self.groupBox)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.radioButton = QRadioButton(self.groupBox_6)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout_3.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox_6)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout_3.addWidget(self.radioButton_2)


        self.gridLayout_4.addWidget(self.groupBox_6, 2, 1, 1, 1)

        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_4.addWidget(self.label_12, 2, 0, 1, 1)

        self.lineEdit_16 = QLineEdit(self.groupBox)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.gridLayout_4.addWidget(self.lineEdit_16, 0, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)

        self.label_18 = QLabel(self.groupBox)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_4.addWidget(self.label_18, 0, 0, 1, 1)

        self.lineEdit_17 = QLineEdit(self.groupBox)
        self.lineEdit_17.setObjectName(u"lineEdit_17")

        self.gridLayout_4.addWidget(self.lineEdit_17, 1, 1, 1, 1)

        self.groupBox_7 = QGroupBox(self.tab)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(550, 20, 131, 161))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_8 = QPushButton(self.groupBox_7)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setEnabled(True)

        self.verticalLayout_2.addWidget(self.pushButton_8)

        self.pushButton_4 = QPushButton(self.groupBox_7)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(True)

        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.groupBox_7)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setEnabled(True)

        self.verticalLayout_2.addWidget(self.pushButton_5)

        self.groupBox_10 = QGroupBox(self.tab)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setGeometry(QRect(10, 200, 671, 201))
        self.groupBox_9 = QGroupBox(self.groupBox_10)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setGeometry(QRect(10, 140, 335, 51))
        self.gridLayout_7 = QGridLayout(self.groupBox_9)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_27 = QLabel(self.groupBox_9)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_7.addWidget(self.label_27, 0, 0, 1, 1)

        self.lineEdit_23 = QLineEdit(self.groupBox_9)
        self.lineEdit_23.setObjectName(u"lineEdit_23")

        self.gridLayout_7.addWidget(self.lineEdit_23, 0, 1, 1, 1)

        self.radioButton_5 = QRadioButton(self.groupBox_9)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.gridLayout_7.addWidget(self.radioButton_5, 0, 2, 1, 1)

        self.radioButton_6 = QRadioButton(self.groupBox_9)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.gridLayout_7.addWidget(self.radioButton_6, 0, 3, 1, 1)

        self.groupBox_3 = QGroupBox(self.groupBox_10)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 16, 651, 111))
        self.gridLayout_5 = QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_13 = QLabel(self.groupBox_3)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_5.addWidget(self.label_13, 0, 0, 1, 1)

        self.label_16 = QLabel(self.groupBox_3)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_5.addWidget(self.label_16, 0, 1, 1, 1)

        self.label_17 = QLabel(self.groupBox_3)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_5.addWidget(self.label_17, 0, 2, 1, 1)

        self.label_24 = QLabel(self.groupBox_3)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_5.addWidget(self.label_24, 0, 3, 1, 1)

        self.label_25 = QLabel(self.groupBox_3)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_5.addWidget(self.label_25, 0, 4, 1, 1)

        self.label_26 = QLabel(self.groupBox_3)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_5.addWidget(self.label_26, 0, 5, 1, 1)

        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_5.addWidget(self.label_15, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.groupBox_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_5.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.groupBox_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_5.addWidget(self.lineEdit_3, 1, 2, 1, 1)

        self.lineEdit_4 = QLineEdit(self.groupBox_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_5.addWidget(self.lineEdit_4, 1, 3, 1, 1)

        self.lineEdit_6 = QLineEdit(self.groupBox_3)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_5.addWidget(self.lineEdit_6, 1, 4, 1, 1)

        self.lineEdit_5 = QLineEdit(self.groupBox_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_5.addWidget(self.lineEdit_5, 1, 5, 1, 1)

        self.checkBox_3 = QCheckBox(self.groupBox_3)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout_5.addWidget(self.checkBox_3, 2, 1, 1, 1)

        self.checkBox_4 = QCheckBox(self.groupBox_3)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout_5.addWidget(self.checkBox_4, 2, 2, 1, 1)

        self.checkBox_5 = QCheckBox(self.groupBox_3)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.gridLayout_5.addWidget(self.checkBox_5, 2, 3, 1, 1)

        self.checkBox_6 = QCheckBox(self.groupBox_3)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.gridLayout_5.addWidget(self.checkBox_6, 2, 4, 1, 1)

        self.checkBox_7 = QCheckBox(self.groupBox_3)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.gridLayout_5.addWidget(self.checkBox_7, 2, 5, 1, 1)

        self.groupBox_11 = QGroupBox(self.tab)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setGeometry(QRect(210, 10, 331, 170))
        self.formLayout = QFormLayout(self.groupBox_11)
        self.formLayout.setObjectName(u"formLayout")
        self.label_29 = QLabel(self.groupBox_11)
        self.label_29.setObjectName(u"label_29")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_29)

        self.lineEdit_18 = QLineEdit(self.groupBox_11)
        self.lineEdit_18.setObjectName(u"lineEdit_18")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_18)

        self.label_4 = QLabel(self.groupBox_11)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.lineEdit_19 = QLineEdit(self.groupBox_11)
        self.lineEdit_19.setObjectName(u"lineEdit_19")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_19)

        self.label_5 = QLabel(self.groupBox_11)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_20 = QLineEdit(self.groupBox_11)
        self.lineEdit_20.setObjectName(u"lineEdit_20")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_20)

        self.label_7 = QLabel(self.groupBox_11)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_7)

        self.lineEdit_22 = QLineEdit(self.groupBox_11)
        self.lineEdit_22.setObjectName(u"lineEdit_22")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_22)

        self.label_6 = QLabel(self.groupBox_11)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_21 = QLineEdit(self.groupBox_11)
        self.lineEdit_21.setObjectName(u"lineEdit_21")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_21)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 10, 471, 251))
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_28 = QLineEdit(self.groupBox_2)
        self.lineEdit_28.setObjectName(u"lineEdit_28")
        self.lineEdit_28.setEnabled(False)

        self.gridLayout.addWidget(self.lineEdit_28, 1, 0, 1, 3)

        self.comboBox = QComboBox(self.groupBox_2)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 2)

        self.comboBox_3 = QComboBox(self.groupBox_2)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout.addWidget(self.comboBox_3, 4, 1, 1, 2)

        self.lineEdit_30 = QLineEdit(self.groupBox_2)
        self.lineEdit_30.setObjectName(u"lineEdit_30")
        self.lineEdit_30.setEnabled(False)

        self.gridLayout.addWidget(self.lineEdit_30, 5, 0, 1, 3)

        self.pushButton_6 = QPushButton(self.groupBox_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setEnabled(True)

        self.gridLayout.addWidget(self.pushButton_6, 6, 2, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.label_19 = QLabel(self.groupBox_2)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout.addWidget(self.label_19, 0, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.lineEdit_29 = QLineEdit(self.groupBox_2)
        self.lineEdit_29.setObjectName(u"lineEdit_29")
        self.lineEdit_29.setEnabled(False)

        self.gridLayout.addWidget(self.lineEdit_29, 3, 0, 1, 3)

        self.comboBox_7 = QComboBox(self.groupBox_2)
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.gridLayout.addWidget(self.comboBox_7, 2, 1, 1, 2)

        self.groupBox_4 = QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 270, 471, 154))
        self.gridLayout_6 = QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_14 = QLabel(self.groupBox_4)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_6.addWidget(self.label_14, 0, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_6.addWidget(self.label_8, 1, 0, 1, 1)

        self.checkBox = QCheckBox(self.groupBox_4)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setEnabled(False)
        self.checkBox.setCheckable(True)
        self.checkBox.setChecked(True)
        self.checkBox.setTristate(False)

        self.gridLayout_6.addWidget(self.checkBox, 2, 0, 1, 2)

        self.pushButton_11 = QPushButton(self.groupBox_4)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setEnabled(True)

        self.gridLayout_6.addWidget(self.pushButton_11, 2, 2, 1, 1)

        self.checkBox_2 = QCheckBox(self.groupBox_4)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setChecked(True)

        self.gridLayout_6.addWidget(self.checkBox_2, 3, 0, 1, 2)

        self.pushButton_7 = QPushButton(self.groupBox_4)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setEnabled(True)

        self.gridLayout_6.addWidget(self.pushButton_7, 3, 2, 1, 1)

        self.lineEdit_27 = QLineEdit(self.groupBox_4)
        self.lineEdit_27.setObjectName(u"lineEdit_27")
        self.lineEdit_27.setEnabled(True)
        self.lineEdit_27.setCursorPosition(8)
        self.lineEdit_27.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineEdit_27, 0, 2, 1, 1)

        self.lineEdit_7 = QLineEdit(self.groupBox_4)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_6.addWidget(self.lineEdit_7, 1, 2, 1, 1)

        self.groupBox_5 = QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(500, 10, 181, 181))
        self.verticalLayout = QVBoxLayout(self.groupBox_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_9 = QPushButton(self.groupBox_5)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setEnabled(True)

        self.verticalLayout.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.groupBox_5)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setEnabled(True)

        self.verticalLayout.addWidget(self.pushButton_10)

        self.pushButton_12 = QPushButton(self.groupBox_5)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setEnabled(True)

        self.verticalLayout.addWidget(self.pushButton_12)

        self.pushButton_13 = QPushButton(self.groupBox_5)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setEnabled(True)

        self.verticalLayout.addWidget(self.pushButton_13)

        self.groupBox_8 = QGroupBox(self.tab_2)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setGeometry(QRect(500, 200, 181, 181))
        self.gridLayout_2 = QGridLayout(self.groupBox_8)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.comboBox_2 = QComboBox(self.groupBox_8)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_2.addWidget(self.comboBox_2, 0, 1, 1, 2)

        self.label_11 = QLabel(self.groupBox_8)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)

        self.comboBox_6 = QComboBox(self.groupBox_8)
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.gridLayout_2.addWidget(self.comboBox_6, 3, 1, 1, 2)

        self.label_20 = QLabel(self.groupBox_8)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_2.addWidget(self.label_20, 0, 0, 1, 1)

        self.comboBox_5 = QComboBox(self.groupBox_8)
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.gridLayout_2.addWidget(self.comboBox_5, 2, 1, 1, 2)

        self.comboBox_4 = QComboBox(self.groupBox_8)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.gridLayout_2.addWidget(self.comboBox_4, 1, 1, 1, 2)

        self.label_21 = QLabel(self.groupBox_8)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_2.addWidget(self.label_21, 1, 0, 1, 1)

        self.label_22 = QLabel(self.groupBox_8)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_2.addWidget(self.label_22, 3, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 560, 701, 161))
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 740, 701, 23))
        self.progressBar.setValue(24)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 745, 26))
        self.menuabout = QMenu(self.menubar)
        self.menuabout.setObjectName(u"menuabout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuabout.menuAction())
        self.menuabout.addAction(self.actionLoad_config)
        self.menuabout.addAction(self.actionSave_config)
        self.menuabout.addSeparator()
        self.menuabout.addAction(self.actionAbout_the_GUI)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbout_the_GUI.setText(QCoreApplication.translate("MainWindow", u"About the GUI", None))
        self.actionLoad_config.setText(QCoreApplication.translate("MainWindow", u"Load config", None))
        self.actionSave_config.setText(QCoreApplication.translate("MainWindow", u"Save config", None))
        self.label_10.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Efficiency GUI", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"DC source setting", None))
        self.groupBox_6.setTitle("")
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"On", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Toggle", None))
        self.lineEdit_16.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"current(A)", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"voltage(V)", None))
        self.lineEdit_17.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.groupBox_7.setTitle("")
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Start efficiency", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"abort efficiency", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Clear log", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"E loading", None))
        self.groupBox_9.setTitle("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Loadling Toggle (Amps)", None))
        self.lineEdit_23.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"On", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"channel setting", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Channel", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"CH1", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"CH3", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"CH5", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"CH7", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"CH9", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Iout max", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"80", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"80", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"80", None))
        self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", u"80", None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"80", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"selected", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"selected", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"selected", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"selected", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"selected", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"efficiency measurement condition", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"start current (A)", None))
        self.lineEdit_18.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"end current (A)", None))
        self.lineEdit_19.setText(QCoreApplication.translate("MainWindow", u"400", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"step(%)", None))
        self.lineEdit_20.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"cooldown time(Sec)", None))
        self.lineEdit_22.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"duration time(Sec)", None))
        self.lineEdit_21.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"main", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Equipments setting", None))
        self.lineEdit_28.setText("")
        self.lineEdit_30.setText("")
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"re-scan equipments", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"E-load", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"DC source", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"DAQ", None))
        self.lineEdit_29.setText("")
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Misc", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Output folder in PC", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"filename", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"filename include Vin/Vout", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"set report folder", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"filename include trimstamp", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Save waveform once", None))
        self.lineEdit_27.setText(QCoreApplication.translate("MainWindow", u"./report", None))
        self.lineEdit_7.setText(QCoreApplication.translate("MainWindow", u"IFX_DB410_", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"test", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"load report for Vmax", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"load report for Vmin", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"test button1", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Get DAQ value once", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"DAQ detial setting", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Iin channel", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Vin channel", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Vout channel", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Iin channel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"setting", None))
        self.menuabout.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

