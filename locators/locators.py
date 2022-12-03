from selenium.webdriver.common.by import By


class BillingAdressLocators:

    addresses_link_input = (By.LINK_TEXT, "Addresses")
    edit_link_input = (By.LINK_TEXT, "Edit")
    first_name_input = (By.ID, "billing_first_name")
    last_name_input = (By.ID, "billing_last_name")
    billing_company = (By.ID, "billing_company")
    billing_country_select = (By.ID, "billing_country")
    billing_address_input = (By.ID, "billing_address_1")
    billing_postcode_input = (By.ID, "billing_postcode")
    billing_city_input = (By.ID, "billing_city")
    billing_phone_phone = (By.ID, "billing_phone")
    save_address_button = (By.NAME, "save_address")
    message_div = (By.XPATH, "//div[@class='woocommerce-message']")


class MyAccountPage:

    username_input = (By.ID, "username")
    password_input = (By.ID, "password")
    reg_email_input = (By.ID, "reg_email")
    reg_password = (By.ID, "reg_password")
    my_account_link = (By.XPATH, "//li[@id='menu-item-22']//a")
    error_meg = (By.XPATH, "//ul[@class='woocommerce-error']//li")
    logout_link = (By.LINK_TEXT, "Logout")


class RegistrAddress:

    click1 = "/html/body/nav/div/div[2]/ul[2]/ul/li[1]/a"
    click2 = "/html/body/nav/div/div[2]/ul[2]/ul/li[1]/ul/li[2]/a"

    firstname = "firstname"
    lastname = "lastname"
    phone = "phone"
    email = "email"
    password = "password"
    confirm_password = "confirmpassword"
    bottom = "//*[@id='headersignupform']/div[9]/button"









