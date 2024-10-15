import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class test_menu_admin:

    url_admin = 'https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers'

    def __init__(self, driver):
        self.driver=driver

    def test_is_url_admin(self):
        return self.driver.current_url==self.url_admin

    def test_click_admin(self):
        self.driver.find_element(By.XPATH, "//a[.//span[text()='Admin']]").click()

    def test_seleciona_filtro(self):

        exibe_filtro = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'oxd-select-text')]"))
        )

        exibe_filtro.click()

        filtro = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'oxd-select-dropdown')]"))
        )

        opcao = filtro.find_elements(By.XPATH, ".//div[text()='Admin']")

        if opcao:
            opcao[0].click()
        else:
            print("Opção Admin não encontrada.")

    def test_filtra(self):
        self.driver.find_element(By.CSS_SELECTOR, "button.oxd-button[type='submit']").click()

    def test_valida(self):
        coluna_user_role = self.driver.find_elements(By.XPATH, "//div[@class='oxd-table-cell oxd-padding-cell' and contains(@role, 'cell')]//div")

        for itens in coluna_user_role:
            assert itens.text == "Admin", f'Valor encontrado: {itens.text}, esperado: Admin'
