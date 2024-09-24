import driver
from selenium.webdriver.common.by import By


class Test4:
    def test_create_user(self,test_login_button):
        driver=test_login_button
        driver.find_element(By.CLASS_NAME,'class="oxd-icon bi-list oxd-topbar-header-hamburger"').click()
