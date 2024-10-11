import pytest

from pages.loginPage import test_LoginPage

@pytest.fixture
def openbrowser():
       loginp=test_LoginPage()
       loginp.test_open_login_page()
       yield loginp
       loginp.test_close()























