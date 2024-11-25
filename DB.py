from  selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import mysql.connector


def main():
    
    bands = [
        "APPLE",
        "ASUS",
        "MSI",
        "ACER",
        "HP",
        "DELL",
        "GIGABYTE",
        "MICROSOFT",
    ]
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=option)
    
    
    driver.get("https://24h.pchome.com.tw/search/")
    
    
    
    search_box = driver.find_element(By.ID,"keyword")
    time.sleep(1)
    
    for brand in bands:
        search_box.clear()
        time.sleep(1)
        search_box.send_keys(brand + "筆記型電腦")
        time.sleep(1)
    
        search_box.send_keys(Keys.ENTER)
        time.sleep(1)
        
    
        body = driver.find_element(By.TAG_NAME,"body")
        for i in range(10):
            time.sleep(0.5)
            body.send_keys(Keys.PAGE_DOWN)
            
        ItemContainer = driver.find_element(By.ID,"ItemContainer")
        name = ItemContainer.find_elements(By.CLASS_NAME,"prod_name")
        description = ItemContainer.find_elements(By.CLASS_NAME,"nick")
        price = ItemContainer.find_elements(By.CSS_SELECTOR,".price.value")
        
        if len(name)==len(description)==len(price):
            data = [(brand,n.text,d.text,p.text)for n,d,p in zip(name,description,price)]
            execute_query(data)
        else:
            print('DATA ERROR:項目'+brand+'錯誤')
            continue
def execute_query(data):
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "mydb"
    )
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS notebook(
        id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
        brand VARCHAR(255) NOT NULL,
        name VARCHAR(255) NOT NULL,
        description LONGTEXT NOT NULL,
        price INT(10) NOT NULL)''')
    sql = "INSERT INTO notebook(brand,name,description,price)VALUES(%s,%s,%s,%s)"
    cursor.executemany(sql,data)
    conn.commit()
    cursor.close()
    conn.close()
if __name__ == '__main__':
    main()        