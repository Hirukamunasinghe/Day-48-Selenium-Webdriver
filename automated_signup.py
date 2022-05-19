from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver_service = Service(executable_path="C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)

URL ="http://secure-retreat-92358.herokuapp.com/"
driver.get(URL)

#Filling out the form
#First Name
f_name = driver.find_element(By.NAME,"fName")
f_name.send_keys("Hiruka")
f_name.send_keys(Keys.ENTER)

#Last Name
l_name = driver.find_element(By.NAME,"lName")
l_name.send_keys("Munasinghe")
l_name.send_keys(Keys.ENTER)

#Email address
email = driver.find_element(By.NAME,"email")
email.send_keys("munasinghehiruka@gmail.com")
email.send_keys(Keys.ENTER)

#Clicking the submit button
submit = driver.find_element(By.CSS_SELECTOR,"form button")
submit.click()


