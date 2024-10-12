import time
from os import times

import driver
from selenium.webdriver.common.by import By
class test_menupim:
    url='https://opensource-demo.orangehrmlive.com/dashboard/index'

    def __init__(self, driver):
        self.driver=driver

    def test_is_url_menupim(self):
        return self.driver.current_url==self.url

    def test_pim_button(self):
        self.driver.find_element(By.CSS_SELECTOR,'#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(2) > a > span').click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,'#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div.orangehrm-paper-container > div.orangehrm-header-container > button').click()
        time.sleep(5)
    def test_criar_user(self):
        self.driver.find_element(By.CSS_SELECTOR, '[name="firstName"]').send_keys('Jani')
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, '[name = "lastName"]').send_keys('Maria')
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, '[type = "submit"]').click()
        time.sleep(4)
        self.driver.find_element(By.CSS_SELECTOR, '[type = "submit"]').click()
        time.sleep(6)
        self.driver.find_element(By.CSS_SELECTOR,'#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(2) > a').click()
        time.sleep(4)
    def test_busca_cadastro(self):
        self.driver.find_element(By.CSS_SELECTOR,'[placeholder="Type for hints..."]').send_keys('Jani Maria')
        time.sleep(4)
        self.driver.find_element(By.CSS_SELECTOR, '[type = "submit"]').click()
        time.sleep(3)
        assert self.driver.find_element(By.CSS_SELECTOR, 'class="header"').text == 'Jani', 'Nome invalido'
        assert self.driver.find_element(By.CSS_SELECTOR, '[class="data"]').text == 'Maria', 'Nome invalido'



