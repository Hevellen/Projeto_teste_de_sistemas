from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

class Test4:
    def test_create_user(self, test_login_button):
        driver=test_login_button
        driver.findelement((By.CLASS_NAME,'class="oxd-icon bi-list oxd-topbar-header-hamburger"')).click()


