import driver
from selenium.webdriver.common.by import By

class menupim:
    url='https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'

    def __init__(self, driver):
        self.driver = driver

    def is_url_menupim(self):
        return driver.current_url==self.url
    def criar_user(self):
        self.driver.findelement((By.CLASS_NAME, 'class="oxd-icon bi-list oxd-topbar-header-hamburger"')).click()
        self.driver.findelement((By.CLASS_NAME,'oxd-text oxd-text--span oxd-main-menu-item--name')).click()
        self.driver.findelement(By.CSS_SELECTOR, '[type="button"]').click()