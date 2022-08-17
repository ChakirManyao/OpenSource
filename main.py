from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Register.html")

# Заполнение всех полей
first_name = driver.find_element_by_xpath("//input[@placeholder='First Name']")
first_name.send_keys("John")
last_name = driver.find_element_by_xpath("//input[@placeholder='Last Name']")
last_name.send_keys("Snow")
email = driver.find_element_by_css_selector("#eid > input") # или //input[@ng-model="EmailAdress"]
email.send_keys("123@mail.ru")
phone = driver.find_element_by_css_selector("div:nth-child(4) > div > input") # или //input[@ng-model="Phone"]
phone.send_keys("1237777777") # номер телефона может отличаться
gender = driver.find_element_by_xpath("//input[@value='Male']")
gender.click()
# Заполнение селекторов country, date of birth
country = driver.find_element_by_id("countries")
select = Select(country)
select.select_by_value("Denmark")
date_of_birth_year = driver.find_element_by_id("yearbox")
select_year = Select(date_of_birth_year)
select_year.select_by_value("1990")
date_of_birth_month = driver.find_element_by_css_selector("div:nth-child(3) > select")
select_month = Select(date_of_birth_month)
select_month.select_by_value("January")
date_of_birth_day = driver.find_element_by_id("daybox")
select_day = Select(date_of_birth_day)
select_day.select_by_value("10")
# Заполнение пароля
password = driver.find_element_by_id("firstpassword")
password.send_keys("123456aA")
password_confirm = driver.find_element_by_id("secondpassword")
password_confirm.send_keys("123456aA")
# Загрузка файла
file = ("C:\doc.txt")
file_upload = driver.find_element_by_id("imagesrc")
file_upload.send_keys(file)
# Скролл страницы и подтверждение регистрации
driver.execute_script("window.scrollBy(0, 300);")
submit_btn = driver.find_element_by_id("submitbtn")
submit_btn.click()
# Проверка что что произошёл переход на ожидаемый адрес страницы
time.sleep(3)
current_page = driver.current_url
assert current_page == "http://demo.automationtesting.in/WebTable.html"
# Расширенная проверка адреса
expected_address = "http://demo.automationtesting.in/WebTable.html"
if current_page == "http://demo.automationtesting.in/WebTable.html": # или == expected_address
    print("Адрес страницы совпадает")
else:
    print("Аддрес не совпадает, фактический:", current_page)
    print("Ожидаемый:", expected_address)
time.sleep(5)
driver.quit()
