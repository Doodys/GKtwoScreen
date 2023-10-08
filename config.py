import configparser
from pathlib import Path
import os

class ScreenConfig:
    pass

class LedsConfig:
    pass

class CameraConfig:
    pass

class EndstopConfig:
    pass

class WidgetConfig:
    pass

thisfolder = os.path.dirname(os.path.abspath(__file__))
initfile = os.path.join(thisfolder, 'gktwoscreen.ini')
config = configparser.RawConfigParser()
config.read(initfile)

screen_config = ScreenConfig()
screen_config.WIDTH = config.getint('screen', 'WIDTH')
screen_config.HEIGHT = config.getint('screen', 'HEIGHT')

leds_config = LedsConfig()
leds_config.LED_COUNT = config.getint('leds', 'LED_COUNT')
leds_config.LED_PIN = config.getint('leds', 'LED_PIN')
leds_config.LED_FREQ_HZ = config.getint('leds', 'LED_FREQ_HZ')
leds_config.LED_DMA = config.getint('leds', 'LED_DMA')
leds_config.LED_BRIGHTNESS = config.getint('leds', 'LED_BRIGHTNESS')
leds_config.LED_INVERT = config.getboolean('leds', 'LED_INVERT')
leds_config.LED_CHANNEL = config.getint('leds', 'LED_CHANNEL')

camera_config = CameraConfig()
camera_config.PRESENT = config.getboolean('camera', 'PRESENT')
camera_config.RES_WIDTH = config.getint('camera', 'RES_WIDTH')
camera_config.RES_HEIGHT = config.getint('camera', 'RES_HEIGHT')

endstop_config = EndstopConfig()
endstop_config.PIN = config.getint('endstop', 'PIN')
endstop_config.PRINT_FINISHED_TIME = config.getint('endstop', 'PRINT_FINISHED_TIME')

widget_config = WidgetConfig()
widget_config.WIDTH = config.getint('widget', 'WIDTH')
widget_config.HEIGHT = config.getint('widget', 'HEIGHT')
widget_config.STATUS_BAR_HEIGHT = config.getint('widget', 'STATUS_BAR_HEIGHT')