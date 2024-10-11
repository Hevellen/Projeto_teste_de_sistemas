import pytest

from pages.loginPage import test_LoginPage

@pytest.fixture
def test_open_browser():
       login_p=test_LoginPage()
       login_p.test_open_login_page()
       yield login_p
       login_p.test_close()























