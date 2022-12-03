from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://www.kurs-selenium.pl/demo/login")
driver.implicitly_wait(10)
driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/form/div[1]/div[5]/div/div[1]/input").send_keys("jako@gmail.com")
driver.find_element(By.NAME,"password").send_keys("korniszon")
driver.find_element(By.XPATH,"//button[@style='font-size: 16px;']").click()




