import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class test_LoginPage:
    url_demo = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

    def __init__(self):
        self.driver = webdriver.Chrome()

    def test_open_login_page(self):
        self.driver.get(self.url_demo)
        time.sleep(3)
    def test_login_button(self):
        self.driver.find_element(By.CSS_SELECTOR, '[placeholder="Username"]').send_keys('Admin')
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, '[placeholder="Password"]').send_keys('admin123')
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, '#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div.oxd-form-actions.orangehrm-login-action > button').click()
        time.sleep(2)
    def test_is_url_login(self):
        return self.driver.current_url=='https://opensource-demo.orangehrmlive.com/dashboard/index',"URL INválida"
    def test_close(self):
        self.driver.quit()

