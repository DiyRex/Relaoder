import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import subprocess

def banner():
    banner = """

    ░█▀▀█ █▀▀ █── █▀▀█ █▀▀█ █▀▀▄ █▀▀ █▀▀█ 
    ░█▄▄▀ █▀▀ █── █──█ █▄▄█ █──█ █▀▀ █▄▄▀ 
    ░█─░█ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀──▀ ▀▀▀─ ▀▀▀ ▀─▀▀
                        -Script By DiyRex-
    """
    print(banner)

def start_chrome_debug_mode():
    print("Initiating Chrome Debug Session...")
    debug_port = "9222"
    user_data_dir = "C:/ChromeRefresher"
    if os.name == 'nt':  # Windows
        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([chrome_path, f"--remote-debugging-port={debug_port}", f"--user-data-dir={user_data_dir}"], shell=True)
    elif os.name == 'posix':  # macOS or Linux
        chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"  # macOS default path
        if not os.path.exists(chrome_path):
            chrome_path = "/usr/bin/google-chrome"  # Default Linux path
        subprocess.Popen([chrome_path, f"--remote-debugging-port={debug_port}", f"--user-data-dir={user_data_dir}"])
    else:
        print("Unsupported OS")

banner()
start_chrome_debug_mode()

time.sleep(2)

chrome_options = Options()
chrome_options.add_experimental_option('debuggerAddress', 'localhost:9222')
driver = webdriver.Chrome(options=chrome_options)

def refresh():
    driver.refresh()


