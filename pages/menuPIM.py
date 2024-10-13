
from selenium.webdriver.common.by import By
class test_menupim:

    url='https://opensource-demo.orangehrmlive.com/dashboard/index'
    url_pim='https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList'
    def __init__(self, driver):
        self.driver=driver

    def test_is_url_dashboard(self):
        return self.driver.current_url==self.url

    def test_is_url_pim(self):
        return self.driver.current_url == self.url_pim

    def test_pim_button(self):
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.CSS_SELECTOR,'#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(2) > a > span').click()

    def test_criar_user(self):
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.CSS_SELECTOR,'#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div.orangehrm-paper-container > div.orangehrm-header-container > button').click()
        self.driver.find_element(By.CSS_SELECTOR, '[name="firstName"]').send_keys('Jerla')
        self.driver.find_element(By.CSS_SELECTOR, '[name = "lastName"]').send_keys('Maria')
        self.driver.find_element(By.CSS_SELECTOR, '[type = "submit"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[type = "submit"]').click()
        self.driver.find_element(By.CSS_SELECTOR,'#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(2) > a').click()

    def test_busca_cadastro(self):
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.CSS_SELECTOR,'[placeholder="Type for hints..."]').send_keys('Jerla Maria')
        self.driver.find_element(By.CSS_SELECTOR, '[type = "submit"]').click()

        #assert self.driver.find_element(By.CSS_SELECTOR, 'class="header"').text == 'Janicleide', 'Nome invalido'
        #assert self.driver.find_element(By.CSS_SELECTOR, '[class="data"]').text == 'Maria', 'Nome invalido'


