import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

url_demo='https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
driver = webdriver.Chrome()  # chamo o browser numa variável...o Driver é o controlador do Selenium
driver.get(url_demo)
time.sleep(3)






