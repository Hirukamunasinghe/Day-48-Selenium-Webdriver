from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver_service = Service(executable_path="C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)

URL ="https://en.wikipedia.org/wiki/Main_Page"
driver.get(URL)

#click
# article_count = driver.find_element(By.CSS_SELECTOR,"#articlecount a")
# print(article_count.text)
# article_count.click()

person_name = driver.find_element(By.LINK_TEXT,"Eduard Fraenkel")
# person_name.click()

#search
search = driver.find_element(By.NAME,"search")
search.send_keys("python")
search.send_keys(Keys.ENTER)




# driver.close()