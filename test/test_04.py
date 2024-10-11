#CT04-criar conta no menu PIM
from conftest import test_open_browser
from pages.loginPage import test_LoginPage
from pages.menuPIM import test_menupim

class Test4:
    def test_create_user(self, test_open_browser):
        login_p = test_open_browser
        login_p.test_login_button()
        assert login_p.test_is_url_login(), 'URL válida'












