import time
from selenium import webdriver
from selenium.webdriver.common.by import By
class test_1:
    url_demo='https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    driver = webdriver.Chrome()  # chamo o browser numa variável...o Driver é o controlador do Selenium
    driver.get(url_demo)
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR,'[placeholder="Username"]').send_keys('Admin')
    driver.find_element(By.CSS_SELECTOR,'[placeholder="Password"]').send_keys('admin123')
    driver.find_element(By.CSS_SELECTOR,'#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div.oxd-form-actions.orangehrm-login-action > button').click()
    time.sleep(2)
    driver.quit()
    #consegui fazer o LOGIN
















