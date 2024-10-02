import pytest
import time
from selenium.webdriver.common.by import By

from pages.loginPage import LoginPage

@pytest.fixture
def test_open_browser():
   loginp=LoginPage()
   loginp.open_login_page()
    yield loginp
    loginp.close()

@pytest.fixture
def test_login_button(test_open_browser):
    driver = test_open_browser
    driver.find_element(By.CSS_SELECTOR, '[placeholder="Username"]').send_keys('Admin')
    driver.find_element(By.CSS_SELECTOR, '[placeholder="Password"]').send_keys('admin123')
    driver.find_element(By.CSS_SELECTOR,'#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div.oxd-form-actions.orangehrm-login-action > button').click()
    assert driver.current_url=='https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index',"URL INválida"
    yield driver
    #consegui fazer o LOGIN



















