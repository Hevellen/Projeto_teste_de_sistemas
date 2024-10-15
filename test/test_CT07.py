from pages.Recruitment import test_Recruitment


class Test_07:
    def test_create_user(self,test_open_browser):
        login_p = test_open_browser
        login_p.test_login_button()
        assert login_p.test_is_url_login(), 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'



