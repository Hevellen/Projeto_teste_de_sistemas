from telnetlib import EC

from pages.Recruitment import test_Recruitment
from selenium.webdriver.support.wait import WebDriverWait


class Test_07:
    def test_create_user(self,test_open_browser):
        login_p = test_open_browser
        login_p.test_login_button()
        assert login_p.test_is_url_login(), 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'


def access_recruitment(self, Recruitment):
    WebDriverWait(self.driver, 10).until(
        EC.visiliby_of_element_located(self.list_of_modules)

    )


    test_Recruitment = self.driver.find_elements(self.modulr_item)
    for module in recruitment:
        if module.text == test_Recruitment:
           WebDriverWait(self.driver, 5).until(
               EC.element_to_be_clickable(recruitment)
           ).click()
           break