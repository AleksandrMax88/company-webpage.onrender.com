from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
# from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service

# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

URL = "https://company-webpage.onrender.com/"
button_login = (By.CSS_SELECTOR, "li p")
button_login_tooltip = (By.CSS_SELECTOR, "div [class='tooltip-inner']")
input_username = (By.CSS_SELECTOR, "input[name='username']")
input_password = (By.CSS_SELECTOR, "input[name='password']")
button_submit = (By.CSS_SELECTOR, 'input[value="Submit"]')
logged_out = (By.CSS_SELECTOR, 'body > div:nth-child(2) > a')
username = 'admin.user'
password = 'Admin_1234'


def test_check_title_login():
    driver.get(URL)
    time.sleep(10)
    driver.maximize_window()
    expected_text = "Login"
    element_find = driver.find_element(*button_login).text
    assert element_find == expected_text


def test_check_tooltip_title_login():
    driver.get(URL)
    time.sleep(10)
    driver.maximize_window()
    expected_text = "Login"
    tooltip_login = driver.find_element(*button_login)
    ActionChains(driver).move_to_element(tooltip_login).perform()
    tooltip_text = driver.find_element(*button_login_tooltip).text
    assert tooltip_text == expected_text


def test_login_up():
    driver.get(URL)
    time.sleep(10)
    driver.maximize_window()
    expected_text = "Logout"
    login_find = driver.find_element(*button_login)
    login_find.click()
    search_user_name = driver.find_element(*input_username)
    search_user_name.send_keys(username)
    search_password = driver.find_element(*input_password)
    search_password.send_keys(password)
    search_submit = driver.find_element(*button_submit)
    search_submit.click()
    element_find = driver.find_element(*button_login).text
    assert element_find == expected_text


def test_log_out():
    driver.get(URL)
    time.sleep(10)
    driver.maximize_window()
    expected_text_logout = "Click here to login again."
    search_logout = driver.find_element(*button_login)
    search_logout.click()
    time.sleep(2)
    element_find = driver.find_element(*logged_out).text
    assert element_find == expected_text_logout

    driver.quit()
