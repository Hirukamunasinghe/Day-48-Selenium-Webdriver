#Cookie clicker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver_service = Service(executable_path="C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)

URL ="https://orteil.dashnet.org/cookieclicker/"
driver.get(URL)

cookie = driver.find_element(By.ID,"bigCookie")
while True:
    cookie.click()
    cursor_price = driver.find_element(By.XPATH,'//*[@id="productPrice0"]')
    no_cursor_price = cursor_price.text
    cookies_amount = driver.find_element(By.XPATH,'//*[@id="cookies"]')
    no_cookies_amount = cookies_amount.text.split(" ")[0]
    if int(no_cookies_amount) >= int(no_cursor_price):
        product_zero = driver.find_element(By.XPATH,'//*[@id="product0"]')
        product_zero.click()
        time.sleep(1)

