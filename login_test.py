from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def test_log_in():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://seleniumdemo.com/")
    # wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.find_element(By.XPATH, "//li[@id='menu-item-22']//a").click()
    driver.find_element(By.ID, "username").send_keys("tester@go2.pl")
    driver.find_element(By.ID, "password").send_keys("ChromeDriverManager")
    driver.find_element(By.NAME, "login").click()

    assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()


def test_log_failed():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://seleniumdemo.com/")
    # wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.find_element(By.XPATH, "//li[@id='menu-item-22']//a").click()
    driver.find_element(By.ID, "username").send_keys("tester1@go2.pl")
    driver.find_element(By.ID, "password").send_keys("ChromeDriverManager1")
    driver.find_element(By.NAME, "login").click()

    assert "ERROR: Incorrect username or password" in driver.find_element(By.XPATH, "//ul[@class='woocommerce-error']//li").text




