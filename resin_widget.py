from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
import config

class ResinWidget(QWidget, QtWidgets.QSizePolicy):

    def __init__(self, sizePolicy):
        super().__init__() 
        self.initUI(sizePolicy)

    def initUI(self, sizePolicy):

        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(0, 0))
        self.setBaseSize(QtCore.QSize(config.widget_config.WIDTH, config.widget_config.HEIGHT))
        self.setObjectName("resin_widget")

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, 0, (config.widget_config.WIDTH - 3), config.widget_config.STATUS_BAR_HEIGHT))
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.label.setStyleSheet("background-color: rgb(34, 118, 181); color: black;")
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")