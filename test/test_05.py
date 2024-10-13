from pages.menuPIM import test_menupim


class Test5:
    def test_edit_user(self, test_open_browser):
        login_p = test_open_browser
        login_p.test_login_button()
        assert login_p.test_is_url_login(), 'URL válida'

        edit_menu_pim = test_menupim(driver=login_p.driver)
        edit_menu_pim.test_pim_button()
        assert edit_menu_pim.test_is_url_dashboard, 'URL inválida'
