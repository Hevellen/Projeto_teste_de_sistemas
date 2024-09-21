from datetime import time
from selenium import webdriver
from selenium.webdriver.common.by import By
class test_1:
    url_demo='https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    driver = webdriver.Chrome()  # chamo o browser numa variável...o Driver é o controlador do Selenium
    driver.get(url_demo)
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,'[placeholder="Username"]').send_keys('Admin')








