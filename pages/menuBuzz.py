import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By


class WebdriverWait:
    pass


class test_menu_buzz:
    url_buzz = 'https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz'

    def __init__(self, driver):
        self.input_new_post = None
        self.driver=driver

    def test_is_url_buzz(self):
        return self.driver.current_url==self.url_buzz

    def test_click_buzz(self):
        self.driver.find_element(By.CSS_SELECTOR,'#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(12) > a').click()
        time.sleep(3)

    def test_validar_like(self):
        self.driver.find_element(By.CSS_SELECTOR, '#heart').click()
        time.sleep(3)



