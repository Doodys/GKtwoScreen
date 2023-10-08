from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QTimer
import RPi.GPIO as GPIO
import config

class EndstopWidget(QWidget, QtWidgets.QSizePolicy):

    def __init__(self, sizePolicy):
        super().__init__()
        self.is_printing = False
        self.finished = False
        self.true_time = 0
        self.initUI(sizePolicy)

    def initUI(self, sizePolicy):

        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(0, 0))
        self.setBaseSize(QtCore.QSize(config.widget_config.WIDTH, config.widget_config.HEIGHT))
        self.setObjectName("status_widget")

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)

        self.status_label = QtWidgets.QLabel(self)
        self.status_label.setGeometry(QtCore.QRect(0, 0, (config.widget_config.WIDTH - 3), config.widget_config.STATUS_BAR_HEIGHT))
        self.status_label.setFont(font)
        self.status_label.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.status_label.setStyleSheet("background-color: rgb(34, 118, 181); color: black;")
        self.status_label.setScaledContents(True)
        self.status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.status_label.setEnabled(True)
        self.status_label.setObjectName("status_label")

        self.endstop_label = QtWidgets.QLabel(self)
        self.endstop_label.setEnabled(True)
        self.endstop_label.setGeometry(QtCore.QRect(30, 70, 421, config.widget_config.STATUS_BAR_HEIGHT))
        self.endstop_label.setFont(font)
        self.endstop_label.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.endstop_label.setStyleSheet("background-color: rgb(219,50, 80); color: black;")
        self.endstop_label.setText('IDLE')
        self.endstop_label.setScaledContents(True)
        self.endstop_label.setAlignment(QtCore.Qt.AlignCenter)
        self.endstop_label.setObjectName("endstop_label")

        self.printStarted = QtWidgets.QPushButton(self)
        self.printStarted.setGeometry(QtCore.QRect(145, 150, 200, 61))
        self.printStarted.setEnabled(True)
        self.printStarted.setFont(font)
        self.printStarted.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.printStarted.setStyleSheet("background-color: rgb(138, 110, 230); color: black;")
        self.printStarted.setObjectName("print_started")
        self.printStarted.clicked.connect(self.set_print_status)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_status)
        self.timer.start(100)  # update every 100 ms

        self.timerPrinting = QTimer()
        self.timerPrinting.timeout.connect(self.check_if_finished)
        self.timerPrinting.start(1000)  # update every 1 s

    def update_status(self):
        if not self.is_printing and self.finished:
            self.endstop_label.setText('FINISHED')
            self.endstop_label.setStyleSheet("background-color: green")
        elif not self.is_printing:
            self.endstop_label.setText('IDLE')
            self.endstop_label.setStyleSheet("background-color: rgb(219,50, 80);")

    def set_print_status(self):
        if not self.is_printing and not self.finished:
            self.endstop_label.setText('PRINTING...')
            self.endstop_label.setStyleSheet("background-color: blue")
            self.finished = False
        else:
            self.endstop_label.setText('IDLE')
            self.endstop_label.setStyleSheet("background-color: rgb(219,50, 80);")
            self.finished = False
        self.is_printing = not self.is_printing

    def check_if_finished(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(config.endstop_config.PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        if not GPIO.input(config.endstop_config.PIN) and self.is_printing:
            self.true_time += 1

            if self.true_time >= config.endstop_config.PRINT_FINISHED_TIME:
                self.endstop_label.setText('FINISHED')
                self.endstop_label.setStyleSheet("background-color: green")
                self.true_time = 0
                self.finished = True
                self.is_printing = False
            else:
                self.finished = False
