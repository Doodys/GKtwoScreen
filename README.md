# About

Management app for GKtwo 3D resin printer addons (or basically any 3D printer). I've created it just for fun to have some on-screen functions for my addons like endstop detecting finished print, WS2812x LEDs, camera preview and, in the future, auto resin refill system. It is build with PyQt5.

# Hardware used

- Raspberry Pi Zero W
- Wavechare 11303 7" 1024x600 touchscreen
- WK625 endstop switch
- WS2812 LED RGB ring 66mm diameter
- OdSeven Camera HD OV5647 5Mpx (Raspberry Pi Camera Rev 1.3)
- microSD card (32GB should be more than enough)
- some wires
- not necessary - Argon POD as rpi case (it can make wifi connection weaker, I had to use additional antenna)

# Initial preparations

You'll have to install some lightweight non-desktop system like Raspbian OS Lite (non desktop) and be able to SSH to it. If you'd like to do any development I highly recommend installing on your PC Visual Studio Code for Python development and WinSCP for faster file management.

Quality of life thing to start with - set static IP for your RPI:

```
sudo nano /etc/dhcpcd.conf

Add (your value instead of X):

interface eth0
static ip_address=192.168.1.X/24
static routers=192.168.1.1
static domain_name_servers=192.168.1.1

interface wlan0
static ip_address=192.168.0.X/24
static routers=192.168.1.1
static domain_name_servers=192.168.1.1
```

Enable camera:

```
sudo raspi-config
Interface Options -> Legacy Camera
sudo reboot
```

For Waveshare 11303 preparation follow: https://www.waveshare.com/wiki/7inch_HDMI_LCD_%28C%29
For any other screen follow your own documentation. **Screen should be 1024x600, there can be some graphical bugs with any other screen size**.

Clone repository:

```
git clone https://github.com/Doodys/GKtwoScreen
```

Prepare service:

```
sudo apt-get update
sudo apt-get install libmtdev1
sudo nano /etc/systemd/system/app.service
```

Fill `app.service` with:

```
[Unit]
Description=GKtwoScreen

[Service]
ExecStart=/bin/bash -c "exec /usr/bin/startx /usr/bin/python3 /home/pi/GKtwoScreen/app.py"
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```

Install PyQt5:

```
sudo apt-get install python3-pyqt5
```

Install XServer to run service on raspberry pi:

```
sudo apt-get install xserver-xorg xinit
```

Open Xwrapper.config:

```
sudo nano /etc/X11/Xwrapper.config
```

Paste in there values:

```
needs_root_rights=yes
allowed_users=anybody
```

Install any missing python3 libraries like:

```
sudo pip3 install rpi_ws281x
sudo pip3 install RPi.GPIO
```

Reload daemon and service:

```
sudo systemctl daemon-reload
sudo systemctl restart app.service
```

# Ini file

I've tried to make my app configurable, like using `printer.cfg` in `Klipper`. There's file called `gktwoscreen.ini` containing whole app configuration. **Every section is needed**. My example:

```
[screen]
WIDTH = 1024
HEIGHT = 600

[leds]
LED_COUNT = 24
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0

[camera]
PRESENT = True
RES_WIDTH = 1024
RES_HEIGHT = 600

[endstop]
PIN = 17
PRINT_FINISHED_TIME = 3

[widget]
WIDTH = 482
HEIGHT = 245
STATUS_BAR_HEIGHT = 35
```

- In `screen` you can setup your screen resolution.
- In `leds` stick with the example values, just edit `LED_COUNT` and `LED_PIN` according to your setup.
- In `camera` you can setup camera resolution and flag if camera is even present in your setup. `PRESENT` **does not work for now**.
- In `endstop` you can change `PIN` where switch is connected and timeout after which status will be changed from `PRINTING` to `FINISHED` (just to make sure that endstop is not triggered because of retraction during very high prints and not buildplate going to max Z position after finished printing).
- In `widget` you can play with UI. If your screen is something else than 1024x600 you can try to adjust those values to your needs. Widget is every one of the four parts in the UI. `WIDTH` and `HEIGHT` are widget's main size values and `STATUS_BAR_HEIGHT` is widget's title label height.





