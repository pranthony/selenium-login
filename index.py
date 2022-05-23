#libraries
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
from selectors import SELECTORS

#eviroments
load_dotenv()
PATH=os.getenv('RUTA')
CORREO=os.getenv('CORREO')
PASSWORD=os.getenv('PASSWORD')

KEYWORD="frontend"

def select(page, selector):
    return page.find_element(by=By.XPATH,value=selector)

def Login(page):
    select(page, SELECTORS["ACCEDER"]).click()
    select(page, SELECTORS["INGRESAR"]).click()
    select(page, SELECTORS["FORM"]).send_keys(CORREO)
    select(page, SELECTORS["CONTINUAR"]).click()
    select(page, SELECTORS["INPUT"]).click()
    time.sleep(0.5)
    select(page, SELECTORS["FORM"]).send_keys(PASSWORD)
    select(page, SELECTORS["CONTINUAR"]).click()
    return True

def Postular(page):
    select(page, SELECTORS["KEYWORD"]).send_keys(KEYWORD, Keys.ENTER)
    select(page, SELECTORS["POSTULAR"]).click()
    return select(page,SELECTORS["USER"]).text

driver = webdriver.Chrome(executable_path=PATH)
driver.implicitly_wait(5)
driver.get("https://laborum.pe/")

Login(driver)
Postular(driver)
print()

driver.close()