from pages.menuPIM import test_menupim
#CT-004 - Adicionar usuário - Jonatas

class Test_04:
    def test_create_user(self,test_open_browser):
        login_p = test_open_browser
        login_p.test_login_button()
        assert login_p.test_is_url_login(), 'URL válida'

        menu_pim = test_menupim(driver=login_p.driver)
        menu_pim.test_pim_button()
        assert menu_pim.test_is_url_pim(), 'URL inválida'
        menu_pim.test_criar_user()
        menu_pim.test_pim_button()
        menu_pim.test_busca_cadastro()



