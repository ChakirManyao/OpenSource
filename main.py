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
# Переход в PIM -> Employee List - > карточка пользователя
pim = driver.find_element_by_id('menu_pim_viewPimModule')
pim.click()
time.sleep(3)
employee_linda = driver.find_element_by_link_text("Linda Jane")
employee_linda.click()
time.sleep(1)
# Проверка недоступности радиокнопки противоположного пола сотрудника
gender_male = driver.find_element_by_id("personal_optGender_1")
gender_male_disabled = gender_male.get_attribute("disabled")
if gender_male_disabled is not None:
print("Селектор недоступен для выбора")
else:
print("Селектор доступен для выбора")
# Проверка недоступности селектора nationality сотрудника
nationality_selector = driver.find_element_by_id("personal_cmbNation")
nationality_selector_disabled = nationality_selector.get_attribute("disabled")
if nationality_selector_disabled is not None:
print("Селектор недоступен для выбора")
else:
print("Селектор доступен для выбора")
# Переход в режим редактирования пользователя
save_edit_btn = driver.find_element_by_id("btnSave")
save_edit_btn.click()
# Выбор и проверка что выбрана радиокнопка противоположного пола
gender_male.click()
gender_male_checked = gender_male.get_attribute("checked")
if gender_male_checked is not None:
print("Чекбокс отмечен")
else:
print("Чекбокс НЕ отмечен")
# Выбор и проверка что в селекторе nationality выбрана самая последняя страна
select = Select(nationality_selector)
select.select_by_value("193")
nationality_selector_zimbabwean = nationality_selector.get_attribute("value")
if nationality_selector_zimbabwean == "193":
print("Выбрана последняя страна в списке")
else:
print("Выбрана НЕ последняя страна в списке")
# Возврат изменений и сохранение
gender_female = driver.find_element_by_id("personal_optGender_2")
gender_female.click()
select.select_by_value("0")
save_edit_btn.click()
driver.quit()


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
select.select_by_value("United Kingdom")
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

driver.quit()

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://demo.automationtesting.in/WebTable.html")

# Переход на вкладку SwitchTo -> Alerts
switch_to = driver.find_element_by_link_text("SwitchTo")
switch_to.click()
switch_to_alerts = driver.find_element_by_link_text("Alerts")
switch_to_alerts.click()
time.sleep(3)
alert_display_box_btn = driver.find_element_by_css_selector("#OKTab > button")
alert_display_box_btn.click()
# Подтверждение и проверка текста окна alert
alert = driver.switch_to.alert
alert_expected_text = "I am an alert box!"
alert_text = alert.text
# Расширенная проверка содержимого текста в окне alert
if alert_text == alert_expected_text:
print("Текст совпадает:", alert_text)
else:
print("Фактический текст:", alert_text)
print("Ожидаемый текст:", alert_expected_text)
alert.accept()
# Получение адреса текущей ссылки
current_url = driver.current_url
time.sleep(3)
second_tab = driver.execute_script("window.open();")
window_after_first = driver.window_handles[1]
driver.switch_to.window(window_after_first)
driver.get(current_url)
time.sleep(3)
# Подтверждение и проверка текста окна alert with ok & cancel
alert_with_ok_cancel = driver.find_element_by_css_selector(".nav-tabs > li:nth-child(2)")
alert_with_ok_cancel.click()
display_confirm_box_btn = driver.find_element_by_css_selector("#CancelTab > button")
display_confirm_box_btn.click()
confirm = driver.switch_to.alert
confirm.dismiss()
time.sleep(3)
# Подтверждение и проверка текста окна alert with textbox
third_tab = driver.execute_script("window.open();")
window_after_second = driver.window_handles[2]
driver.switch_to.window(window_after_second)
driver.get(current_url)
time.sleep(3)
alert_with_textbox_btn = driver.find_element_by_css_selector(".nav-tabs > li:nth-child(3)")
alert_with_textbox_btn.click()
display_promt_box_btn = driver.find_element_by_css_selector("#Textbox > button")
display_promt_box_btn.click()
prompt = driver.switch_to.alert
prompt.send_keys("Ура! Задание выполнено!")
prompt.accept()

driver.quit()


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://demo.automationtesting.in/WebTable.html")

# Переход в раздел More -> Loader
more = driver.find_element_by_link_text("More")
more.click()
more_loader = driver.find_element_by_link_text("Loader")
more_loader.click()

# Реализация неявных ожиданий
run_btn = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.ID, "loader")) # css_selector: .panel-default > div > button
)
run_btn.click()

lorem_text = WebDriverWait(driver, 20).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".modal-body > p"), "Lorem"))

save_changes_btn = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-footer .btn-primary"))
)
save_changes_btn.click()

driver.quit()


from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://demo.automationtesting.in/WebTable.html")

# Переход в раздел More -> Dynamic Data
more = driver.find_element_by_link_text("More")
more.click()
more_dynamic_data = driver.find_element_by_link_text("Dynamic Data")
more_dynamic_data.click()
# Проверка, что заголовок окна равен "Loading the data Dynamically"
window_title = driver.find_element_by_tag_name("h3")
window_title_text = window_title.text
assert window_title_text == "Loading the data Dynamically"
get_dynamic_data_btn = driver.find_element_by_id("save")
get_dynamic_data_btn.click()
time.sleep(3)
# Вывод ссылки на сгенерированную картинку
get_src = driver.find_element_by_css_selector("#loading > img")
get_src_value = get_src.get_attribute("src")
print(get_src_value)

driver.quit()


from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://demo.automationtesting.in/WebTable.html")

# Переход в раздел More -> File Upload
more = driver.find_element_by_link_text("More")
more.click()
more_loading_file_upload = driver.find_element_by_link_text("File Upload")
more_loading_file_upload.click()
file_picture = ("C:\picture.jpg")
browse_btn = driver.find_element_by_id("input-4")
browse_btn.send_keys(file_picture)
remove_tbn = driver.find_element_by_class_name("glyphicon-trash")
remove_tbn.click()
file_txt = ("C:\doc.txt")
browse_btn.send_keys(file_txt)
close_alert_message = driver.find_element_by_class_name("kv-error-close")
close_alert_message.click()
upload_btn = driver.find_element_by_css_selector(".file-input .fileinput-upload")
upload_btn_disabled = upload_btn.get_attribute("disabled")
if upload_btn_disabled is not None:
print("Кнопка заблокирована")
else:
print("Кнопка доступна для нажатия")

driver.quit()



from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://demo.automationtesting.in/WebTable.html")

# Переход в раздел More -> JQuery ProgressBar
more = driver.find_element_by_link_text("More")
more.click()
more_loading_file_upload = driver.find_element_by_link_text("JQuery ProgressBar")
more_loading_file_upload.click()
# Проверка что кнопка close невидима
progress_bar = WebDriverWait(driver, 10).until(
EC.invisibility_of_element_located((By.CSS_SELECTOR, ".ui-dialog-buttonset > button")))
# Открытие окна загрузки
start_download = driver.find_element_by_id("downloadButton")
start_download.click()
# Проверка названия кнопки
close_btn_text = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".ui-dialog-buttonset > button"), "Cancel Download"))
# Закрытие - > открытие окна загрузки
close_btn = driver.find_element_by_css_selector(".ui-dialog-buttonset > button")
close_btn.click()
start_download.click()
# Проверка финального текста
window_text = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".progress-label"), "Complete!"))

driver.quit()



from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10) # вынесли повторяющуюся часть в переменную wait
driver.get("http://demo.automationtesting.in/WebTable.html")

# Переход в раздел SwitchTo -> Windows
switch_to = driver.find_element_by_link_text("SwitchTo")
switch_to.click()
switch_to_windows = driver.find_element_by_link_text("Windows")
switch_to_windows.click()
# Открытие нового окна
first_browser_tab = driver.current_window_handle
open_new_run_btn = driver.find_element_by_css_selector(".active .btn")
open_new_run_btn.click()
# Переключение на второе окно > его закрытие - > переключение обратно на первое окно
second_browser_tab = driver.window_handles[1]
driver.switch_to.window(second_browser_tab)
driver.close() # закрытие вкладки
driver.switch_to.window(first_browser_tab)
# Открытие Separate Multiple Windows - > click
open_separate_multiple_tab = driver.find_element_by_css_selector("li:nth-child(3) > a.analystic")
open_separate_multiple_tab.click()
open_separate_multiple_run_btn = driver.find_element_by_css_selector("#Multiple > button")
open_separate_multiple_run_btn.click()
# Переключение на второе окно. Проверка что адрес страницы верный и что в браузере открыто 3 вкладки
driver.switch_to.window(driver.window_handles[2]) # цифра 2(а не 1), тк до этого закрывали вкладку и она есть в памяти
link_check = wait.until(EC.url_to_be("http://demo.automationtesting.in/Index.html"))
number_of_tabs = wait.until(EC.number_of_windows_to_be(3)) # кавычки для цифры не нужны
print(number_of_tabs)
# Ввод email и проверка что адрес финальной страницы верный
email = driver.find_element_by_id("email")
email.send_keys("email@mail.ru")
send_btn = driver.find_element_by_id("enterimg")
send_btn.click()
final_link_check = wait.until(EC.url_to_be("http://demo.automationtesting.in/Register.html"))

driver.quit()
