from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless")  # Запуск в фоновом режиме
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Открываем сайт
url = "https://eco-c.ru/guides/emission"
driver.get(url)
# print(driver.text)
# Пример поиска элементов (замени на нужные селекторы)
elements = driver.find_elements(By.CSS_SELECTOR, 'div.dx-datagrid-text-content.dx-text-content-alignment-left.dx-header-filter-indicator')
print(elements)

for element in elements:
    print(element.text)

# Закрываем браузерз
driver.quit()
