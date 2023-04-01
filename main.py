from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import time

check = time.time() + 10




service = Service("C:\\Users\SOMA\Music\chromeDriver\chromedriver.exe")
options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

driver.get('http://orteil.dashnet.org/experiments/cookie/')
cookie = driver.find_element(By.ID,'cookie')

i = True
while i:
    if time.time() > check:
        print('in if statement')
        money = driver.find_element(By.ID, 'money')
        my_money = int(money.text)
        upgrades = driver.find_element(By.ID, 'store')
        upgraded_list = upgrades.find_elements(By.TAG_NAME, 'div')
        upgrade_list_name_price = []
        upgrade_list_price_only = []
        upgrade_list_name_only = []
        new_dict = {}

        for i in upgraded_list:
            upgrade_list_name_price.append(i.text.split('\n')[0])
        upgrade_list_name_price.pop()
        for i in upgrade_list_name_price:
            upgrade_list_name_only.append(i.split(' ')[0])
        for i in upgrade_list_name_price:
            upgrade_list_price_only.append(int(i.split(' ')[-1].replace(',', '')))
        new_dict = dict(zip(upgrade_list_name_only, upgrade_list_price_only))
        for i in new_dict:
            if my_money >= new_dict[i]:
                upgrade = driver.find_element(By.ID, f'buy{i}')
                upgrade.click()
        count = time.time()
    else:
        cookie.click()






