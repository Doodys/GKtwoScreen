from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
import config
import sys
import picamera

class CameraWidget(QWidget, QtWidgets.QSizePolicy):

    def __init__(self, sizePolicy):
        super().__init__()
        self.initUI(sizePolicy)
        self.is_previewing = False
        self.camera = picamera.PiCamera()

    def initUI(self, sizePolicy):
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(0, 0))
        self.setBaseSize(QtCore.QSize(config.widget_config.WIDTH, config.widget_config.HEIGHT))
        self.setObjectName("camera_widget")

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)

        self.camer_label = QtWidgets.QLabel(self)
        self.camer_label.setGeometry(QtCore.QRect(0, 0, (config.widget_config.WIDTH - 3), config.widget_config.STATUS_BAR_HEIGHT))
        self.camer_label.setFont(font)
        self.camer_label.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.camer_label.setStyleSheet("background-color: rgb(34, 118, 181); color: black;")
        self.camer_label.setScaledContents(True)
        self.camer_label.setAlignment(QtCore.Qt.AlignCenter)
        self.camer_label.setObjectName("camer_label")

        self.camera_button = QtWidgets.QPushButton(self)
        self.camera_button.setGeometry(QtCore.QRect(0, 0, 80, config.widget_config.STATUS_BAR_HEIGHT))
        self.camera_button.setFont(font)
        self.camera_button.setStyleSheet("color: black;")
        self.camera_button.setObjectName("camera_button")
        self.camera_button.clicked.connect(self.toggle_camera)

    def toggle_camera(self):
        if self.is_previewing:
            self.camera.stop_preview()
        else:
            self.camera.resolution = (config.camera_config.RES_WIDTH, config.camera_config.RES_HEIGHT)
            self.camera.start_preview(fullscreen=False, window=(315, 58, 900, 225))  # Adjusted to top-right corner with 20px margin
        self.is_previewing = not self.is_previewing