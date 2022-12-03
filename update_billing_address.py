from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import random




def test_update_billing_adress():
    email = str(random.randint(0,10000)) + "tester1@go2.pl"
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://seleniumdemo.com/?page_id=7")
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "reg_email").send_keys(email)
    driver.find_element(By.ID, "reg_password").send_keys("ChromeDriverManager")
    driver.find_element(By.ID, "reg_password").send_keys(Keys.ENTER)
    driver.find_element(By.LINK_TEXT, "Addresses").click()
    driver.find_element(By.LINK_TEXT, "Edit").click()
    driver.find_element(By.ID, "billing_first_name").send_keys("Melko")
    driver.find_element(By.ID, "billing_last_name").send_keys("wario")
    driver.find_element(By.ID, "billing_company").send_keys("TesterAutomatyczny")
    Select(driver.find_element(By.ID, "billing_country")).select_by_visible_text("Poland")
    driver.find_element(By.ID, "billing_address_1").send_keys("Konwaliowa 1")
    driver.find_element(By.ID, "billing_postcode").send_keys("00-000")
    driver.find_element(By.ID, "billing_city").send_keys("Wrocław")
    driver.find_element(By.ID, "billing_phone").send_keys("555-555-555")
    driver.find_element(By.NAME, "save_address").click()

    assert "Address changed successfully." in driver.find_element(By.XPATH, "//div[@class='woocommerce-message']").text





