from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()

# Логин
driver.get("https://opensource-demo.orangehrmlive.com/")
login = driver.find_element_by_id("txtUsername")
login.send_keys("Admin")
password = driver.find_element_by_id("txtPassword")
password.send_keys("admin123")
login_btn = driver.find_element_by_id("btnLogin")
login_btn.click()
# Переход в PIM в карточку пользователя
Pim = driver.find_element_by_id('menu_pim_viewPimModule')
Pim.click()
time.sleep(3)
employee_peter = driver.find_element_by_link_text("Peter Mac")
employee_peter.click()
time.sleep(1)
# Проверка недоступности радиокнопки 
gender_male = driver.find_element_by_id("personal_optGender_2")
gender_male_disabled = gender_male.get_attribute("disabled")
if gender_male_disabled is not None:
    print("Селектор недоступен для выбора")
else:
    print("Селектор доступен для выбора")
# Проверка недоступности селектора
nationality_selector = driver.find_element_by_id("personal_cmbNation")
nationality_selector_disabled = nationality_selector.get_attribute("disabled")
if nationality_selector_disabled is not None:
    print("Селектор недоступен для выбора")
else:
    print("Селектор доступен для выбора")
# Режим редактирования пользователя
save_edit_btn = driver.find_element_by_id("btnSave")
save_edit_btn.click()
# Выбор и проверка радиокнопки противоположного пола
gender_male.click()
gender_male_checked = gender_male.get_attribute("checked")
if gender_male_checked is not None:
    print("Чекбокс отмечен")
else:
    print("Чекбокс НЕ отмечен")
# Выбор и проверка (самая последняя страна)
select = Select(nationality_selector)
select.select_by_value("193")
nationality_selector_zimbabwean = nationality_selector.get_attribute("value")
if nationality_selector_zimbabwean == "193":
    print("Выбрана последняя страна в списке")
else:
    print("Выбрана НЕ последняя страна в списке")
# Возвращаем изменения и сохраненяем
gender_female = driver.find_element_by_id("personal_optGender_1")
gender_female.click()
select.select_by_value("0")
save_edit_btn.click()
driver.quit()