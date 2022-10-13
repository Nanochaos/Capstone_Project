# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide2.QtGui import (QFont, QIcon)
from PySide2.QtWidgets import (QCheckBox, QComboBox, QFrame, QHBoxLayout, QLabel, QLineEdit,QStyle, QStyleOptionSlider,
                               QPushButton, QSizePolicy, QSlider, QSpacerItem, QSpinBox, QStackedWidget, QVBoxLayout,
                               QWidget)

from Custom_Widgets.Widgets import (QCustomSlideMenu, QCustomStackedWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	background: none;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #FFF;\n"
"}\n"
"\n"
"#centralwidget{\n"
"	background-color:#1f232a;\n"
"}\n"
"#leftMenuSubContainer{\n"
"	background-color:#16191d;\n"
"}\n"
"#leftMenuSubContainer QPushButton{\n"
"	text-align: left;\n"
"	padding: 2px 5px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"#centerMenuSubContainer{\n"
"	background-color: #2c313c;\n"
"}\n"
"#frame_4{\n"
"	background-color: #16191d;\n"
"	border-radius: 10px\n"
"}\n"
"#headerContainer{\n"
"	background-color: #2c313c;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenuContainer.sizePolicy().hasHeightForWidth())
        self.leftMenuContainer.setSizePolicy(sizePolicy)
        self.leftMenuContainer.setMaximumSize(QSize(50, 16777215))
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftMenuSubContainer.sizePolicy().hasHeightForWidth())
        self.leftMenuSubContainer.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.frame = QFrame(self.leftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        icon1 = QIcon()
        icon1.addFile(u"icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon1)
        self.menuBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.menuBtn)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.leftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.homeBtn = QPushButton(self.frame_2)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setStyleSheet(u"background-color: #1f232a;")
        icon2 = QIcon()
        icon2.addFile(u"icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon2)
        self.homeBtn.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.homeBtn)

        self.dataBtn = QPushButton(self.frame_2)
        self.dataBtn.setObjectName(u"dataBtn")
        icon3 = QIcon()
        icon3.addFile(u"icons/heatmap.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dataBtn.setIcon(icon3)
        self.dataBtn.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.dataBtn)

        self.openBtn = QPushButton(self.frame_2)
        self.openBtn.setObjectName(u"openBtn")
        self.openBtn.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u"icons/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.openBtn.setIcon(icon4)
        self.openBtn.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.openBtn)

        self.cameraBtn = QPushButton(self.frame_2)
        self.cameraBtn.setObjectName(u"cameraBtn")
        self.cameraBtn.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u"icons/camera - white.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cameraBtn.setIcon(icon5)
        self.cameraBtn.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.cameraBtn)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.frame_8 = QFrame(self.leftMenuSubContainer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 0))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_8)
        self.verticalLayout_17.setSpacing(3)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.humanIcon = QPushButton(self.frame_8)
        self.humanIcon.setObjectName(u"humanIcon")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.humanIcon.sizePolicy().hasHeightForWidth())
        self.humanIcon.setSizePolicy(sizePolicy2)
        self.humanIcon.setMinimumSize(QSize(0, 0))
        icon6 = QIcon()
        icon6.addFile(u"icons/human - white.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.humanIcon.setIcon(icon6)
        self.humanIcon.setIconSize(QSize(30, 30))

        self.verticalLayout_17.addWidget(self.humanIcon, 0, Qt.AlignHCenter)

        self.humanCounter = QLabel(self.frame_8)
        self.humanCounter.setObjectName(u"humanCounter")
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.humanCounter.setFont(font)
        self.humanCounter.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.humanCounter, 0, Qt.AlignHCenter)

        self.warningIcon = QPushButton(self.frame_8)
        self.warningIcon.setObjectName(u"warningIcon")
        sizePolicy2.setHeightForWidth(self.warningIcon.sizePolicy().hasHeightForWidth())
        self.warningIcon.setSizePolicy(sizePolicy2)
        self.warningIcon.setMinimumSize(QSize(30, 30))
        self.warningIcon.setMaximumSize(QSize(16777215, 30))
        self.warningIcon.setIconSize(QSize(30, 30))

        self.verticalLayout_17.addWidget(self.warningIcon, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame_8)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.reloadBtn = QPushButton(self.frame_3)
        self.reloadBtn.setObjectName(u"reloadBtn")
        icon7 = QIcon()
        icon7.addFile(u"icons/refresh-ccw - white.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.reloadBtn.setIcon(icon7)
        self.reloadBtn.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.reloadBtn)

        self.runBtn = QPushButton(self.frame_3)
        self.runBtn.setObjectName(u"runBtn")
        icon8 = QIcon()
        icon8.addFile(u"icons/play-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.runBtn.setIcon(icon8)
        self.runBtn.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.runBtn)

        self.settingsBtn = QPushButton(self.frame_3)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u"icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon9)
        self.settingsBtn.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.settingsBtn)

        self.infoBtn = QPushButton(self.frame_3)
        self.infoBtn.setObjectName(u"infoBtn")
        self.infoBtn.setAutoFillBackground(False)
        icon10 = QIcon()
        icon10.addFile(u"icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.infoBtn.setIcon(icon10)
        self.infoBtn.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.infoBtn)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.leftMenuSubContainer)


        self.horizontalLayout.addWidget(self.leftMenuContainer)

        self.centerMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        sizePolicy1.setHeightForWidth(self.centerMenuContainer.sizePolicy().hasHeightForWidth())
        self.centerMenuContainer.setSizePolicy(sizePolicy1)
        self.centerMenuContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_5 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer = QWidget(self.centerMenuContainer)
        self.centerMenuSubContainer.setObjectName(u"centerMenuSubContainer")
        self.centerMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_6 = QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_4 = QFrame(self.centerMenuSubContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.sideBarLabel = QLabel(self.frame_4)
        self.sideBarLabel.setObjectName(u"sideBarLabel")
        sizePolicy.setHeightForWidth(self.sideBarLabel.sizePolicy().hasHeightForWidth())
        self.sideBarLabel.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(13)
        self.sideBarLabel.setFont(font1)
        self.sideBarLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.sideBarLabel)

        self.sideBarCloseBtn = QPushButton(self.frame_4)
        self.sideBarCloseBtn.setObjectName(u"sideBarCloseBtn")
        icon11 = QIcon()
        icon11.addFile(u"icons/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sideBarCloseBtn.setIcon(icon11)
        self.sideBarCloseBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.sideBarCloseBtn, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_4)

        self.sideBarWidget = QCustomStackedWidget(self.centerMenuSubContainer)
        self.sideBarWidget.setObjectName(u"sideBarWidget")
        self.sideBarPage1 = QWidget()
        self.sideBarPage1.setObjectName(u"sideBarPage1")
        self.verticalLayout_18 = QVBoxLayout(self.sideBarPage1)
        self.verticalLayout_18.setSpacing(10)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_3)

        self.frame_10 = QFrame(self.sideBarPage1)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_10)
        self.verticalLayout_14.setSpacing(3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_10)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 22))
        font2 = QFont()
        font2.setPointSize(12)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_10.setSpacing(3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.confidenceSlider = QSlider(self.frame_11)
        self.confidenceSlider.setObjectName(u"confidenceSlider")
        self.confidenceSlider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid;\n"
"	border-radius: 2px;\n"
"	border-color: rgb(30, 30, 30);\n"
"    height: 3px;\n"
"    margin: 0px;\n"
"	background-color: rgb(37, 37, 37);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(48, 48, 48);\n"
"    border: 1px solid;\n"
"	border-radius: 4px;\n"
"	border-color: rgb(35, 35, 35);\n"
"    width: 12px;\n"
"    margin: -5px -1px;\n"
"}")
        self.confidenceSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_10.addWidget(self.confidenceSlider)

        self.confidenceText = QLabel(self.frame_11)
        self.confidenceText.setObjectName(u"confidenceText")
        self.confidenceText.setMinimumSize(QSize(20, 0))
        self.confidenceText.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_10.addWidget(self.confidenceText)


        self.verticalLayout_14.addWidget(self.frame_11, 0, Qt.AlignTop)


        self.verticalLayout_18.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.sideBarPage1)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_9)
        self.verticalLayout_13.setSpacing(3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_18.addWidget(self.frame_9)

        self.frame_12 = QFrame(self.sideBarPage1)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_12)
        self.verticalLayout_15.setSpacing(3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_15.addItem(self.verticalSpacer_6)

        self.label_2 = QLabel(self.frame_12)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setMaximumSize(QSize(16777215, 22))
        self.label_2.setBaseSize(QSize(0, 0))
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_2)

        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_11.setSpacing(3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.overlapSlider = QSlider(self.frame_13)
        self.overlapSlider.setObjectName(u"overlapSlider")
        self.overlapSlider.setMinimumSize(QSize(0, 0))
        self.overlapSlider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid;\n"
"	border-radius: 2px;\n"
"	border-color: rgb(30, 30, 30);\n"
"    height: 3px;\n"
"    margin: 0px;\n"
"	background-color: rgb(37, 37, 37);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(48, 48, 48);\n"
"    border: 1px solid;\n"
"	border-radius: 4px;\n"
"	border-color: rgb(35, 35, 35);\n"
"    width: 12px;\n"
"    margin: -5px -1px;\n"
"}")
        self.overlapSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_11.addWidget(self.overlapSlider)

        self.overlapText = QLabel(self.frame_13)
        self.overlapText.setObjectName(u"overlapText")
        self.overlapText.setMinimumSize(QSize(20, 0))

        self.horizontalLayout_11.addWidget(self.overlapText)


        self.verticalLayout_15.addWidget(self.frame_13, 0, Qt.AlignTop)


        self.verticalLayout_18.addWidget(self.frame_12)

        self.frame_14 = QFrame(self.sideBarPage1)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_14)
        self.verticalLayout_16.setSpacing(3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_16.addItem(self.verticalSpacer_7)

        self.label_5 = QLabel(self.frame_14)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 22))
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_5)

        self.lineSpinBox = QSpinBox(self.frame_14)
        self.lineSpinBox.setObjectName(u"lineSpinBox")
        sizePolicy1.setHeightForWidth(self.lineSpinBox.sizePolicy().hasHeightForWidth())
        self.lineSpinBox.setSizePolicy(sizePolicy1)
        self.lineSpinBox.setMinimumSize(QSize(0, 22))
        self.lineSpinBox.setFont(font2)
        self.lineSpinBox.setAutoFillBackground(False)
        self.lineSpinBox.setStyleSheet(u"QSpinBox {\n"
"    border: 1px solid rgb(30, 30, 30);\n"
"	border-radius: 5px;\n"
"	color: white;\n"
" 	background-color: rgb(51, 51, 51);\n"
"}")
        self.lineSpinBox.setKeyboardTracking(False)
        self.lineSpinBox.setMinimum(1)
        self.lineSpinBox.setMaximum(3)

        self.verticalLayout_16.addWidget(self.lineSpinBox)

        self.verticalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_16.addItem(self.verticalSpacer_8)


        self.verticalLayout_18.addWidget(self.frame_14)

        self.frame_16 = QFrame(self.sideBarPage1)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_16)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_16)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 22))
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)

        self.heatmapCombo = QComboBox(self.frame_16)
        self.heatmapCombo.setObjectName(u"heatmapCombo")
        sizePolicy1.setHeightForWidth(self.heatmapCombo.sizePolicy().hasHeightForWidth())
        self.heatmapCombo.setSizePolicy(sizePolicy1)
        self.heatmapCombo.setMinimumSize(QSize(0, 22))
        self.heatmapCombo.setFont(font2)
        self.heatmapCombo.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid rgb(30, 30, 30);\n"
"	border-radius: 5px;\n"
"	color: white;\n"
" 	background-color: rgb(51, 51, 51);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px rgb(30, 30, 30);\n"
"    selection-background-color: gray;\n"
"	background-color: rgb(65, 65, 65);\n"
"	color: white;\n"
"}")

        self.verticalLayout_7.addWidget(self.heatmapCombo)


        self.verticalLayout_18.addWidget(self.frame_16)

        self.verticalSpacer_5 = QSpacerItem(20, 45, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_5)

        self.frame_19 = QFrame(self.sideBarPage1)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.maxDetectionsCheckBox = QCheckBox(self.frame_19)
        self.maxDetectionsCheckBox.setObjectName(u"maxDetectionsCheckBox")
        self.maxDetectionsCheckBox.setFont(font2)
        self.maxDetectionsCheckBox.setStyleSheet(u"QCheckBox {\n"
"    spacing: 10px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"	border: 1px solid white;\n"
"	background-color: rgb(51, 51, 51);\n"
"	\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	width: 14px;\n"
"    height: 14px;\n"
"	border: 1px solid rgb(51, 51, 51);\n"
"    background-color: rgb(150, 150, 150);\n"
"}\n"
"")

        self.horizontalLayout_13.addWidget(self.maxDetectionsCheckBox)

        self.maxDetectionsInput = QLineEdit(self.frame_19)
        self.maxDetectionsInput.setObjectName(u"maxDetectionsInput")
        self.maxDetectionsInput.setMaximumSize(QSize(40, 16777215))
        self.maxDetectionsInput.setFont(font2)
        self.maxDetectionsInput.setFocusPolicy(Qt.ClickFocus)
        self.maxDetectionsInput.setStyleSheet(u"QLineEdit{\n"
"	border: 1px solid white;\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"	selection-background-color: rgb(100, 100, 100);\n"
"	background-color: gray\n"
"}")

        self.horizontalLayout_13.addWidget(self.maxDetectionsInput)


        self.verticalLayout_18.addWidget(self.frame_19)

        self.labelsCheckBox = QCheckBox(self.sideBarPage1)
        self.labelsCheckBox.setObjectName(u"labelsCheckBox")
        self.labelsCheckBox.setFont(font2)
        self.labelsCheckBox.setStyleSheet(u"QCheckBox {\n"
"    spacing: 10px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"	border: 1px solid white;\n"
"	background-color: rgb(51, 51, 51);\n"
"	\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	width: 14px;\n"
"    height: 14px;\n"
"	border: 1px solid rgb(51, 51, 51);\n"
"    background-color: rgb(150, 150, 150);\n"
"}\n"
"")

        self.verticalLayout_18.addWidget(self.labelsCheckBox)

        self.confidenceCheckBox = QCheckBox(self.sideBarPage1)
        self.confidenceCheckBox.setObjectName(u"confidenceCheckBox")
        self.confidenceCheckBox.setFont(font2)
        self.confidenceCheckBox.setStyleSheet(u"QCheckBox {\n"
"    spacing: 10px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"	border: 1px solid white;\n"
"	background-color: rgb(51, 51, 51);\n"
"	\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	width: 14px;\n"
"    height: 14px;\n"
"	border: 1px solid rgb(51, 51, 51);\n"
"    background-color: rgb(150, 150, 150);\n"
"}\n"
"")

        self.verticalLayout_18.addWidget(self.confidenceCheckBox)

        self.overlapCheckBox = QCheckBox(self.sideBarPage1)
        self.overlapCheckBox.setObjectName(u"overlapCheckBox")
        self.overlapCheckBox.setFont(font2)
        self.overlapCheckBox.setStyleSheet(u"QCheckBox {\n"
"    spacing: 10px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"	border: 1px solid white;\n"
"	background-color: rgb(51, 51, 51);\n"
"	\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	width: 14px;\n"
"    height: 14px;\n"
"	border: 1px solid rgb(51, 51, 51);\n"
"    background-color: rgb(150, 150, 150);\n"
"}\n"
"")

        self.verticalLayout_18.addWidget(self.overlapCheckBox)

        self.cudaCheckBox = QCheckBox(self.sideBarPage1)
        self.cudaCheckBox.setObjectName(u"cudaCheckBox")
        self.cudaCheckBox.setFont(font2)
        self.cudaCheckBox.setStyleSheet(u"QCheckBox {\n"
"    spacing: 10px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"	border: 1px solid white;\n"
"	background-color: rgb(51, 51, 51);\n"
"	\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	width: 14px;\n"
"    height: 14px;\n"
"	border: 1px solid rgb(51, 51, 51);\n"
"    background-color: rgb(150, 150, 150);\n"
"}\n"
"")

        self.verticalLayout_18.addWidget(self.cudaCheckBox)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_4)

        self.sideBarWidget.addWidget(self.sideBarPage1)
        self.sideBarPage2 = QWidget()
        self.sideBarPage2.setObjectName(u"sideBarPage2")
        self.verticalLayout_8 = QVBoxLayout(self.sideBarPage2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.informationText = QLabel(self.sideBarPage2)
        self.informationText.setObjectName(u"informationText")
        self.informationText.setFont(font1)
        self.informationText.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.informationText.setWordWrap(False)

        self.verticalLayout_8.addWidget(self.informationText)

        self.sideBarWidget.addWidget(self.sideBarPage2)

        self.verticalLayout_6.addWidget(self.sideBarWidget)


        self.verticalLayout_5.addWidget(self.centerMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.centerMenuContainer)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy)
        self.mainBodyContainer.setMinimumSize(QSize(0, 0))
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        sizePolicy.setHeightForWidth(self.headerContainer.sizePolicy().hasHeightForWidth())
        self.headerContainer.setSizePolicy(sizePolicy)
        self.horizontalLayout_5 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.headerContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setSpacing(3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.icon = QPushButton(self.frame_5)
        self.icon.setObjectName(u"icon")
        icon12 = QIcon()
        icon12.addFile(u"icons/shutter.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon.setIcon(icon12)
        self.icon.setIconSize(QSize(25, 25))

        self.horizontalLayout_7.addWidget(self.icon)

        self.thermografi = QLabel(self.frame_5)
        self.thermografi.setObjectName(u"thermografi")
        sizePolicy1.setHeightForWidth(self.thermografi.sizePolicy().hasHeightForWidth())
        self.thermografi.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(True)
        font3.setItalic(False)
        self.thermografi.setFont(font3)
        self.thermografi.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.thermografi)


        self.horizontalLayout_5.addWidget(self.frame_5, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frame_6 = QFrame(self.headerContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.playBtn = QPushButton(self.frame_6)
        self.playBtn.setObjectName(u"playBtn")
        icon13 = QIcon()
        icon13.addFile(u"icons/play.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.playBtn.setIcon(icon13)
        self.playBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_6.addWidget(self.playBtn)

        self.pauseBtn = QPushButton(self.frame_6)
        self.pauseBtn.setObjectName(u"pauseBtn")
        icon14 = QIcon()
        icon14.addFile(u"icons/pause.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pauseBtn.setIcon(icon14)
        self.pauseBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_6.addWidget(self.pauseBtn)

        self.stopBtn = QPushButton(self.frame_6)
        self.stopBtn.setObjectName(u"stopBtn")
        icon15 = QIcon()
        icon15.addFile(u"icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.stopBtn.setIcon(icon15)
        self.stopBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_6.addWidget(self.stopBtn)


        self.horizontalLayout_5.addWidget(self.frame_6, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.minimizeBtn = QPushButton(self.frame_7)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        icon16 = QIcon()
        icon16.addFile(u"icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon16)
        self.minimizeBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.minimizeBtn)

        self.maximizeBtn = QPushButton(self.frame_7)
        self.maximizeBtn.setObjectName(u"maximizeBtn")
        icon17 = QIcon()
        icon17.addFile(u"icons/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeBtn.setIcon(icon17)
        self.maximizeBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.maximizeBtn)

        self.closeBtn = QPushButton(self.frame_7)
        self.closeBtn.setObjectName(u"closeBtn")
        icon18 = QIcon()
        icon18.addFile(u"icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon18)
        self.closeBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.closeBtn)


        self.horizontalLayout_5.addWidget(self.frame_7, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_9.addWidget(self.headerContainer, 0, Qt.AlignTop)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy3)
        self.mainBodyContent.setMinimumSize(QSize(550, 570))
        self.verticalLayout_12 = QVBoxLayout(self.mainBodyContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.mainContentsWidget = QCustomStackedWidget(self.mainBodyContent)
        self.mainContentsWidget.setObjectName(u"mainContentsWidget")
        self.mainContentsWidget.setMinimumSize(QSize(0, 0))
        self.mainContentsWidget.setMaximumSize(QSize(16777215, 16777215))
        self.mainContentsWidget.setStyleSheet(u"background-color:  #1f232a;\n"
"border-bottom-right-radius: 10px")
        self.loginPage = QWidget()
        self.loginPage.setObjectName(u"loginPage")
        self.verticalLayout_22 = QVBoxLayout(self.loginPage)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.loginPage)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_20)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy4)
        self.frame_21.setMinimumSize(QSize(341, 291))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_21)
        self.verticalLayout_24.setSpacing(2)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.frame_21)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.pushButton = QPushButton(self.frame_22)
        self.pushButton.setObjectName(u"pushButton")
        icon19 = QIcon()
        icon19.addFile(u"icons/logo.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon19)
        self.pushButton.setIconSize(QSize(500, 200))

        self.horizontalLayout_14.addWidget(self.pushButton)


        self.verticalLayout_24.addWidget(self.frame_22, 0, Qt.AlignHCenter)

        self.frame_23 = QFrame(self.frame_21)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_23)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_24 = QFrame(self.frame_23)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_15.setSpacing(2)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, -1, 0, 0)
        self.label_8 = QLabel(self.frame_24)
        self.label_8.setObjectName(u"label_8")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.label_8.setFont(font4)

        self.horizontalLayout_15.addWidget(self.label_8)

        self.usernameInput = QLineEdit(self.frame_24)
        self.usernameInput.setObjectName(u"usernameInput")
        sizePolicy1.setHeightForWidth(self.usernameInput.sizePolicy().hasHeightForWidth())
        self.usernameInput.setSizePolicy(sizePolicy1)
        self.usernameInput.setMinimumSize(QSize(230, 0))
        self.usernameInput.setMaximumSize(QSize(230, 16777215))
        self.usernameInput.setFont(font2)
        self.usernameInput.setFocusPolicy(Qt.ClickFocus)
        self.usernameInput.setStyleSheet(u"QLineEdit{\n"
"	border: 1px solid white;\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"	selection-background-color: rgb(100, 100, 100);\n"
"	background-color: gray\n"
"}")

        self.horizontalLayout_15.addWidget(self.usernameInput, 0, Qt.AlignRight)


        self.verticalLayout_23.addWidget(self.frame_24)

        self.frame_25 = QFrame(self.frame_23)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_16.setSpacing(6)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, -1, 0, 0)
        self.label_9 = QLabel(self.frame_25)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font4)

        self.horizontalLayout_16.addWidget(self.label_9)

        self.passwordInput = QLineEdit(self.frame_25)
        self.passwordInput.setObjectName(u"passwordInput")
        sizePolicy1.setHeightForWidth(self.passwordInput.sizePolicy().hasHeightForWidth())
        self.passwordInput.setSizePolicy(sizePolicy1)
        self.passwordInput.setMinimumSize(QSize(230, 0))
        self.passwordInput.setMaximumSize(QSize(230, 16777215))
        self.passwordInput.setFont(font2)
        self.passwordInput.setFocusPolicy(Qt.ClickFocus)
        self.passwordInput.setStyleSheet(u"QLineEdit{\n"
"	border: 1px solid white;\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"	selection-background-color: rgb(100, 100, 100);\n"
"	background-color: gray\n"
"}")

        self.horizontalLayout_16.addWidget(self.passwordInput, 0, Qt.AlignRight)


        self.verticalLayout_23.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.frame_23)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setLayoutDirection(Qt.LeftToRight)
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 9, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(84, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_3)

        self.loginBtn = QPushButton(self.frame_26)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setMinimumSize(QSize(150, 26))
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setStyleStrategy(QFont.PreferDefault)
        self.loginBtn.setFont(font5)
        self.loginBtn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(61, 65, 72);\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: beige;\n"
"	border-radius: 8px\n"
"}")

        self.horizontalLayout_17.addWidget(self.loginBtn)

        self.horizontalSpacer_4 = QSpacerItem(83, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_4)


        self.verticalLayout_23.addWidget(self.frame_26)


        self.verticalLayout_24.addWidget(self.frame_23, 0, Qt.AlignHCenter)

        self.frame_27 = QFrame(self.frame_21)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMaximumSize(QSize(16777215, 20))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_15 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.horizontalLayout_18.addItem(self.verticalSpacer_15)

        self.invalidText = QLabel(self.frame_27)
        self.invalidText.setObjectName(u"invalidText")
        font6 = QFont()
        font6.setBold(True)
        self.invalidText.setFont(font6)
        self.invalidText.setStyleSheet(u"QLabel {\n"
"	color: red;\n"
"}")

        self.horizontalLayout_18.addWidget(self.invalidText)

        self.verticalSpacer_16 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.horizontalLayout_18.addItem(self.verticalSpacer_16)


        self.verticalLayout_24.addWidget(self.frame_27, 0, Qt.AlignHCenter)


        self.verticalLayout_25.addWidget(self.frame_21)


        self.verticalLayout_22.addWidget(self.frame_20, 0, Qt.AlignHCenter)

        self.mainContentsWidget.addWidget(self.loginPage)
        self.mainPage1 = QWidget()
        self.mainPage1.setObjectName(u"mainPage1")
        self.verticalLayout_10 = QVBoxLayout(self.mainPage1)
        self.verticalLayout_10.setSpacing(2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.outputImage = QLabel(self.mainPage1)
        self.outputImage.setObjectName(u"outputImage")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.outputImage.sizePolicy().hasHeightForWidth())
        self.outputImage.setSizePolicy(sizePolicy5)
        self.outputImage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.outputImage)

        self.frame_15 = QFrame(self.mainPage1)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.currentTime = QLabel(self.frame_15)
        self.currentTime.setObjectName(u"currentTime")
        self.currentTime.setMinimumSize(QSize(70, 0))
        self.currentTime.setFont(font2)
        self.currentTime.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.horizontalLayout_8.addWidget(self.currentTime)

        self.videoSlider = Slider(self.frame_15)
        self.videoSlider.setObjectName(u"videoSlider")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.videoSlider.sizePolicy().hasHeightForWidth())
        self.videoSlider.setSizePolicy(sizePolicy6)
        self.videoSlider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid;\n"
"	border-radius: 2px;\n"
"	border-color: rgb(30, 30, 30);\n"
"    height: 5px;\n"
"    margin: 0px;\n"
"	background-color: rgb(200, 55, 58);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(48, 66, 66);\n"
"    border: 1px solid;\n"
"	border-radius: 7px;\n"
"	border-color: rgb(33, 33, 33);\n"
"    width: 12px;\n"
"    margin: -5px -1px;\n"
"}")
        self.videoSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_8.addWidget(self.videoSlider, 0, Qt.AlignVCenter)

        self.totalTime = QLabel(self.frame_15)
        self.totalTime.setObjectName(u"totalTime")
        self.totalTime.setMinimumSize(QSize(70, 0))
        self.totalTime.setFont(font2)
        self.totalTime.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_8.addWidget(self.totalTime)


        self.verticalLayout_10.addWidget(self.frame_15)

        self.mainContentsWidget.addWidget(self.mainPage1)
        self.mainPage2 = QWidget()
        self.mainPage2.setObjectName(u"mainPage2")
        self.verticalLayout_11 = QVBoxLayout(self.mainPage2)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.heatmapWidget = QStackedWidget(self.mainPage2)
        self.heatmapWidget.setObjectName(u"heatmapWidget")
        self.heatmapPage1 = QWidget()
        self.heatmapPage1.setObjectName(u"heatmapPage1")
        self.verticalLayout_21 = QVBoxLayout(self.heatmapPage1)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.currentHeatmapOutput = QLabel(self.heatmapPage1)
        self.currentHeatmapOutput.setObjectName(u"currentHeatmapOutput")
        sizePolicy5.setHeightForWidth(self.currentHeatmapOutput.sizePolicy().hasHeightForWidth())
        self.currentHeatmapOutput.setSizePolicy(sizePolicy5)
        self.currentHeatmapOutput.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.currentHeatmapOutput)

        self.heatmapDesc = QLabel(self.heatmapPage1)
        self.heatmapDesc.setObjectName(u"heatmapDesc")
        self.heatmapDesc.setFont(font)
        self.heatmapDesc.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.heatmapDesc)

        self.heatmapWidget.addWidget(self.heatmapPage1)
        self.heatmapPage2 = QWidget()
        self.heatmapPage2.setObjectName(u"heatmapPage2")
        self.verticalLayout_19 = QVBoxLayout(self.heatmapPage2)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.heatmapPage2)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy5.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy5)
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_17)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.overallHeatmapOutput = QLabel(self.frame_17)
        self.overallHeatmapOutput.setObjectName(u"overallHeatmapOutput")
        sizePolicy5.setHeightForWidth(self.overallHeatmapOutput.sizePolicy().hasHeightForWidth())
        self.overallHeatmapOutput.setSizePolicy(sizePolicy5)
        self.overallHeatmapOutput.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.overallHeatmapOutput)

        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy2.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy2)
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_12.setSpacing(2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.currentHeatmap = QLabel(self.frame_18)
        self.currentHeatmap.setObjectName(u"currentHeatmap")
        self.currentHeatmap.setMinimumSize(QSize(70, 0))
        self.currentHeatmap.setMaximumSize(QSize(70, 16777215))
        self.currentHeatmap.setFont(font2)
        self.currentHeatmap.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.horizontalLayout_12.addWidget(self.currentHeatmap)

        self.heatmapStartSlider = Slider(self.frame_18)
        self.heatmapStartSlider.setObjectName(u"heatmapStartSlider")
        sizePolicy5.setHeightForWidth(self.heatmapStartSlider.sizePolicy().hasHeightForWidth())
        self.heatmapStartSlider.setSizePolicy(sizePolicy5)
        self.heatmapStartSlider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid;\n"
"	border-radius: 2px;\n"
"	border-color: rgb(30, 30, 30);\n"
"    height: 5px;\n"
"    margin: 0px;\n"
"	background-color: rgb(200, 55, 58);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(48, 66, 66);\n"
"    border: 1px solid;\n"
"	border-radius: 7px;\n"
"	border-color: rgb(33, 33, 33);\n"
"    width: 12px;\n"
"    margin: -5px -1px;\n"
"}")
        self.heatmapStartSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_12.addWidget(self.heatmapStartSlider)

        self.horizontalSpacer = QSpacerItem(72, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer)


        self.verticalLayout_20.addWidget(self.frame_18)

        self.frame_28 = QFrame(self.frame_17)
        self.frame_28.setObjectName(u"frame_28")
        sizePolicy2.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy2)
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_19.setSpacing(2)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(72, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_2)

        self.heatmapEndSlider = Slider(self.frame_28)
        self.heatmapEndSlider.setObjectName(u"heatmapEndSlider")
        sizePolicy5.setHeightForWidth(self.heatmapEndSlider.sizePolicy().hasHeightForWidth())
        self.heatmapEndSlider.setSizePolicy(sizePolicy5)
        self.heatmapEndSlider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid;\n"
"	border-radius: 2px;\n"
"	border-color: rgb(30, 30, 30);\n"
"    height: 5px;\n"
"    margin: 0px;\n"
"	background-color: rgb(200, 55, 58);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(48, 66, 66);\n"
"    border: 1px solid;\n"
"	border-radius: 7px;\n"
"	border-color: rgb(33, 33, 33);\n"
"    width: 12px;\n"
"    margin: -5px -1px;\n"
"}")
        self.heatmapEndSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_19.addWidget(self.heatmapEndSlider)

        self.endHeatmap = QLabel(self.frame_28)
        self.endHeatmap.setObjectName(u"endHeatmap")
        self.endHeatmap.setMinimumSize(QSize(70, 0))
        self.endHeatmap.setMaximumSize(QSize(70, 16777215))
        self.endHeatmap.setBaseSize(QSize(0, 0))
        self.endHeatmap.setFont(font2)
        self.endHeatmap.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_19.addWidget(self.endHeatmap)


        self.verticalLayout_20.addWidget(self.frame_28)


        self.verticalLayout_19.addWidget(self.frame_17)

        self.heatmapDesc_2 = QLabel(self.heatmapPage2)
        self.heatmapDesc_2.setObjectName(u"heatmapDesc_2")
        self.heatmapDesc_2.setFont(font)
        self.heatmapDesc_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.heatmapDesc_2)

        self.heatmapWidget.addWidget(self.heatmapPage2)

        self.verticalLayout_11.addWidget(self.heatmapWidget)

        self.mainContentsWidget.addWidget(self.mainPage2)

        self.verticalLayout_12.addWidget(self.mainContentsWidget)

        self.sizeGrip = QFrame(self.mainBodyContent)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(20, 20))
        self.sizeGrip.setMaximumSize(QSize(20, 20))
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.sizeGrip)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.resize = QPushButton(self.sizeGrip)
        self.resize.setObjectName(u"resize")
        icon20 = QIcon()
        icon20.addFile(u"icons/resize_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.resize.setIcon(icon20)
        self.resize.setIconSize(QSize(20, 20))

        self.horizontalLayout_9.addWidget(self.resize)


        self.verticalLayout_12.addWidget(self.sizeGrip, 0, Qt.AlignRight)


        self.verticalLayout_9.addWidget(self.mainBodyContent)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.sideBarWidget.setCurrentIndex(0)
        self.heatmapCombo.setCurrentIndex(-1)
        self.mainContentsWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u" Home", None))
#if QT_CONFIG(tooltip)
        self.dataBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Data Analysis", None))
#endif // QT_CONFIG(tooltip)
        self.dataBtn.setText(QCoreApplication.translate("MainWindow", u" Data Analysis", None))
#if QT_CONFIG(tooltip)
        self.openBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Open", None))
#endif // QT_CONFIG(tooltip)
        self.openBtn.setText(QCoreApplication.translate("MainWindow", u" Open", None))
#if QT_CONFIG(tooltip)
        self.cameraBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Open", None))
#endif // QT_CONFIG(tooltip)
        self.cameraBtn.setText(QCoreApplication.translate("MainWindow", u" Camera", None))
        self.humanIcon.setText("")
        self.humanCounter.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.warningIcon.setText("")
#if QT_CONFIG(tooltip)
        self.reloadBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Run", None))
#endif // QT_CONFIG(tooltip)
        self.reloadBtn.setText(QCoreApplication.translate("MainWindow", u" Refresh", None))
#if QT_CONFIG(tooltip)
        self.runBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Run", None))
#endif // QT_CONFIG(tooltip)
        self.runBtn.setText(QCoreApplication.translate("MainWindow", u" Run", None))
#if QT_CONFIG(tooltip)
        self.settingsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u" Settings", None))
#if QT_CONFIG(tooltip)
        self.infoBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Info", None))
#endif // QT_CONFIG(tooltip)
        self.infoBtn.setText(QCoreApplication.translate("MainWindow", u" Info", None))
        self.sideBarLabel.setText(QCoreApplication.translate("MainWindow", u"More Menu", None))
        self.sideBarCloseBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Confidence Threshold", None))
        self.confidenceText.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Overlap Threshold", None))
        self.overlapText.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Line Thickness", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Heatmap Type", None))
        self.heatmapCombo.setCurrentText("")
        self.heatmapCombo.setPlaceholderText("")
        self.maxDetectionsCheckBox.setText(QCoreApplication.translate("MainWindow", u"Max Detections:", None))
        self.maxDetectionsInput.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.labelsCheckBox.setText(QCoreApplication.translate("MainWindow", u"Hide Labels", None))
        self.confidenceCheckBox.setText(QCoreApplication.translate("MainWindow", u"Hide Confidence", None))
        self.overlapCheckBox.setText(QCoreApplication.translate("MainWindow", u"Overlap Heatmap", None))
        self.cudaCheckBox.setText(QCoreApplication.translate("MainWindow", u"CUDA Quick Process", None))
        self.informationText.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.icon.setText("")
        self.thermografi.setText(QCoreApplication.translate("MainWindow", u"Thermografi", None))
        self.playBtn.setText("")
        self.pauseBtn.setText("")
        self.stopBtn.setText("")
        self.minimizeBtn.setText("")
        self.maximizeBtn.setText("")
        self.closeBtn.setText("")
        self.pushButton.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Username: ", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.loginBtn.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.invalidText.setText(QCoreApplication.translate("MainWindow", u"Invalid username and/or password", None))
        self.outputImage.setText("")
        self.currentTime.setText(QCoreApplication.translate("MainWindow", u"0:00:00", None))
        self.totalTime.setText(QCoreApplication.translate("MainWindow", u"0:00:00", None))
        self.currentHeatmapOutput.setText("")
        self.heatmapDesc.setText(QCoreApplication.translate("MainWindow", u"Current Heatmap", None))
        self.overallHeatmapOutput.setText("")
        self.currentHeatmap.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.endHeatmap.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.heatmapDesc_2.setText(QCoreApplication.translate("MainWindow", u"Overall Heatmap", None))
        self.resize.setText("")
    # retranslateUi

class Slider(QSlider):
    change_event = False
    intersect_event = False

    def mousePressEvent(self, event):
        super(Slider, self).mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            val = self.pixelPosToRangeValue(event.pos())
            self.setValue(val)
        self.change(True)

    def pixelPosToRangeValue(self, pos):
        opt = QStyleOptionSlider()
        self.initStyleOption(opt)
        gr = self.style().subControlRect(QStyle.CC_Slider, opt, QStyle.SC_SliderGroove, self)
        sr = self.style().subControlRect(QStyle.CC_Slider, opt, QStyle.SC_SliderHandle, self)

        if self.orientation() == Qt.Horizontal:
            sliderLength = sr.width()
            sliderMin = gr.x()
            sliderMax = gr.right() - sliderLength + 1
        else:
            sliderLength = sr.height()
            sliderMin = gr.y()
            sliderMax = gr.bottom() - sliderLength + 1;
        pr = pos - sr.center() + sr.topLeft()
        p = pr.x() if self.orientation() == Qt.Horizontal else pr.y()
        self.intersect_event = True
        return QStyle.sliderValueFromPosition(self.minimum(), self.maximum(), p - sliderMin,
                                              sliderMax - sliderMin, opt.upsideDown)

    def change(self, state):
        self.change_event = state

    def change_event_return(self):
        return self.change_event
