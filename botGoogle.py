from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.chrome.options import Options
import time
# import requests

empresa = []
servico = []
telefone = []

WINDOW_SIZE = "1500,900"
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

driver = webdriver.Chrome()

driver.get('https://www.google.com.br/maps')
time.sleep(2)

driver.find_element(By.XPATH,'//*[@id="searchboxinput"]').send_keys('comercios proximos')
driver.find_element(By.XPATH,'//*[@id="searchbox-searchbutton"]').click()

time.sleep(2)

card = driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[3]/div/a')

y = 3

for i in range(13):
    # if i == 0 or i == 1:
    #     continue


    driver.find_element(By.XPATH, f'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[{y}]/div/a')

    nomeEmpresa = driver.find_element(By.XPATH, f'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[{y}]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[1]/div[2]').text
   
    y = y + 2

    empresa.append(nomeEmpresa)

    print(empresa)


time.sleep(15)