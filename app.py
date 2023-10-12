import sys
from PyQt5.QtWidgets import QApplication, QFrame
from PyQt5.QtCore import Qt
from rpi_ws281x import *
from PyQt5 import QtCore, QtGui, QtWidgets
import logging
import config
import resin_widget
import endstop_widget
import led_widget
import camera_widget
import status_proxy_service

logging.basicConfig(filename='app.log', level=logging.DEBUG)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # MainWindow setup
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(config.screen_config.WIDTH, config.screen_config.HEIGHT)
        MainWindow.setStyleSheet("background-color: rgb(79, 81, 107);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)

        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, config.screen_config.WIDTH, config.screen_config.HEIGHT))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, config.screen_config.WIDTH, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # endstop_widget
        self.endstop_widget_frame = QFrame()
        self.endstop_widget_frame.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        self.endstop_widget_frame.setStyleSheet("background-color: rgb(136, 139, 184);")

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.endstop_widget = endstop_widget.EndstopWidget(sizePolicy)
        sizePolicy.setHeightForWidth(self.endstop_widget.sizePolicy().hasHeightForWidth())

        self.endstop_widget.setEnabled(True)
        self.endstop_widget.setSizePolicy(sizePolicy)
        self.endstop_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.endstop_widget.setBaseSize(QtCore.QSize(config.widget_config.WIDTH, config.widget_config.HEIGHT))
        self.endstop_widget.setObjectName("endstop_widget")
        self.endstop_widget.setParent(self.endstop_widget_frame)

        self.gridLayout.addWidget(self.endstop_widget_frame, 0, 0, 1, 1)

        # led_widget
        self.led_widget_frame = QFrame()
        self.led_widget_frame.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        self.led_widget_frame.setStyleSheet("background-color: rgb(136, 139, 184);")

        self.led_widget = led_widget.LedWidget(sizePolicy)
        sizePolicy.setHeightForWidth(self.led_widget.sizePolicy().hasHeightForWidth())

        self.led_widget.setEnabled(True)
        self.led_widget.setSizePolicy(sizePolicy)
        self.led_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.led_widget.setBaseSize(QtCore.QSize(config.widget_config.WIDTH, config.widget_config.HEIGHT))
        self.led_widget.setObjectName("led_widget")
        self.led_widget.setParent(self.led_widget_frame)

        self.gridLayout.addWidget(self.led_widget_frame, 2, 0, 1, 1)

        # camera_widget
        self.camera_widget_frame = QFrame()
        self.camera_widget_frame.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        self.camera_widget_frame.setStyleSheet("background-color: rgb(136, 139, 184);")

        self.camera_widget = camera_widget.CameraWidget(sizePolicy)
        sizePolicy.setHeightForWidth(self.camera_widget.sizePolicy().hasHeightForWidth())

        self.camera_widget.setEnabled(True)
        self.camera_widget.setSizePolicy(sizePolicy)
        self.camera_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.camera_widget.setBaseSize(QtCore.QSize(config.widget_config.WIDTH, config.widget_config.HEIGHT))
        self.camera_widget.setObjectName("led_widget")
        self.camera_widget.setParent(self.camera_widget_frame)

        self.gridLayout.addWidget(self.camera_widget_frame, 0, 2, 1, 1)

        # resin_widget

        self.resin_widget_frame = QFrame()
        self.resin_widget_frame.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        self.resin_widget_frame.setStyleSheet("background-color: rgb(136, 139, 184);")

        self.resin_widget = resin_widget.ResinWidget(sizePolicy)
        sizePolicy.setHeightForWidth(self.resin_widget.sizePolicy().hasHeightForWidth())

        self.resin_widget.setEnabled(True)
        self.resin_widget.setSizePolicy(sizePolicy)
        self.resin_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.resin_widget.setBaseSize(QtCore.QSize(config.widget_config.WIDTH, config.widget_config.HEIGHT))
        self.resin_widget.setObjectName("led_widget")
        self.resin_widget.setParent(self.resin_widget_frame)

        self.gridLayout.addWidget(self.resin_widget_frame, 2, 2, 1, 1)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.resin_widget.label.setText(_translate("MainWindow", "RESIN STATUS"))
        self.endstop_widget.status_label.setText(_translate("MainWindow", "ENDSTOP STATUS"))
        self.endstop_widget.printStarted.setText(_translate("MainWindow", "Print Started/Set Idle"))
        self.camera_widget.camer_label.setText(_translate("MainWindow", "CAMERA"))
        self.camera_widget.camera_button.setText(_translate("MainWindow", "Toggle"))
        self.led_widget.led_label.setText(_translate("MainWindow", "LED STATE"))
        self.led_widget.blue.setText(_translate("MainWindow", "Blue"))
        self.led_widget.red.setText(_translate("MainWindow", "Red"))
        self.led_widget.green.setText(_translate("MainWindow", "Green"))
        self.led_widget.yellow.setText(_translate("MainWindow", "Yellow"))
        self.led_widget.magenta.setText(_translate("MainWindow", "Magenta"))
        self.led_widget.cyan.setText(_translate("MainWindow", "Cyan"))
        self.led_widget.off.setText(_translate("MainWindow", "Off"))
        self.led_widget.white.setText(_translate("MainWindow", "White"))
        self.led_widget.orange.setText(_translate("MainWindow", "Orange"))

if __name__ == '__main__':
    status_proxy_service.update_status('IDLE')
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    QApplication.setOverrideCursor(Qt.BlankCursor)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
