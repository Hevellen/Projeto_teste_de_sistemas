#CT04-criar conta no menu PIM
from conftest import test_open_browser
from pages.menuPIM import test_menupim
url_demo = 'https://opensource-demo.orangehrmlive.com/auth/login'

class Test4:
    def test_create_user(self, test_open_browser):
        loginp=test_open_browser()
        loginp.test_login_button()
        menu_pim=test_menupim(driver=loginp.driver)
        menu_pim.test_is_url_menupim(),"URL inválida!"
        menu_pim=test_menupim(driver=loginp.driver)
        menu_pim.test_pim_button()








