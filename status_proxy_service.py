import json
import threading
import config
import logging
import os

logging.basicConfig(filename=config.system_config.HOME_DIR + 'app.log', level=logging.DEBUG)

lock = threading.Lock()
file_path = config.system_config.HOME_DIR + 'statusProxy.json'

default_data = {
        "endstop_status": "IDLE",
        "set_print_status": False
    }

def check_and_init_status_proxy():
    if os.path.exists(file_path):
        with open(file_path, 'r+') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:  # Handles empty or invalid JSON
                data = {}
            
            # Checking and setting default values if properties don't exist
            data.setdefault('endstop_status', default_data['endstop_status'])
            data.setdefault('set_print_status', default_data['set_print_status'])
            
            f.seek(0)  # Resets file position
            f.truncate()  # Clears the file
            json.dump(data, f)
    else:
        with open(file_path, 'w') as f:
            json.dump(default_data, f)

def update_status(new_status):
    with lock:
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