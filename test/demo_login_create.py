


import pytest
from pages.create_account import CreateAccount

@pytest.mark.usefixtures("setup")
class TestLoginAccountCreate:

    def test_loggin(self):
        create_account = CreateAccount(self.driver)
        create_account.open_web_side()
        create_account.get_in_login()
        create_account.get_in_login2()
        create_account.fisrt_name("Mleko")
        create_account.last_name("Jak")
        create_account.odders_dane("555-555-555","jak@go2.pl","kalisz93","kalisz93")
        create_account.bottom_press()
