#libraries
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv

#eviroments
load_dotenv()
PATH=os.getenv('RUTA')
print(PATH)
CORREO=os.getenv('CORREO')
PASSWORD=os.getenv('PASSWORD')

KEYWORD="supervisor"

SELECTORS = {
    "ACCEDER": "button.MuiButtonBase-root.MuiButton-root.MuiButton-contained",
    "INGRESAR": "button.MuiButtonBase-root.MuiButton-root.MuiButton-outlined.jss214",
    "CORREO": "input[name='login']",
    "CONTINUAR": "div.jss212 > button",
    "INPUT": "div.jss212 > div.MuiFormControl-root > div",
    "PASSWORD":"input[type='password']",
    "KEYWORD":"input[type='text']",
    "POSTULAR": "div.MuiGrid-root.MuiGrid-container button",
    "USER": "span.MuiTypography-root.MuiCardHeader-subheader"
}

def select(page, selector):
    return page.find_element_by_css_selector(css_selector=selector)

def Login(page):
    select(page, SELECTORS["ACCEDER"]).click()
    select(page, SELECTORS["INGRESAR"]).click()
    select(page, SELECTORS["CORREO"]).send_keys(CORREO)
    select(page, SELECTORS["CONTINUAR"]).click()
    select(page, SELECTORS["INPUT"]).click()
    time.sleep(1)
    select(page, SELECTORS["PASSWORD"]).send_keys(PASSWORD)
    select(page, SELECTORS["CONTINUAR"]).click()

    return True

def Postular(page):
    select(page, SELECTORS["KEYWORD"]).send_keys(KEYWORD, Keys.ENTER)
    time.sleep(5)
    select(page, SELECTORS["POSTULAR"]).click()
    time.sleep(5)
    return select(page,SELECTORS["USER"]).text
    

driver = webdriver.Chrome(PATH)
driver.get("https://laborum.pe/")
successLogin = Login(driver)
if successLogin:
    email=Postular(driver)
    print(email)
    assert email == CORREO, "No se ha realizado todos pasos"

driver.close()