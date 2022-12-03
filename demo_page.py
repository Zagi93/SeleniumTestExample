from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("http://www.kurs-selenium.pl/demo/")
driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/ul/li[1]/a").click()
driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/ul/li[1]/ul/li[2]/a").click()
driver.find_element_by_name("firstname").send_keys("Jak")
driver.find_element_by_name("lastname").send_keys("Melko")
driver.find_element_by_name("phone").send_keys("555-555-555")
driver.find_element_by_name("email").send_keys("jako@gmail.com")
driver.find_element_by_name("password").send_keys("korniszon")
driver.find_element_by_name("confirmpassword").send_keys("korniszon")
driver.find_element_by_xpath("//*[@id='headersignupform']/div[9]/button").click()









driver.quit()



