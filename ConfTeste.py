import pytest

from pages.loginPage import LoginPage, test_LoginPage


@pytest.fixture
def test_open_browser():
       loginp=test_LoginPage()
       loginp.test_open_login_page()
       yield loginp
       loginp.test_close()





















