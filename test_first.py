import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def test_menu_item():
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options, executable_path='/Users/dmitr/PycharmProjects/tms_aqa_python_pytest/chromedriver.exe')
    driver.get('https://spb.minfin.gov.by/')
    driver.fullscreen_window()

    time.sleep(1)

    menu_item_locator = driver.find_element(By.XPATH,'//div[contains(text(),"Справочная информация")]')
    menu_item_locator.click()

    header_locator = driver.find_element(By.XPATH,'//h3[contains(text(),"Справочная информация")]')
    assert header_locator.is_displayed() == True
