import json
import threading
import config

lock = threading.Lock()

def update_status(new_status: str):
    with lock:
        with open(config.system_config.HOME_DIR + 'statusProxy.json', 'r') as f:
            data = json.load(f)
        data['endstop_status'] = new_status
        with open(config.system_config.HOME_DIR + 'statusProxy.json', 'w') as f:
            json.dump(data, f)

def get_status() -> str:
    with lock:
        with open(config.system_config.HOME_DIR + 'statusProxy.json', 'r') as f:
            data = json.load(f)
    return data['endstop_status']

def set_printing_state(new_state: bool):
    with lock:
        with open(config.system_config.HOME_DIR + 'statusProxy.json', 'r') as f:
            data = json.load(f)
        data['set_print_status'] = new_state
        with open(config.system_config.HOME_DIR + 'statusProxy.json', 'w') as f:
            json.dump(data, f)

def get_printing_state() -> bool:
    with lock:
        with open(config.system_config.HOME_DIR + 'statusProxy.json', 'r') as f:
            data = json.load(f)
    return data['set_print_status']