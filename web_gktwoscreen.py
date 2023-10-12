from flask import Flask, render_template
from flask_socketio import SocketIO
import config
import led_widget
import logging
import app
import status_proxy_service

logging.basicConfig(filename=config.system_config.HOME_DIR + 'app.log', level=logging.DEBUG)
last_status: str = None

appFlask = Flask(__name__)
socketio = SocketIO(appFlask, cors_allowed_origins="*")

@appFlask.route('/')
def index():
    return render_template('index.html')

@appFlask.route('/trigger_blue')
def trigger_blue():
    led_widget.changeLedColor((0, 0, 255))
    return '', 200

@appFlask.route('/trigger_red')
def trigger_red():
    led_widget.changeLedColor((255, 0, 0))
    return '', 200

@appFlask.route('/trigger_green')
def trigger_green():
    led_widget.changeLedColor((0, 255, 0))
    return '', 200

@appFlask.route('/trigger_cyan')
def trigger_cyan():
    led_widget.changeLedColor((0, 255, 255))
    return '', 200

@appFlask.route('/trigger_magenta')
def trigger_magenta():
    led_widget.changeLedColor((255, 0, 255))
    return '', 200

@appFlask.route('/trigger_yellow')
def trigger_yellow():
    led_widget.changeLedColor((255, 255, 0))
    return '', 200

@appFlask.route('/trigger_orange')
def trigger_orange():
    led_widget.changeLedColor((255, 165, 0))
    return '', 200

@appFlask.route('/trigger_white')
def trigger_white():
    led_widget.changeLedColor((255, 255, 255))
    return '', 200

@appFlask.route('/trigger_off')
def trigger_off():
    led_widget.changeLedColor((0, 0, 0))
    return '', 200

@appFlask.route('/toggle_print_status')
def toggle_print_status():
    status_proxy_service.set_printing_state(True)
    return '', 200

@socketio.on('connect_to_host')
def connect():
    logging.log(logging.INFO, 'Connected')
    socketio.send("Connected")

@socketio.on('request_status')
def update_status():
    global last_status
    status = status_proxy_service.get_status()

    if last_status != status:
        last_status = status
        socketio.emit('update_visibility', {'status': status})

if __name__ == '__main__':
    socketio.run(appFlask, host=config.system_config.LOCAL_IP, port=5000, allow_unsafe_werkzeug=True)