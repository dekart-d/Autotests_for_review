#Сами тесты
import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import get_screen
import pytest
import requests
from data.data_tests_form_abLocal2 import ValueGenerator
from data.clear_validate import clear_validate
import bs4
import lxml
from db import DbConnection


# Метод получение session ID из local storage, по которому мы будем находить данные в бд нашей сессии
def get_sid(app):
    driver = app.driver
    localstorage = driver.execute_script("return window.localStorage;")
    return_sid = localstorage["sID"].replace('"', "")
    return return_sid


generator = ValueGenerator()

#удалил значения кредов от БД
db_connection = DbConnection(
    dbname='dbname',
    user="user",
    password="password",
    host="host",
    port="5432",
)


# 1step form
def test_db_connect(app):
    db_connection.connect()


def test_enter_lastname(app):
    app.open_form(url='ссылка на проект')
    driver = app.driver
    search_element = driver.find_element(By.NAME, 'lastname')
    search_element.send_keys(generator.get_last_name())
    search_element_text = driver.find_element(By.CSS_SELECTOR, '#field-lastname').get_attribute('value')

    assert search_element_text == generator.get_last_name()


def test_enter_firstname(app):
    driver = app.driver
    search_element = driver.find_element(By.NAME, 'firstname')
    search_element.send_keys(generator.get_first_name())
    search_element_text = driver.find_element(By.CSS_SELECTOR, '#field-firstname').get_attribute('value')

    assert search_element_text == generator.get_first_name()


def test_enter_middlename(app):
    driver = app.driver
    search_element = driver.find_element(By.NAME, 'middlename')
    search_element.send_keys(generator.get_middle_name())
    search_element_text = driver.find_element(By.CSS_SELECTOR, '#field-middlename').get_attribute('value')

    assert search_element_text == generator.get_middle_name()


def test_enter_phone(app):
    driver = app.driver
    search_element = driver.find_element(By.NAME, 'phone')
    search_element.send_keys(generator.get_phone())
    search_element_text = driver.find_element(By.CSS_SELECTOR, '#field-phone').get_attribute('value')

    assert clear_validate(search_element_text) == generator.get_phone()


def test_click_phone_button(app):
    driver = app.driver
    search_element = driver.find_element(By.CLASS_NAME, 'confirm-box-btn')
    search_element.click()


def test_enter_sms_code(app):
    driver = app.driver
    search_element = driver.find_element(By.NAME, 'smsCode')
    search_element.send_keys(generator.get_sms_code())
    # if error 500
    #
    # alert_HTML_all = driver.execute_script('return document.body.innerHTML')
    # HTML_parser = bs4.BeautifulSoup(alert_HTML_all, "lxml")
    # alert_p = HTML_parser.find_all("p", attrs={'class': 'error form-message'})
    #
    # if alert_p:
    #     driver.save_screenshot(fr'{get_screen.path}{get_screen.generate_name_screen()}')
    #     pytest.exit("ERROR CODE 500 sms_code")


def test_enter_email(app):
    driver = app.driver
    search_element = driver.find_element(By.NAME, 'email')
    search_element.send_keys(generator.get_email())
    search_element.send_keys(Keys.ARROW_DOWN)
    search_element.send_keys(Keys.ENTER)
    search_element_text = driver.find_element(By.CSS_SELECTOR, '#field-email').get_attribute('value')
    assert search_element_text == generator.get_email()


def test_choose_checkbox(app):
    driver = app.driver
    search_element = driver.find_element(By.CLASS_NAME, 'field-first-multi-checkbox')
    search_element.click()


def test_go_to_page2(app):
    driver = app.driver
    driver.save_screenshot(fr'{get_screen.path}{get_screen.generate_name_screen()}')
    search_element = driver.find_element(By.XPATH,
                                         '//*[@id="root"]/main/div[2]/div/div[2]/div[1]/div/form/div[2]/div[1]/button')
    search_element.click()
    time.sleep(1.5)
    string_url = driver.current_url
    # Получаю ссылку текущей страницы и реплейсом удаляю домен и гет параметры,
    # так как при переходе на другие шаги анкеты у нас в ссылке указывается шаг в гет параметре
    step = string_url.replace('домен', '').replace('гет параметр', '')
    assert step == 'step/1'


def test_check_status_code_page_2(app):
    driver = app.driver
    string_url = driver.current_url
    response = requests.get(f'{string_url}')
    assert response.status_code == 200


def test_sid(app):
    record_with_sid = db_connection.find_sid_db(get_sid(app))

    assert record_with_sid


def test_lastname_db(app):
    record_with_lastname = db_connection.find_lastname(get_sid(app))

    assert record_with_lastname == generator.get_last_name()


def test_firstname_db(app):
    record_with_firstname = db_connection.find_firstname(get_sid(app))

    assert record_with_firstname == generator.get_first_name()


def test_middlename_db(app):
    record_with_middlename = db_connection.find_middlename(get_sid(app))

    assert record_with_middlename == generator.get_middle_name()


def test_phone_db(app):
    record_with_phone = db_connection.find_phone(get_sid(app))

    assert record_with_phone == generator.get_phone()


def test_email_db(app):
    record_with_email = db_connection.find_email(get_sid(app))

    assert record_with_email == generator.get_email()


# End 1 step form


# Start 2step form

def test_enter_birht_date(app):
    driver = app.driver
    search_element = driver.find_element(By.NAME, 'birthDate')
    search_element.send_keys(generator.get_birth_date())
    search_element_text = driver.find_element(By.CSS_SELECTOR, '#field-birthDate').get_attribute('value')
    assert search_element_text == generator.get_birth_date()


def test_choose_sex(app):
    driver = app.driver
    search_element = driver.find_element(By.XPATH,
                                         '//*[@id="root"]/main/div[2]/div/div[2]/div/div/form/div[1]/div[2]/div/div[2]/div/div[1]/div/label')
    search_element.click()
    assert search_element.text == 'Мужской'


def test_enter_birht_place(app):
    driver = app.driver
    search_element = driver.find_element(By.NAME, 'birthPlace')
    search_element.send_keys(generator.get_birth_place())

    search_element_text = driver.find_element(By.CSS_SELECTOR, '#field-birthPlace').get_attribute('value')
    assert search_element_text == generator.get_birth_place()


def test_enter_passport(app):
    driver = app.driver
    search_element = driver.find_element(By.NAME, 'passport')
    search_element.send_keys(generator.get_passport())
    search_element_text = driver.find_element(By.CSS_SELECTOR, '#field-passport').get_attribute('value')
    assert search_element_text == generator.get_passport()


def test_enter_passport_code(app):
    driver = app.driver
    search_element = driver.find_element(By.NAME, 'passportCode')
    search_element.send_keys(generator.get_passport_code())
    search_element_text = driver.find_element(By.CSS_SELECTOR, '#field-passportCode').get_attribute('value')
    assert search_element_text == generator.get_passport_code()


def test_enter_passport_date(app):
    driver = app.driver
    search_element = driver.find_element(By.NAME, 'passportDateGive')
    search_element.send_keys(generator.get_passport_date_give())
    search_element_text = driver.find_element(By.CSS_SELECTOR, '#field-passportDateGive').get_attribute('value')
    assert search_element_text == generator.get_passport_date_give()


def test_enter_passport_place(app):
    driver = app.driver
    search_element = driver.find_element(By.NAME, 'passportByGive')
    search_element.send_keys(generator.get_passport_by_give())
    search_element.send_keys(Keys.ARROW_DOWN)
    search_element.send_keys(Keys.ENTER)
    time.sleep(0.8)
    search_element_text = driver.find_element(By.CSS_SELECTOR, '#field-passportByGive')

    assert search_element_text.get_attribute('value') == generator.get_passport_by_give()


def test_go_to_page3(app):
    driver = app.driver
    search_element = driver.find_element(By.XPATH,
                                         '//*[@id="root"]/main/div[2]/div/div[2]/div/div/form/div[3]/div[1]/button')
    time.sleep(0.5)
    search_element.click()
    driver.get_screenshot_as_file(fr'{get_screen.path}{get_screen.generate_name_screen()}')
    time.sleep(1)
    step = driver.current_url.replace('домен', '').replace('гет параметр', '')
    assert step == 'step/2'


def test_check_status_code_page_3(app):
    test_check_status_code_page_2(app)


def test_birth_place_db(app):
    record_birth_place = db_connection.find_birth_place(get_sid(app))

    assert record_birth_place == generator.get_birth_place()


def test_passport_db(app):
    record_passport = db_connection.find_passport(get_sid(app))

    assert record_passport == generator.get_passport()


def test_passport_code_db(app):
    record_passport_code = db_connection.find_passport_code(get_sid(app))

    assert record_passport_code == generator.get_passport_code()


def test_passport_by_give_db(app):
    record_passport_by_give = db_connection.find_passport_by_give(get_sid(app))

    assert record_passport_by_give == generator.get_passport_by_give()


# End 2step form


# Start 3step form


def test_enter_inn(app):
    driver = app.driver
    search_element = driver.find_element(By.NAME, 'inn')
    search_element.send_keys(generator.get_inn())
    search_element_text = driver.find_element(By.CSS_SELECTOR, '#field-inn').get_attribute('value')
    assert search_element_text == generator.get_inn()


def test_enter_snils(app):
    driver = app.driver
    search_element = driver.find_element(By.NAME, 'snils')
    search_element.send_keys(generator.get_snils())
    time.sleep(0.7)
    search_element_text = driver.find_element(By.CSS_SELECTOR, '#field-snils').get_attribute('value')
    assert search_element_text == generator.get_snils()


def test_enter_address_registrarion(app):
    driver = app.driver
    search_element = driver.find_element(By.NAME, 'registration-address')
    search_element.send_keys(generator.get_registration_address())
    # в некоторых местах есть большие явные ошидания так как там идёт ожидание обработки dadata,
    # знаю что это некорректно но на тот момент я не знал про WebDriverWait и переписать не успел
    time.sleep(8)
    search_element.send_keys(Keys.ARROW_DOWN)
    search_element.send_keys(Keys.ENTER)
    search_element = driver.find_element(By.CSS_SELECTOR, '#field-registration-address').get_attribute('value')
    assert search_element == generator.get_registration_address()


def test_enter_fact_address_checkbox(app):
    driver = app.driver
    search_element = driver.find_element(By.XPATH,
                                         '//*[@id="root"]/main/div[2]/div/div[2]/div/div/form/div[3]/div/label')
    search_element.click()


def test_enter_address_fact(app):
    driver = app.driver
    search_element = driver.find_element(By.NAME, 'fact-address')
    search_element.send_keys(generator.get_fact_address())
    time.sleep(12)
    search_element.send_keys(Keys.ARROW_DOWN)
    search_element.send_keys(Keys.ENTER)
    driver.get_screenshot_as_file(fr'{get_screen.path}{get_screen.generate_name_screen()}')
    search_element = driver.find_element(By.CSS_SELECTOR, '#field-fact-address').get_attribute('value')
    assert search_element == generator.get_fact_address()


def test_go_to_page4(app):
    driver = app.driver
    search_element = driver.find_element(By.XPATH,
                                         '//*[@id="root"]/main/div[2]/div/div[2]/div/div/form/div[4]/div[1]/button')
    driver.execute_script("arguments[0].click();", search_element)
    time.sleep(2)
    string_url = driver.current_url
    step = string_url.replace('домен', '').replace('гет параметр', '')
    assert step == 'step/3'


def test_check_status_code_page_4(app):
    driver = app.driver
    string_url = driver.current_url
    response = requests.get(f'{string_url}')
    assert response.status_code == 200


# End 3step form

# Start 4step form

def test_choose_busy(app):
    driver = app.driver
    time.sleep(0.5)
    search_element = driver.find_element(By.XPATH,
                                         '//*[@id="field-employment"]/div/input')
    search_element.click()
    # cycle to select busy
    # почему не селектом принимал значения, отличный вопрос =) На фронте селект был выполнен как инпут,
    # при клике на который срабатывал js и выдавал значения на лету, другого способа как выбрать из так называемого селекта данные я не нашёл
    number_key = 0
    while number_key < 5:
        search_element.send_keys(Keys.ARROW_DOWN)
        time.sleep(0.3)
        number_key += 1
    search_element.send_keys(Keys.ENTER)
    search_element_text = driver.find_element(By.CSS_SELECTOR, '#field-employment > div > input')
    assert search_element_text.get_attribute('value') == generator.get_buzy()


def test_enter_name_organization(app):
    driver = app.driver
    search_element = driver.find_element(By.NAME, 'nameOrganization')
    search_element.send_keys(generator.get_name_organization())
    search_element_text = driver.find_element(By.CSS_SELECTOR, '#field-nameOrganization')
    assert search_element_text.get_attribute('value') == generator.get_name_organization()


def test_enter_position_work(app):
    driver = app.driver
    search_element = driver.find_element(By.NAME, 'positionWork')
    search_element.send_keys(generator.get_position_work())
    driver.get_screenshot_as_file(fr'{get_screen.path}{get_screen.generate_name_screen()}')
    search_element_text = driver.find_element(By.CSS_SELECTOR, '#field-positionWork')
    assert search_element_text.get_attribute('value') == generator.get_position_work()


def test_enter_selary(app):
    driver = app.driver
    search_element = driver.find_element(By.NAME, 'monthlyIncome')
    search_element.send_keys(generator.get_monthly_income())
    search_element_text = driver.find_element(By.CSS_SELECTOR, '#field-monthlyIncome')
    assert search_element_text.get_attribute('value') == generator.get_monthly_income()


def test_enter_work_phone(app):
    driver = app.driver
    search_element = driver.find_element(By.NAME, 'workPhone')
    search_element.send_keys(generator.get_work_phone())


def test_click_additional_income_checkbox(app):
    driver = app.driver
    search_element = driver.find_element(By.XPATH,
                                         '//*[@id="root"]/main/div[2]/div/div[2]/div/div/form/div[3]/div/label')
    driver.execute_script("arguments[0].click();", search_element)


def test_enter_additional_income(app):
    driver = app.driver
    search_element = driver.find_element(By.NAME, 'additionalIncomeSum')
    search_element.send_keys(generator.get_additional_income_sum())
    search_element_text = driver.find_element(By.CSS_SELECTOR, '#field-additionalIncomeSum')
    assert search_element_text.get_attribute('value') == generator.get_additional_income_sum()


def test_enter_work_address(app):
    driver = app.driver
    driver.get_screenshot_as_file(fr'{get_screen.path}{get_screen.generate_name_screen()}')
    search_element = driver.find_element(By.NAME, 'work-address')
    search_element.send_keys(generator.get_work_address())
    time.sleep(10)
    search_element.send_keys(Keys.ARROW_DOWN)
    search_element.send_keys(Keys.ENTER)
    search_element_text = driver.find_element(By.CSS_SELECTOR, '#field-work-address')
    assert search_element_text.get_attribute('value') == generator.get_work_address()
    search_element.send_keys(Keys.PAGE_DOWN)
    driver.get_screenshot_as_file(fr'{get_screen.path}{get_screen.generate_name_screen()}')
    search_element.send_keys(Keys.PAGE_DOWN)


def test_enter_contact_name(app):
    driver = app.driver
    search_element = driver.find_element(By.NAME, 'contactFullName')
    search_element.send_keys(generator.get_contact_full_name())
    search_element_text = driver.find_element(By.CSS_SELECTOR, '#field-contactFullName').get_attribute('value')
    assert search_element_text == generator.get_contact_full_name()


def test_enter_contact_phone(app):
    driver = app.driver
    search_element = driver.find_element(By.NAME, 'contactPhone')
    search_element.send_keys(generator.get_contact_phone())
    search_element_text = driver.find_element(By.CSS_SELECTOR, '#field-contactPhone').get_attribute('value')
    assert clear_validate(search_element_text) == generator.get_contact_phone()


def test_go_to_page5(app):
    driver = app.driver
    time.sleep(2)
    search_element = driver.find_element(By.CSS_SELECTOR, '#root > main > div:nth-child(2) > div > div:nth-child(2)'
                                                          ' > div > div > form > div.pagination.clr > div.pagination--col-next > button')
    driver.execute_script("arguments[0].click();", search_element)
    time.sleep(1)

    string_url = driver.current_url
    step = string_url.replace('домен', '').replace('гет параметр',
                         '')
    assert step == 'step/4'


def test_check_status_code_page_5(app):
    driver = app.driver
    string_url = driver.current_url
    response = requests.get(f'{string_url}')
    assert response.status_code == 200


# End 4step form

# Start 5step form

def test_choose_sum_money(app):
    driver = app.driver
    search_element = driver.find_element(By.CSS_SELECTOR, '#field-sumMoney')
    search_element.send_keys(Keys.LEFT_CONTROL, 'a')
    search_element.send_keys(Keys.DELETE)
    search_element.send_keys(generator.get_sum_get_money())
    assert search_element.get_attribute('value') == generator.get_sum_get_money()


def test_choose_period(app):
    driver = app.driver
    search_element = driver.find_element(By.CSS_SELECTOR, '#field-period')
    search_element.send_keys(Keys.LEFT_CONTROL, 'a')
    search_element.send_keys(Keys.DELETE)
    search_element = driver.find_element(By.CSS_SELECTOR, '#field-period')
    search_element.send_keys(generator.get_get_period())
    search_element = driver.find_element(By.CSS_SELECTOR, '#field-period')
    assert search_element.get_attribute('value') == generator.get_get_period()


def test_choose_checkbox_pay(app):
    driver = app.driver
    search_element = driver.find_element(By.XPATH,
                                         '//*[@id="root"]/main/div[2]/div/div[2]/div/div/form/div[2]/div[2]/div/div/label')
    search_element.click()


def test_enter_promo(app):
    driver = app.driver
    search_element = driver.find_element(By.NAME, 'promoCode')
    search_element.send_keys(generator.get_promo_code())
    time.sleep(2.5)
    #уведомления об ошибках тоже обрабатываются скриптом, изящнее решения я не смог найти и просто прикрутил парсер на момент ошибки
    alert_HTML_all = driver.execute_script('return document.body.innerHTML')
    HTML_parser = bs4.BeautifulSoup(alert_HTML_all, "lxml")
    alert_p = HTML_parser.find_all("p", attrs={'class': 'success form-message'})

    assert alert_p


def test_send_form_1(app):
    driver = app.driver
    driver.get_screenshot_as_file(fr'{get_screen.path}{get_screen.generate_name_screen()}')
    search_element = driver.find_element(By.CSS_SELECTOR,
                                         '#root > main > div:nth-child(2) > div > div:nth-child(2) > div > div > form > div.pagination.clr > div:nth-child(1) > div > button')
    driver.execute_script("arguments[0].click();", search_element)
    time.sleep(1)


def test_enter_sms_code_final(app):
    driver = app.driver
    search_element = driver.find_element(By.NAME, 'sms-code-submit')
    search_element.send_keys(generator.get_sms_code_last())
    time.sleep(1.5)
    search_element = driver.find_element(By.CSS_SELECTOR, '#field-sms-code-submit')
    assert search_element.get_attribute('value') == generator.get_sms_code_last()


def test_send_form_final(app):
    driver = app.driver
    search_element = driver.find_element(By.XPATH,
                                         '//*[@id="root"]/main/div[2]/div/div[2]/div/div/form/div[4]/div[1]/div/div[3]/div/div/button')
    driver.execute_script("arguments[0].click();", search_element)
    time.sleep(4)
    driver.get_screenshot_as_file(fr'{get_screen.path}{get_screen.generate_name_screen()}')


def test_responce_final_form(app):
    driver = app.driver
    alert_HTML_all = driver.execute_script('return document.body.innerHTML')
    HTML_parser = bs4.BeautifulSoup(alert_HTML_all, "lxml")
    alert_p = HTML_parser.find_all("h3", attrs={'class': 'modal-title'})

    assert alert_p


def test_delete_db(app):
    db_connection.delete_test_data_db(get_sid(app))
