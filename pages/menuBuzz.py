import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class test_menu_buzz:
    url_buzz = 'https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz'

    def __init__(self, driver):
        self.driver=driver

    def test_is_url_buzz(self):
        return self.driver.current_url==self.url_buzz

    def test_click_buzz(self):
        self.driver.find_element(By.CSS_SELECTOR,'#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(12) > a').click()
        time.sleep(3)

    def test_digit(self):
        self.driver.find_element(By.CSS_SELECTOR,'[#Buzz\ Newsfeed > div > div.oxd-sheet.oxd-sheet--rounded.oxd-sheet--gutters.oxd-sheet--white.orangehrm-buzz-create-post > div.orangehrm-buzz-create-post-header > div.orangehrm-buzz-create-post-header-text > form > div > textarea]').sendkeys('Eu tenho uma pergunta')


