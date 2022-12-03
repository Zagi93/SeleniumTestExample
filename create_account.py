from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import random


def test_create_account_failed():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://seleniumdemo.com/?page_id=7")
    driver.implicitly_wait(10)
    driver.find_element(By.ID,"reg_email").send_keys("tester1@go2.pl")
    driver.find_element(By.ID,"reg_password").send_keys("ChromeDriverManager")
    driver.find_element(By.ID,"reg_password").send_keys(Keys.ENTER)


    assert "An account is already registered with your email address. Please log in." in driver.find_element(By.XPATH,"//ul[@class='woocommerce-error']//li").text

def test_create_account_passed():
    email = str(random.randint(0,10000)) + "tester1@go2.pl"
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://seleniumdemo.com/?page_id=7")
    driver.implicitly_wait(10)
    driver.find_element(By.ID,"reg_email").send_keys(email)
    driver.find_element(By.ID,"reg_password").send_keys("ChromeDriverManager")
    driver.find_element(By.ID,"reg_password").send_keys(Keys.ENTER)

    assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()