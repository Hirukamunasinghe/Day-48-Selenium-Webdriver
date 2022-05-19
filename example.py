from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_service = Service(executable_path="C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)


URL ="https://www.python.org/"
driver.get(URL)

#Getting the price
# price = driver.find_element(By.CLASS_NAME,"a-price-whole")
# print(price.text)

#Search bar
search_bar = driver.find_element(By.NAME,"q")
print(search_bar.get_attribute("placeholder"))

#Logo
logo = driver.find_element(By.CLASS_NAME,"python-logo")
print(logo.size)

#Docs Link
documentation_link = driver.find_element(By.CSS_SELECTOR,".documentation-widget a")
print(documentation_link.text)

#xpath
bug_link = driver.find_element(By.XPATH,'//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

driver.close()

