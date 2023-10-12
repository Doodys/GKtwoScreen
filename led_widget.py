from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from rpi_ws281x import *
import config
import sys

strip = PixelStrip(config.leds_config.LED_COUNT, config.leds_config.LED_PIN, config.leds_config.LED_FREQ_HZ, config.leds_config.LED_DMA, config.leds_config.LED_INVERT, config.leds_config.LED_BRIGHTNESS, config.leds_config.LED_CHANNEL)
strip.begin()

def changeLedColor(color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(color[0], color[1], color[2]))
    strip.show()

class LedWidget(QWidget, QtWidgets.QSizePolicy):
    color_selected = pyqtSignal(tuple)

    def __init__(self, sizePolicy):
        super().__init__() 
        self.initUI(sizePolicy)

    def initUI(self, sizePolicy):

        self.setSizePolicy(sizePolicy)

        self.setMinimumSize(QtCore.QSize(0, 0))
        self.setBaseSize(QtCore.QSize(config.widget_config.WIDTH, config.widget_config.HEIGHT))
        self.setObjectName("led_widget")

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)

        self.led_label = QtWidgets.QLabel(self)
        self.led_label.setGeometry(QtCore.QRect(0, 0, (config.widget_config.WIDTH - 3), config.widget_config.STATUS_BAR_HEIGHT))
        self.led_label.setFont(font)
        self.led_label.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.led_label.setStyleSheet("background-color: rgb(34, 118, 181); color: black;")
        self.led_label.setScaledContents(True)
        self.led_label.setAlignment(QtCore.Qt.AlignCenter)
        self.led_label.setObjectName("led_label")

        self.blue = QtWidgets.QPushButton(self)
        self.blue.setGeometry(QtCore.QRect(20, 50, 131, 41))
        self.blue.setFont(font)
        self.blue.setStyleSheet("background-color: blue; color: black;")
        self.blue.setObjectName("blue")
        self.blue.clicked.connect(lambda: self.color_selected.emit((0, 0, 255)))

        self.red = QtWidgets.QPushButton(self)
        self.red.setGeometry(QtCore.QRect(170, 50, 131, 41))
        self.red.setFont(font)
        self.red.setStyleSheet("background-color: red; color: black;")
        self.red.setObjectName("red")
        self.red.clicked.connect(lambda: self.color_selected.emit((255, 0, 0)))

        self.green = QtWidgets.QPushButton(self)
        self.green.setGeometry(QtCore.QRect(320, 50, 131, 41))
        self.green.setFont(font)
        self.green.setStyleSheet("background-color: green; color: black;")
        self.green.setObjectName("green")
        self.green.clicked.connect(lambda: self.color_selected.emit((0, 255, 0)))

        self.yellow = QtWidgets.QPushButton(self)
        self.yellow.setGeometry(QtCore.QRect(320, 120, 131, 41))
        self.yellow.setFont(font)
        self.yellow.setStyleSheet("background-color: yellow; color: black;")
        self.yellow.setObjectName("yellow")
        self.yellow.clicked.connect(lambda: self.color_selected.emit((255, 255, 0)))

        self.magenta = QtWidgets.QPushButton(self)
        self.magenta.setGeometry(QtCore.QRect(170, 120, 131, 41))
        self.magenta.setFont(font)
        self.magenta.setStyleSheet("background-color: magenta; color: black;")
        self.magenta.setObjectName("magenta")
        self.magenta.clicked.connect(lambda: self.color_selected.emit((255, 0, 255)))

        self.cyan = QtWidgets.QPushButton(self)
        self.cyan.setGeometry(QtCore.QRect(20, 120, 131, 41))
        self.cyan.setFont(font)
        self.cyan.setStyleSheet("background-color: cyan; color: black;")
        self.cyan.setObjectName("cyan")
        self.cyan.clicked.connect(lambda: self.color_selected.emit((0, 255, 255)))

        self.off = QtWidgets.QPushButton(self)
        self.off.setGeometry(QtCore.QRect(320, 190, 131, 41))
        self.off.setStyleSheet("color: black;")
        self.off.setFont(font)
        self.off.setObjectName("off")
        self.off.clicked.connect(lambda: self.color_selected.emit((0, 0, 0)))

        self.white = QtWidgets.QPushButton(self)
        self.white.setGeometry(QtCore.QRect(170, 190, 131, 41))
        self.white.setFont(font)
        self.white.setStyleSheet("background-color: white; color: black;")
        self.white.setObjectName("white")
        self.white.clicked.connect(lambda: self.color_selected.emit((255, 255, 255)))

        self.orange = QtWidgets.QPushButton(self)
        self.orange.setGeometry(QtCore.QRect(20, 190, 131, 41))
        self.orange.setFont(font)
        self.orange.setStyleSheet("background-color: orange; color: black;")
        self.orange.setObjectName("orange")
        self.orange.clicked.connect(lambda: self.color_selected.emit((255, 165, 0)))

        self.color_selected.connect(changeLedColor)

class WebLedWidget():

    def __init__(self, color):
        super().__init__() 
        changeLedColor(strip, color)
        