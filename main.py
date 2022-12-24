#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
APPNAME = "PROTONDECK"
VERSION = "0.0.7"
##  Author: Ainus64
##  gitlab: https://gitlab.com/misjuegosenlinux/ProtonDeck
################################################################################
#
# Dependencies
# pip install requests
#
################################################################################
##  IMPORT GUI FILE AND SYSTEM
#from re import X
#from turtle import width
from PySide2 import *
from ui_interface import * # Import GUI
from module_lib import * # Download Module
from listDB import *
from pathlib import Path
import sys
import os
import json
import wget
################################################################################

#################################################################################
## Variables and system folder 
#################################################################################
APP = APPNAME + " - " + VERSION
#button_start_install = "Start Install"
download_dir = "/mnt/Juegos/tmp/proton/"
install_dir = "/mnt/Juegos/tmp/installation/"
Download = False

# Check TMP Folder
Path(download_dir).mkdir(parents=True, exist_ok=True)


################################################################################
##  MAIN WINDOW CLASS
################################################################################

# Set protonge.download, protonge.install, protonge.uninstall
protonGE = protonClass()
#################################################################################

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #######################################################################
        ## # Remove window tittle bar
        ########################################################################    
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint) # uncomented only for Final Release 

        #######################################################################
        ## # Fix Menu position
        ########################################################################    
        self.ui.slide_menu_container.setMinimumSize(0, 0)
        self.ui.boxContainer.setMaximumHeight(0)
        self.ui.BoxDownload.setMaximumHeight(0)
        #################################################################################

        #######################################################################
        # Set window Icon   # This icon and title will not appear on our app main window because we removed the title bar
        #######################################################################
        self.setWindowIcon(QtGui.QIcon(":/theme/icons/app-icon.svg"))
        #################################################################################

        #################################################################################
        # Set window tittle
        #################################################################################
        self.setWindowTitle(APPNAME)
        self.ui.AppName.setText(APP)
        #################################################################################

        #################################################################################
        # Window Size grip to resize window
        #################################################################################
        QSizeGrip(self.ui.size_grip)
        #################################################################################

        #######################################################################
        # Menu button
        #######################################################################
        #print (list[0]) # uncomented only for TEST
        #print (ProtonDescription[list[0]]) # uncomented only for TEST

        self.ui.installButton_0.setText(list[0])
        self.ui.installButton_1.setText(list[1])
        self.ui.installButton_2.setText(list[2])
        self.ui.installButton_3.setText(list[3])
        self.ui.installButton_4.setText(list[4])
        self.ui.installButton_5.setText(list[5])
        self.ui.installButton_6.setText(list[6])
        self.ui.installButton_7.setText(list[7])
        self.ui.installButton_8.setText(list[8])
        self.ui.installButton_9.setText(list[9])

        self.ui.open_close_side_bar_btn.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.installButton_0.clicked.connect(lambda: self.selectInstall(list[0], ProtonDescription[list[0]]))
        self.ui.installButton_1.clicked.connect(lambda: self.selectInstall(list[1], ProtonDescription[list[1]]))
        self.ui.installButton_2.clicked.connect(lambda: self.selectInstall(list[2], ProtonDescription[list[2]]))
        self.ui.installButton_3.clicked.connect(lambda: self.selectInstall(list[3], ProtonDescription[list[3]]))
        self.ui.installButton_4.clicked.connect(lambda: self.selectInstall(list[4], ProtonDescription[list[4]]))
        self.ui.installButton_5.clicked.connect(lambda: self.selectInstall(list[5], ProtonDescription[list[5]]))
        self.ui.installButton_6.clicked.connect(lambda: self.selectInstall(list[6], ProtonDescription[list[6]]))
        self.ui.installButton_7.clicked.connect(lambda: self.selectInstall(list[7], ProtonDescription[list[7]]))
        self.ui.installButton_8.clicked.connect(lambda: self.selectInstall(list[8], ProtonDescription[list[8]]))
        self.ui.installButton_9.clicked.connect(lambda: self.selectInstall(list[9], ProtonDescription[list[9]]))
        #######################################################################  

        #######################################################################
        # Function to Move window on mouse drag event on the tittle bar
        #######################################################################
        def moveWindow(e):
            # Detect if the window is  normal size  
            if self.isMaximized() == False: #Not maximized
                # Move window only when window is normal size  
                # if left mouse button is clicked (Only accept left mouse button clicks)
                if e.buttons() == Qt.LeftButton:  
                    #Move window 
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        #######################################################################
        # Add click event/Mouse move event/drag event to the top header to move the window
        self.ui.header_frame.mouseMoveEvent = moveWindow
        #######################################################################
        
        self.show()

    #######################################################################
    # Add mouse events to the window
    #######################################################################
    def mousePressEvent(self, event):
        # Get the current position of the mouse
        self.clickPosition = event.globalPos()
        # We will use this value to move the window
    #######################################################################

    #######################################################################
    # EFFECT SLIDER MENU
    #######################################################################
    def slideLeftMenu(self):
        width = self.ui.slide_menu_container.width()
        # If Minimized
        if width == 0:
            # Expand Menu
            newWidth = 200
            self.ui.open_close_side_bar_btn.setStyleSheet("font-weight: bold")
        # If Maximized
        else:
            # Restore Menu
            newWidth = 0
            self.ui.open_close_side_bar_btn.setStyleSheet("font-weight: regular")
            # Fix Hide BoxContainer when menu botton is clicked
            self.ui.boxContainer.setMaximumHeight(0)
            self.ui.boxTitle.setText("PROTON INSTALLER")
            self.ui.descBox.setText("")
                    
        # Animation Effect Menu
        self.animation = QPropertyAnimation(self.ui.slide_menu_container, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
    #######################################################################

    #######################################################################
    # Step 1 - Select ProtonGE
    #######################################################################
    def selectInstall(self, ProtonGE_Release, desc):
        height = self.ui.boxContainer.height()
        self.ui.boxTitle.setText(ProtonGE_Release + " Installer")
        self.ui.installButton.setText("Start Install " + ProtonGE_Release)
        self.ui.installButton.clicked.connect(lambda: self.install_Proton(ProtonGE_Release, download_dir))
        self.ui.descBox.setText(desc)

        if height == 0:
            newHeight = 200
        else:
            newHeight = 200
            
        # Animation Effect
        self.animation = QPropertyAnimation(self.ui.boxContainer, b"maximumHeight")
        self.animation.setDuration(250)
        self.animation.setStartValue(height)
        self.animation.setEndValue(newHeight)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
    #######################################################################

    #######################################################################
    # Step 2 - Download And Install ProtonGE Process
    #######################################################################
    def install_Proton(self, ProtonGE_Release, download_dir):
        Download = True
        # protonGE.download(ProtonGE_Release, download_dir) # Download disabled only for TEST
    #######################################################################

################################################################################
##  EXECUTE APP
################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
################################################################################
##  END
################################################################################