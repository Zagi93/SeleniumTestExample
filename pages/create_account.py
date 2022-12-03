from locators import locators

class CreateAccount:


    def __init__(self,driver):
        self.driver = driver
        self.click1 = locators.RegistrAddress.click1
        self.click2 = locators.RegistrAddress.click2
        self.firstname = locators.RegistrAddress.firstname
        self.lastname = locators.RegistrAddress.lastname
        self.phone = locators.RegistrAddress.phone
        self.email = locators.RegistrAddress.email
        self.password = locators.RegistrAddress.password
        self.confirm_password = locators.RegistrAddress.confirm_password
        self.bottom = locators.RegistrAddress.bottom


    def open_web_side(self):
        self.driver.get("http://www.kurs-selenium.pl/demo/")

    def get_in_login(self):
        self.driver.find_element_by_xpath(self.click1).click()

    def get_in_login2(self):
        self.driver.find_element_by_xpath(self.click2).click()


    def fisrt_name(self,name):
        self.driver.find_element_by_name(self.firstname).send_keys(name)

    def last_name(self,name2):
        self.driver.find_element_by_name(self.lastname).send_keys(name2)

    def odders_dane(self, phone, email, password, confirmpassword):
        self.driver.find_element_by_name(self.phone).send_keys(phone)
        self.driver.find_element_by_name(self.email).send_keys(email)
        self.driver.find_element_by_name(self.password).send_keys(password)
        self.driver.find_element_by_name(self.confirm_password).send_keys(confirmpassword)

    def bottom_press(self):
        self.driver.find_element_by_xpath(self.bottom).click()


