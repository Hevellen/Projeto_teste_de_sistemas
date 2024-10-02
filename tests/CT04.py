from pages.menuPIM import menupim

url_demo = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

class Test4:
    def test_create_user(self, test_open_browser):
        loginp=test_open_browser()
        loginp.test_login_button()
        menu_pim=menupim()
        menu_pim.is_url_menupim(),"URL inválida!"





