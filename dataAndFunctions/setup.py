from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dataAndFunctions.links import linkes
from pages.login import login

class Setup(login):

    Options = Options()
    Options.headless = True
    driver = webdriver.Chrome(options=Options)
    driver.implicitly_wait(10)
    driver.get(linkes.login)


