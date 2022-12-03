import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://seleniumdemo.com/")
driver.find_element_by_id("menu-item-21").click()
driver.find_element_by_xpath("//*[@id='content']/ul/li[3]/a[2]").click()
driver.find_element_by_class_name("nav__title").click()

assert "Your cart is currently empty." in driver.find_element_by_class_name("cart-empty").text

driver.quit()







