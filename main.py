from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import time

check = time.time() + 5
timeout = time.time() + 60*5

service = Service("C:\\Users\SOMA\Music\chromeDriver\chromedriver.exe")
options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

driver.get('http://orteil.dashnet.org/experiments/cookie/')
cookie = driver.find_element(By.ID,'cookie')
money = driver.find_element(By.ID,'money')


# i = True
# while i == True:
cookie.click()
upgrade_list = driver.find_elements(By.ID,'store')
# for i in range(0,len(upgrade_list)):
#     # print(upgrade_list[i].text.split(' -'))
#     upgrade_list[i]

upgrade_list_text = []
for i in upgrade_list:
    upgrade_list_text.append(i.text)
print(upgrade_list_text)


# upgrade_list_without_description = []
# for i in range(0,len(upgrade_list)):
#     upgrade_list_without_description.append(upgrade_list[i+1])
#
#

