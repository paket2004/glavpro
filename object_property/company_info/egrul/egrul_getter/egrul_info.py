# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# import os

# import time

# # Set the download directory
# download_dir = os.path.join(os.getcwd(), 'downloads')  # Save files in a 'downloads' folder
# if not os.path.exists(download_dir):
#     os.makedirs(download_dir)

# # Configure ChromeOptions
# chrome_options = webdriver.ChromeOptions()
# prefs = {
#     "download.default_directory": download_dir,  # Set the download directory
#     "download.prompt_for_download": False,       # Disable download prompt
#     "download.directory_upgrade": True,
#     "safebrowsing.enabled": True
# }
# chrome_options.add_experimental_option("prefs", prefs)

# # Initialize the Chrome browser with options
# browser = webdriver.Chrome(options=chrome_options)
# def get_statement(inn: str):
#     try:
#         # Open the target website
#         browser.get("https://egrul.nalog.ru/index.html")
            
#         # Wait until the input field is present in the DOM
#         inn_form = WebDriverWait(browser, 10).until(
#             EC.presence_of_element_located((By.ID, 'query'))
#         )
            
#         inn_form.send_keys(inn)
#         inn_form.send_keys(Keys.ENTER)
#         time.sleep(5)
#         content = WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located((By.CLASS_NAME, 'res-text'))
#         )
#         print("Result Text:", content.text)

#         download_button = WebDriverWait(browser, 10).until(
#             EC.element_to_be_clickable((By.CLASS_NAME, 'btn-with-icon.btn-excerpt.op-excerpt'))
#         )
            
#         download_button.click()
            
#         time.sleep(10)  # Adjust the sleep time based on the file size and network speed

#             # print(content)
            
#     finally:
#         browser.quit()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import time

def create_driver(download_dir):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # обязательно headless в облаке
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument(f"--user-data-dir=/tmp/user-data")  # временный профиль
    chrome_options.add_argument(f"--disable-extensions")
    
    # Для скачивания файлов
    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
    }
    chrome_options.add_experimental_option("prefs", prefs)

    # Явно указываем бинарник и chromedriver
    chrome_options.binary_location = "/usr/bin/chromium"
    driver = webdriver.Chrome(service=Service("/usr/bin/chromedriver"), options=chrome_options)
    return driver

def get_statement(inn: str):
    download_dir = os.path.join(os.getcwd(), 'downloads')
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    driver = create_driver(download_dir)
    try:
        driver.get("https://egrul.nalog.ru/index.html")

        inn_form = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'query'))
        )
        inn_form.send_keys(inn)
        inn_form.send_keys(Keys.ENTER)

        content = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'res-text'))
        )
        print("Result Text:", content.text)

        download_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'btn-with-icon.btn-excerpt.op-excerpt'))
        )
        download_button.click()

        # Ждем пока файл скачается
        time.sleep(10)

        # Можно попытаться проверить, что файл скачался, например:
        files = os.listdir(download_dir)
        print("Скачанные файлы:", files)

    finally:
        driver.quit()
