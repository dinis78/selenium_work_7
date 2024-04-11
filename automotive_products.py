from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Установка пути до chromedriver
webdriver_service = Service('path_to_chromedriver')

# Опции браузера Chrome
options = Options()
options.add_argument("--headless") # Запустить браузер в фоновом режиме

# Создание экземпляра драйвера
driver = webdriver.Chrome(service=webdriver_service, options=options)

# URL сайта esd-avto.ru
url = "https://www.esd-avto.ru/"

# Переход на нужную страницу сайта
driver.get(url)
# Например, переходим на страницу с каталогом автоаксессуаров
driver.find_element(By.LINK_TEXT, "Каталог").click()
driver.find_element(By.LINK_TEXT, "Автоаксессуары").click()

# Ожидание загрузки страницы
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "products")))

# Используем BeautifulSoup для парсинга HTML
soup = BeautifulSoup(driver.page_source, "html.parser")

# Извлечение информации о продуктах
products = soup.find_all("div", class_="product-item")

# Создаем список для сохранения данных
data = []

# Извлекаем название и цену продуктов
for product in products:
    name = product.find("div", class_="name").text.strip()
    price = product.find("span", class_="price").text.strip()
    data.append({"name": name, "price": price})

# Вывод данных
for item in data:
    print("Название: " + item["name"])
    print("Цена: " + item["price"])
    print("")

# Закрытие браузера
driver.quit()
