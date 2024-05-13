from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException
from pprint import pprint
import pandas as pd
import time

empresa = []
servico = []
telefone = []



# WINDOW_SIZE = "1500,900"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

driver = webdriver.Chrome()

driver.get('https://www.google.com.br/maps')
time.sleep(2)

driver.find_element(By.XPATH,'//*[@id="searchboxinput"]').send_keys('lojas de tenis')
driver.find_element(By.XPATH,'//*[@id="searchbox-searchbutton"]').click()

time.sleep(2)

card = driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[3]/div/a')

y = 3

for i in range(3):
    

    driver.find_element(By.XPATH, f'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[{y}]/div/a')
    nomeEmpresa = driver.find_element(By.XPATH, f'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[{y}]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[1]/div[2]').text

    
    tipoServico = driver.find_element(By.XPATH, f'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[{y}]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[4]/div[1]/span[1]/span').text

    

    try:
        numTelefone = driver.find_element(By.XPATH, f'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[{y}]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[4]/div[2]/span[2]/span[2]').text
    
    except NoSuchElementException:
        numTelefone = ""
        pass

    time.sleep(2)


    driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]').send_keys(Keys.PAGE_DOWN)

   
    y = y + 2

    empresa.append(nomeEmpresa)
    servico.append(tipoServico)
    telefone.append(numTelefone)

driver.close()
  



df = pd.DataFrame({'Empresa':empresa, 'Servico':servico, 'Telefone':telefone})
    
   

print(df.head)
df.to_excel('testeBot.xlsx')


