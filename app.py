import time
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyautogui
import pyperclip
from tqdm import tqdm

options = Options()
options.add_experimental_option("detach", False)
driver = webdriver.Chrome(options=options)
driver.set_window_size(600, 400)

actions = ActionChains(driver)

def wait(before):
    while 1:
        if before != driver.execute_script("return document.getElementsByClassName('CodeMirror-code')[0].innerHTML"):
            break
        else:
            time.sleep(.5)

def init_driver():
    driver.get("https://php-minify.com/php-obfuscator/index.php")
    time.sleep(1)

def encript(code):
    pyautogui.hotkey('ctrl','a')
    time.sleep(0.15)
    # actions.send_keys(code).perform()
    pyperclip.copy(code)
    time.sleep(0.15)
    pyautogui.hotkey('ctrl','v')
    time.sleep(0.15)

    driver.execute_script("input_minify.click()")
    wait(driver.execute_script("return document.getElementsByClassName('CodeMirror-code')[0].innerHTML"))
    time.sleep(0.15)
    pyautogui.hotkey('ctrl','a')
    time.sleep(0.15)
    pyautogui.hotkey('ctrl','c')
    time.sleep(0.15)

def list_files(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def get_files(arg):
    directory_path = f'.\\application\\{arg}\\'
    files = list_files(directory_path)
    output = []
    for file in files:
            if('.php' in file):
                output.append(file)
    return output

def execute(files):
    for file in tqdm(files):
        path = f'.\\encrypted\\{file[14:]}'
        os.makedirs(os.path.dirname(path), exist_ok=True)
        try:
            f = open(path, "x")
        except:
            pass
        with open(file) as f: s = f.read()
        encript(s)
        f = open(path, "w")
        f.write(pyperclip.paste())
        f.close()

def main():
    print('initiating')
    init_driver()
    print('tools loaded')
    execute(get_files('models'))
    execute(get_files('controllers'))
    
if __name__ == '__main__':
    main()