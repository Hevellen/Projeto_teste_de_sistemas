import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
class test_1:
        @pytest.fixture
        def open_browser(self):
                url_demo = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
                self.driver = webdriver.Chrome()
                self.driver.get(url_demo)
                time.sleep(2)
        def login(self,open_browser):
                self.driver.find_element(By.CSS_SELECTOR, '[placeholder="Username"]').send_keys('Admin')
                self.driver.find_element(By.CSS_SELECTOR, '[placeholder="Password"]').send_keys('admin123')
                self.driver.find_element(By.CSS_SELECTOR,'#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div.oxd-form-actions.orangehrm-login-action > button').click()
                time.sleep(5)
                assert self.driver.current_url=='https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index',"URL INválida"
                self.driver.quit()
                #consegui fazer o LOGIN


















