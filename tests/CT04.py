from selenium.webdriver.common.by import By

from pages.loginPage import LoginPage

url_demo = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

class Test4:
    def test_create_user(self, test_login_button):
        loginp=LoginPage()
        loginp.test_login_button()
        loginp.close()
        driver.findelement((By.CLASS_NAME,'class="oxd-icon bi-list oxd-topbar-header-hamburger"')).click()

        driver.findelement(By.CLASS_NAME,'oxd-text oxd-text--span oxd-main-menu-item--name')).click()
        driver.findelement(By.CSS_SELECTOR,'[type="button"]').click()


