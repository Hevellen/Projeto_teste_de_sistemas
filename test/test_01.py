from pages.menuAdmin import test_menu_admin

class Test_01:
    def test_create_user(self, test_open_browser):
        login_p = test_open_browser
        login_p.test_login_button()
        assert login_p.test_is_url_login(), 'URL válida'

        menu_admin = test_menu_admin(driver=login_p.driver)
        menu_admin.test_click_admin()
        assert menu_admin.test_is_url_admin(), 'URL inválida'
        menu_admin.test_seleciona_filtro()
        menu_admin.test_filtra()