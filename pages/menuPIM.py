import time

from selenium.webdriver.common.by import By
class test_menupim:

    url = 'https://opensource-demo.orangehrmlive.com/dashboard/index'
    url_pim = 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList'

    def __init__(self, driver):
        self.driver=driver

    def test_is_url_dashboard(self):
        return self.driver.current_url==self.url

    def test_is_url_pim(self):
        return self.driver.current_url == self.url_pim

    def test_pim_button(self):
        self.driver.find_element(By.CSS_SELECTOR,'#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(2) > a > span').click()
        time.sleep(3)
    def test_criar_user(self):
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,'#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div.orangehrm-paper-container > div.orangehrm-header-container > button').click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, '[name="firstName"]').send_keys('Maria')
        self.driver.find_element(By.CSS_SELECTOR, '[name = "lastName"]').send_keys('Joaquina')
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, '[type = "submit"]').click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, '[type = "submit"]').click()
        time.sleep(5)

    def test_busca_cadastro(self):
        self.driver.find_element(By.CSS_SELECTOR,'#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(2) > a > span').click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,'#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div.oxd-table-filter > div.oxd-table-filter-area > form > div.oxd-form-row > div > div:nth-child(1) > div > div:nth-child(2) > div > div > input').send_keys('Maria Joaquina')
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, '[type = "submit"]').click()
        time.sleep(5)
        assert self.driver.find_element(By.CSS_SELECTOR,'#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div.orangehrm-paper-container > div:nth-child(2) > div').text == '(1) Record Found', 'Titulo invalido'

    #assert self.driver.find_element(By.CSS_SELECTOR, 'class="header"').text == 'Janicleide', 'Nome invalido'
        #assert self.driver.find_element(By.CSS_SELECTOR, '[class="data"]').text == 'Maria', 'Nome invalido'

    def test_editar_user(self):
        self.driver.find_element(By.CSS_SELECTOR,'#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(2) > a > span').click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,'#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div.oxd-table-filter > div.oxd-table-filter-area > form > div.oxd-form-row > div > div:nth-child(1) > div > div:nth-child(2) > div > div > input').send_keys('Joana Novasco')
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, '[type = "submit"]').click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR,'#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div.orangehrm-paper-container > div:nth-child(2) > div').click()


