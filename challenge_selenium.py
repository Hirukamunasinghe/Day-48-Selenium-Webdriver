from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver_service = Service(executable_path="C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)

URL ="https://www.python.org/"
driver.get(URL)


#Extracting data
event_times = driver.find_elements(By.CSS_SELECTOR,".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR,".event-widget li a")

events ={}

for n in range(0,len(event_times)):
    events[n]={
        "time": event_times[n].text,
        "name": event_names[n].text
    }

print(events)

driver.close()