from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.chrome.options import Options
import time
# import requests

nomeEmpresa = []
servico = []
telefone = []

WINDOW_SIZE = "1500,900"
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

driver = webdriver.Chrome()

driver.get('https://www.google.com.br/maps')
time.sleep(5)

driver.find_element(By.XPATH,'//*[@id="searchboxinput"]').send_keys('comercios proximos')
driver.find_element(By.XPATH,'//*[@id="searchbox-searchbutton"]').click()

time.sleep(5)

card = driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]')

for i in range(len(card)):
    if i == 0 or i == 1:
        continue


time.sleep(15)