import json
import threading
import config
import logging

logging.basicConfig(filename=config.system_config.HOME_DIR + 'app.log', level=logging.DEBUG)

lock = threading.Lock()
file_path = config.system_config.HOME_DIR + 'statusProxy.json'

def update_status(new_status):
    with lock:
        logging.log(logging.INFO, f"File path: {file_path}")
        with open(file_path, 'r') as f:
            data = json.load(f)
        data['endstop_status'] = new_status
        with open(file_path, 'w') as f:
            json.dump(data, f)

def get_status():
    with lock:
        with open(file_path, 'r') as f:
            data = json.load(f)
    return data['endstop_status']

def set_printing_state(new_state):
    with lock:
        with open(file_path, 'r') as f:
            data = json.load(f)
        data['set_print_status'] = new_state
        with open(file_path, 'w') as f:
            json.dump(data, f)

def get_printing_state():
    with lock:
        with open(file_path, 'r') as f:
            data = json.load(f)
    return data['set_print_status']