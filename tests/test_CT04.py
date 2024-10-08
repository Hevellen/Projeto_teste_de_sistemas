from pages.menuPIM import test_menupim
#CT04-criar conta no menu PIM
url_demo = 'https://opensource-demo.orangehrmlive.com/auth/login'

class Test4:
    def test_create_user(self,openbrowser):
        loginp=openbrowser()
        loginp.test_login_button()

        menu_pim=test_menupim(driver=loginp.driver)
        menu_pim.test_is_url_menupim(),"URL inválida!"
        menu_pim=test_menupim(driver=loginp.driver)
        menu_pim.test_pim_button()







