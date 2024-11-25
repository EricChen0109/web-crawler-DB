from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys
import time

sys.stdout.reconfigure(encoding='utf-8')

option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=option)

url = "https://24h.pchome.com.tw/"
driver.get(url)

search_box = driver.find_element(By.CSS_SELECTOR,".c-search_input")

search_box.send_keys("macbook air")
time.sleep(1)

search_box.send_keys(Keys.ENTER)
time.sleep(1)


titles = driver.find_elements(By.CLASS_NAME,"prod_name")

list = []
for i in titles:
    list.append(i.text)

print(list)


