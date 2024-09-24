import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
url_demo = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
class Test1:
        @pytest.fixture
        def open_browser(self):
                driver=webdriver.Chrome()
                driver.get(url_demo)
                yield driver
                time.sleep(2)
                driver.quit()
        def test_login_button(open_browser):
                driver=open_browser
                driver.find_element(By.CSS_SELECTOR, '[placeholder="Username"]').send_keys('Admin')
                driver.find_element(By.CSS_SELECTOR, '[placeholder="Password"]').send_keys('admin123')
                driver.find_element(By.CSS_SELECTOR,'#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div.oxd-form-actions.orangehrm-login-action > button').click()
                assert driver.current_url=='https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index',"URL INválida"
                yield driver
                #consegui fazer o LOGIN



















