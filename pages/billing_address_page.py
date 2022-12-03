from selenium.webdriver.support.select import Select

from locators import locators



class BillingAddressPage:


    def __init__(self,driver):
        self.driver = driver
        self.addresses_link_input = locators.BillingAdressLocators.addresses_link_input
        self.edit_link_input = locators.BillingAdressLocators.edit_link_input
        self.first_name_input = locators.BillingAdressLocators.first_name_input
        self.last_name_input = locators.BillingAdressLocators.last_name_input
        self.billing_company = locators.BillingAdressLocators.billing_company
        self.billing_country_select = locators.BillingAdressLocators.billing_country_select
        self.billing_address_input = locators.BillingAdressLocators.billing_address_input
        self.billing_postcode_input = locators.BillingAdressLocators.billing_postcode_input
        self.billing_city_input = locators.BillingAdressLocators.billing_city_input
        self.billing_phone_phone = locators.BillingAdressLocators.billing_phone_phone
        self.save_address_button = locators.BillingAdressLocators.save_address_button
        self.message_div = locators.BillingAdressLocators.message_div

    def open_edit_billing_address(self):
        self.driver.find_element(*self.addresses_link_input).click()
        self.driver.find_element(*self.edit_link_input).click()


    def set_personal_date(self,first_name, last_name):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)

    def select_country(self, country):
        select = Select(self.driver.find_element(*self.billing_country_select))
        select.select_by_visible_text(country)

    def set_address(self, street, postcode, city):
        self.driver.find_element(*self.billing_address_input).send_keys(street)
        self.driver.find_element(*self.billing_postcode_input).send_keys(postcode)
        self.driver.find_element(*self.billing_city_input).send_keys(city)

    def set_phone_number(self, number):
        self.driver.find_element(*self.billing_phone_phone).send_keys(number)


    def save_address(self):
        self.driver.find_element(*self.save_address_button).click()

    def get_message_text(self):
        return self.driver.find_element(*self.message_div).text










