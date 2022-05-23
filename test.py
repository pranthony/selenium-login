import os
import time
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

from selectors import SELECTORS

PATH=os.getenv('RUTA')


class TestLaborum(unittest.TestCase):
     
    def setUp(self):
        self.driver = webdriver.Chrome(PATH)
        self.driver.implicitly_wait(5)
        self.wait = WebDriverWait(self.driver, 5)

        self.CORREO = os.getenv("CORREO")
        self.PASSWORD = os.getenv("PASSWORD")
        self.KEYWORD = "FULLSTACK"
    
    def test_in_laborum(self):
        self.driver.get("https://laborum.pe/")
        self.login()
        correo = self.postular()
        print(correo)
        self.assertIn(self.CORREO, correo)

    def login(self):
        self.select_xpath(SELECTORS["ACCEDER"]).click()
        self.select_xpath(SELECTORS["INGRESAR"]).click()
        self.select_xpath(SELECTORS["FORM"]).send_keys(self.CORREO)
        self.select_xpath(SELECTORS["CONTINUAR"]).click()
        self.select_xpath(SELECTORS["INPUT"]).click()
        time.sleep(0.5)
        self.select_xpath(SELECTORS["FORM"]).send_keys(self.PASSWORD)
        self.select_xpath(SELECTORS["CONTINUAR"]).click()

    def postular(self):
        self.select_xpath(SELECTORS["KEYWORD"]).send_keys(self.KEYWORD, Keys.ENTER)
        self.select_xpath(SELECTORS["POSTULAR"]).click()
        return self.select_xpath(SELECTORS["USER"]).text
        

    def select_xpath(self, selector):
        return self.driver.find_element(By.XPATH,selector)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()