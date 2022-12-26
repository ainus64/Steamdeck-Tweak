# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceEpIJAi.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import theme_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 480)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(1280, 800))
        MainWindow.setStyleSheet(u"*{\n"
"	border:none;\n"
"	color:white;\n"
"	font-family: \"bertina Sans\";\n"
"}\n"
"\n"
"/* Vertical Scrollbar */\n"
"QScrollBar:vertical{\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	width: 14px;\n"
"	margin: 15px 0 15px 0;\n"
"	border-radius: 0px;\n"
"}\n"
"/* Handle Bar Vertical */\n"
"QScrollBar::handle:vertical {\n"
"	background-color: rgb(80, 80, 122);\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"/* btn Top Scrollbar */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical :hover{\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::sub-line:vertical :pressed{\n"
""
                        "	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* boton Down Scrollbar */\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical :hover{\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::add-line:vertical :pressed{\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* Reset Arrow */\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setFamily(u"bertina Sans")
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setStyleSheet(u"")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_body)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.main_body)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"background-color:rgb(9,5,13);")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.frame_3 = QFrame(self.header_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.frame_3, 0, Qt.AlignLeft)

        self.frame_2 = QFrame(self.header_frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.AppName = QLabel(self.frame_2)
        self.AppName.setObjectName(u"AppName")
        font1 = QFont()
        font1.setFamily(u"bertina Sans")
        font1.setPointSize(14)
        self.AppName.setFont(font1)

        self.horizontalLayout_6.addWidget(self.AppName)


        self.horizontalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.main_body_contents = QFrame(self.main_body)
        self.main_body_contents.setObjectName(u"main_body_contents")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.main_body_contents.sizePolicy().hasHeightForWidth())
        self.main_body_contents.setSizePolicy(sizePolicy2)
        self.main_body_contents.setStyleSheet(u"*{\n"
"	background-color: rgb(  33, 47, 61  )\n"
"}\n"
"\n"
"")
        self.main_body_contents.setFrameShape(QFrame.StyledPanel)
        self.main_body_contents.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.main_body_contents)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.main_body_contents)
        self.frame.setObjectName(u"frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.slide_menu_container = QFrame(self.frame)
        self.slide_menu_container.setObjectName(u"slide_menu_container")
        sizePolicy1.setHeightForWidth(self.slide_menu_container.sizePolicy().hasHeightForWidth())
        self.slide_menu_container.setSizePolicy(sizePolicy1)
        self.slide_menu_container.setMinimumSize(QSize(200, 0))
        self.slide_menu_container.setMaximumSize(QSize(0, 16777215))
        self.slide_menu_container.setStyleSheet(u"*{\n"
"	background-color:rgb(23, 32, 42)\n"
"}\n"
"\n"
"/* Button Styles */\n"
"QPushButton{\n"
"	font-size: 16px;\n"
"	font-weight:  bold;\n"
"	text-align: left;\n"
"	margin: 3px;\n"
"	font-family: \"Betina Sans\";\n"
"	padding: 5px 5px;\n"
"	background-color: rgb(59, 59, 90);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(185, 0, 92);\n"
"}")
        self.slide_menu_container.setFrameShape(QFrame.StyledPanel)
        self.slide_menu_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.slide_menu_container)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.slide_menu = QFrame(self.slide_menu_container)
        self.slide_menu.setObjectName(u"slide_menu")
        self.slide_menu.setMinimumSize(QSize(200, 0))
        self.slide_menu.setMaximumSize(QSize(16777215, 16777215))
        self.slide_menu.setAutoFillBackground(False)
        self.slide_menu.setStyleSheet(u"")
        self.slide_menu.setFrameShape(QFrame.StyledPanel)
        self.slide_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.slide_menu)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.toolBox = QToolBox(self.slide_menu)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setMinimumSize(QSize(73, 0))
        font2 = QFont()
        font2.setFamily(u"bertina Sans")
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setWeight(50)
        self.toolBox.setFont(font2)
        self.toolBox.setStyleSheet(u"QToolBox{\n"
"	background-color:rgb(23,26,2f);\n"
"	text-align: left;\n"
"}\n"
"QToolBox::tab {\n"
"	border-radius: 5px;\n"
"	background-color:rgb(23,26,2f);\n"
"	text-align: left;\n"
"}")
        self.System = QWidget()
        self.System.setObjectName(u"System")
        self.System.setGeometry(QRect(0, 0, 200, 281))
        self.verticalLayout_13 = QVBoxLayout(self.System)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.Caja_de_botones = QFrame(self.System)
        self.Caja_de_botones.setObjectName(u"Caja_de_botones")
        self.Caja_de_botones.setStyleSheet(u"")
        self.Caja_de_botones.setFrameShape(QFrame.StyledPanel)
        self.Caja_de_botones.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.Caja_de_botones)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.installButton_0 = QPushButton(self.Caja_de_botones)
        self.installButton_0.setObjectName(u"installButton_0")
        font3 = QFont()
        font3.setFamily(u"Betina Sans")
        font3.setBold(True)
        font3.setWeight(75)
        self.installButton_0.setFont(font3)

        self.verticalLayout_15.addWidget(self.installButton_0)

        self.installButton_1 = QPushButton(self.Caja_de_botones)
        self.installButton_1.setObjectName(u"installButton_1")
        self.installButton_1.setFont(font3)

        self.verticalLayout_15.addWidget(self.installButton_1)

        self.installButton_2 = QPushButton(self.Caja_de_botones)
        self.installButton_2.setObjectName(u"installButton_2")
        self.installButton_2.setFont(font3)

        self.verticalLayout_15.addWidget(self.installButton_2)

        self.installButton_3 = QPushButton(self.Caja_de_botones)
        self.installButton_3.setObjectName(u"installButton_3")
        self.installButton_3.setFont(font3)

        self.verticalLayout_15.addWidget(self.installButton_3)


        self.verticalLayout_13.addWidget(self.Caja_de_botones, 0, Qt.AlignTop)

        icon = QIcon()
        icon.addFile(u":/theme/icons/package.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.System, icon, u"Sistema")
        self.Software = QWidget()
        self.Software.setObjectName(u"Software")
        self.Software.setGeometry(QRect(0, 0, 200, 281))
        self.verticalLayout_14 = QVBoxLayout(self.Software)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_13 = QFrame(self.Software)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_13)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.unInstallButton_1 = QPushButton(self.frame_13)
        self.unInstallButton_1.setObjectName(u"unInstallButton_1")
        self.unInstallButton_1.setFont(font3)

        self.verticalLayout_16.addWidget(self.unInstallButton_1)

        self.unInstallButton_2 = QPushButton(self.frame_13)
        self.unInstallButton_2.setObjectName(u"unInstallButton_2")
        self.unInstallButton_2.setFont(font3)

        self.verticalLayout_16.addWidget(self.unInstallButton_2)

        self.pushButton_3 = QPushButton(self.frame_13)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_16.addWidget(self.pushButton_3)


        self.verticalLayout_14.addWidget(self.frame_13, 0, Qt.AlignTop)

        icon1 = QIcon()
        icon1.addFile(u":/theme/icons/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.Software, icon1, u"Software")
        self.Options = QWidget()
        self.Options.setObjectName(u"Options")
        self.Options.setGeometry(QRect(0, 0, 200, 281))
        self.verticalLayout_5 = QVBoxLayout(self.Options)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_5 = QFrame(self.Options)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 0))
        self.frame_5.setMaximumSize(QSize(16777215, 294))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_4.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_5)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_4.addWidget(self.pushButton_2, 0, Qt.AlignTop)


        self.verticalLayout_5.addWidget(self.frame_5)

        icon2 = QIcon()
        icon2.addFile(u":/theme/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.Options, icon2, u"Options")

        self.verticalLayout_12.addWidget(self.toolBox)


        self.verticalLayout_11.addWidget(self.slide_menu)


        self.horizontalLayout_9.addWidget(self.slide_menu_container)

        self.bodyContents = QFrame(self.frame)
        self.bodyContents.setObjectName(u"bodyContents")
        self.bodyContents.setSizeIncrement(QSize(0, 0))
        self.bodyContents.setBaseSize(QSize(0, 0))
        self.bodyContents.setStyleSheet(u"")
        self.bodyContents.setFrameShape(QFrame.StyledPanel)
        self.bodyContents.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.bodyContents)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.BoxHeader = QFrame(self.bodyContents)
        self.BoxHeader.setObjectName(u"BoxHeader")
        self.BoxHeader.setFrameShape(QFrame.StyledPanel)
        self.BoxHeader.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.BoxHeader)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.logoTitle = QLabel(self.BoxHeader)
        self.logoTitle.setObjectName(u"logoTitle")
        self.logoTitle.setMinimumSize(QSize(0, 0))
        self.logoTitle.setMaximumSize(QSize(128, 128))
        self.logoTitle.setSizeIncrement(QSize(0, 0))
        self.logoTitle.setStyleSheet(u"")
        self.logoTitle.setPixmap(QPixmap(u":/theme/icons/gamepad.svg"))
        self.logoTitle.setScaledContents(True)
        self.logoTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.logoTitle, 0, Qt.AlignHCenter)

        self.boxTitle = QLabel(self.BoxHeader)
        self.boxTitle.setObjectName(u"boxTitle")
        self.boxTitle.setMaximumSize(QSize(16777215, 128))
        font4 = QFont()
        font4.setFamily(u"bertina Sans")
        font4.setPointSize(16)
        font4.setBold(True)
        font4.setWeight(75)
        self.boxTitle.setFont(font4)

        self.verticalLayout_7.addWidget(self.boxTitle)


        self.verticalLayout_2.addWidget(self.BoxHeader, 0, Qt.AlignHCenter)

        self.boxContainer = QFrame(self.bodyContents)
        self.boxContainer.setObjectName(u"boxContainer")
        self.boxContainer.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.boxContainer.sizePolicy().hasHeightForWidth())
        self.boxContainer.setSizePolicy(sizePolicy3)
        self.boxContainer.setMaximumSize(QSize(16777215, 16777215))
        self.boxContainer.setStyleSheet(u"/* Button Styles */\n"
"QPushButton{\n"
"	font-size: 16px;\n"
"	font-weight:  bold;\n"
"	text-align: left;\n"
"	margin: 3px;\n"
"	font-family: \"Betina Sans\";\n"
"	padding: 5px 5px;\n"
"	background-color: rgb(59, 59, 90);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(185, 0, 92);\n"
"}")
        self.boxContainer.setFrameShape(QFrame.StyledPanel)
        self.boxContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.boxContainer)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.descTitle = QLabel(self.boxContainer)
        self.descTitle.setObjectName(u"descTitle")
        font5 = QFont()
        font5.setFamily(u"bertina Sans")
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setWeight(75)
        self.descTitle.setFont(font5)

        self.verticalLayout_6.addWidget(self.descTitle)

        self.frame_8 = QFrame(self.boxContainer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.descBox = QLabel(self.frame_8)
        self.descBox.setObjectName(u"descBox")
        self.descBox.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.descBox.sizePolicy().hasHeightForWidth())
        self.descBox.setSizePolicy(sizePolicy3)
        self.descBox.setMaximumSize(QSize(1080, 720))
        self.descBox.setSizeIncrement(QSize(0, 0))
        self.descBox.setStyleSheet(u"*{\n"
"	font-style: italic;\n"
"}")
        self.descBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.descBox.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.descBox)


        self.verticalLayout_6.addWidget(self.frame_8)

        self.installButton = QPushButton(self.boxContainer)
        self.installButton.setObjectName(u"installButton")
        self.installButton.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.installButton.sizePolicy().hasHeightForWidth())
        self.installButton.setSizePolicy(sizePolicy4)

        self.verticalLayout_6.addWidget(self.installButton, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.boxContainer, 0, Qt.AlignTop)

        self.BoxDownload = QFrame(self.bodyContents)
        self.BoxDownload.setObjectName(u"BoxDownload")
        self.BoxDownload.setMaximumSize(QSize(16777215, 50))
        self.BoxDownload.setFrameShape(QFrame.StyledPanel)
        self.BoxDownload.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.BoxDownload)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.progressBar = QProgressBar(self.BoxDownload)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy5)
        self.progressBar.setMaximumSize(QSize(16777215, 16777215))
        self.progressBar.setValue(24)

        self.verticalLayout_8.addWidget(self.progressBar, 0, Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.BoxDownload)


        self.horizontalLayout_9.addWidget(self.bodyContents)


        self.verticalLayout_10.addWidget(self.frame)


        self.verticalLayout.addWidget(self.main_body_contents)

        self.footer = QFrame(self.main_body)
        self.footer.setObjectName(u"footer")
        self.footer.setStyleSheet(u"background-color:rgb(9,5,13);")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.footer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.open_close_side_bar_btn = QPushButton(self.frame_7)
        self.open_close_side_bar_btn.setObjectName(u"open_close_side_bar_btn")
        icon3 = QIcon()
        icon3.addFile(u":/theme/icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.open_close_side_bar_btn.setIcon(icon3)

        self.verticalLayout_3.addWidget(self.open_close_side_bar_btn, 0, Qt.AlignLeft)


        self.horizontalLayout_8.addWidget(self.frame_7)


        self.horizontalLayout_3.addWidget(self.frame_6)

        self.frame_4 = QFrame(self.footer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.Back = QLabel(self.frame_4)
        self.Back.setObjectName(u"Back")

        self.horizontalLayout_10.addWidget(self.Back)


        self.horizontalLayout_3.addWidget(self.frame_4, 0, Qt.AlignRight)

        self.size_grip = QFrame(self.footer)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.size_grip, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.AppName.setText(QCoreApplication.translate("MainWindow", u"APPNAME", None))
#if QT_CONFIG(accessibility)
        self.System.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.installButton_0.setText(QCoreApplication.translate("MainWindow", u"Super Usuario", None))
        self.installButton_1.setText(QCoreApplication.translate("MainWindow", u"Partici\u00f3n", None))
        self.installButton_2.setText(QCoreApplication.translate("MainWindow", u"Idioma", None))
        self.installButton_3.setText(QCoreApplication.translate("MainWindow", u"Herramientas", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.System), QCoreApplication.translate("MainWindow", u"Sistema", None))
        self.unInstallButton_1.setText(QCoreApplication.translate("MainWindow", u"Proton Installer", None))
        self.unInstallButton_2.setText(QCoreApplication.translate("MainWindow", u"Software Adicional", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Steam Integration", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Software), QCoreApplication.translate("MainWindow", u"Software", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Pantalla", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Options), QCoreApplication.translate("MainWindow", u"Options", None))
        self.logoTitle.setText("")
        self.boxTitle.setText(QCoreApplication.translate("MainWindow", u"TWEAK - DECK", None))
        self.descTitle.setText(QCoreApplication.translate("MainWindow", u"Description:", None))
        self.descBox.setText("")
        self.installButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.open_close_side_bar_btn.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.Back.setText("")
    # retranslateUi

