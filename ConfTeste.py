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

    assert driver.current_url=='https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index',"URL INválida"
    yield driver
    #consegui fazer o LOGIN



















