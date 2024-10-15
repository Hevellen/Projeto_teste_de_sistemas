from pages.menuBuzz import test_menu_buzz



class Test_06:
    def test_create_user(self,test_open_browser):
        login_p = test_open_browser
        login_p.test_login_button()
        assert login_p.test_is_url_login(), 'URL válida'

        menu_buzz = test_menu_buzz(driver=login_p.driver)
        menu_buzz.test_click_buzz()
        menu_buzz.test_is_url_buzz()
        menu_buzz.test_digitar()


