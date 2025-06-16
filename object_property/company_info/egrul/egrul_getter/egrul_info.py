from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import time

def create_driver(download_dir):
    print("🔧 [1] Настраиваем драйвер...")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument("--user-data-dir=/tmp/user-data")

    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
    }
    chrome_options.add_experimental_option("prefs", prefs)

    # chrome_options.binary_location = "/usr/bin/chromium"

    print("🔄 Запускаем браузер...")
    # driver = webdriver.Chrome(service=Service("/usr/bin/chromedriver"), options=chrome_options)
    driver = webdriver.Chrome(options=chrome_options)
    print("✅ Драйвер готов")
    return driver

def get_statement(inn: str):
    print("📁 [2] Готовим папку загрузки...")
    download_dir = os.path.join(os.getcwd(), 'downloads')
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    print("🚀 [3] Запускаем Selenium")
    driver = create_driver(download_dir)
    try:
        print(f"🌐 [4] Открываем сайт ЕГРЮЛ...")
        driver.get("https://egrul.nalog.ru/index.html")

        print("⌛ [5] Ждём поле ввода ИНН...")
        inn_form = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'query'))
        )
        print("📝 Вводим ИНН:", inn)
        inn_form.send_keys(inn)
        inn_form.send_keys(Keys.ENTER)

        print("⌛ [6] Ждём результатов...")
        content = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'res-text'))
        )
        print("✅ Найден текст результата:", content.text)

        print("📥 [7] Ждём кнопку скачивания...")
        download_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'btn-with-icon.btn-excerpt.op-excerpt'))
        )
        print("👉 Нажимаем кнопку скачать...")
        download_button.click()

        print("⏳ [8] Ожидаем скачивание файла...")
        time.sleep(10)

        print("📂 [9] Список файлов в папке загрузки:")
        files = os.listdir(download_dir)
        for f in files:
            print(" -", f)

    except Exception as e:
        print("❌ Произошла ошибка:", str(e))
    finally:
        print("🧹 [10] Закрываем браузер")
        driver.quit()
