from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import random
import pytest

from pages.billing_address_page import BillingAddressPage
from pages.my_account_page import MyAccountPage


@pytest.mark.usefixtures("setup")
class TestUpdateBillingAddress:

    def test_update_billing_adress(self):
        email = str(random.randint(0, 10000)) + "tester1@go2.pl"
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account(email, "ChromeDriverManager")
        billing_address_page = BillingAddressPage(self.driver)
        billing_address_page.open_edit_billing_address()
        billing_address_page.set_personal_date("Jak", "Meko")
        billing_address_page.select_country("Poland")
        billing_address_page.set_phone_number("555-555-555")
        billing_address_page.set_address("Kwiatowa 1","00-000","Warszawa")
        billing_address_page.save_address()


        assert "Address changed successfully." in billing_address_page.get_message_text()





