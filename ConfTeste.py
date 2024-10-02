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





















