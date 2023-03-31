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

money = driver.find_element(By.ID, 'money')
my_money = int(money.text)
upgrades = driver.find_element(By.ID, 'store')
upgraded_list = upgrades.find_elements(By.TAG_NAME, 'div')
upgrade_list_name_price = []
upgrade_list_price_only = []
for i in upgraded_list:
    upgrade_list_name_price.append(i.text.split('\n')[0])

upgrade_list_name_price.pop()
for i in upgrade_list_name_price:
    upgrade_list_price_only.append(int(i.split(' ')[-1].replace(',', '')))
if my_money >= upgrade_list_price_only[-1]:
    upgrade = driver.find_element(By.ID, '')

print(upgraded_list)
print(upgrade_list_price_only)

# i = True
# while i == True:
#     if time.time() > timeout:
#
#     else:
#         cookie.click()
#
#











# upgrade_list = []
# done = False
# i = 0
# while done == False:
#     try:
#         upgrade_list.append(driver.find_element(By.XPATH,f'/html/body/div[4]/div[5]/div/div[{i}]'))
#         i += 1
#     except:
#         done = True
# print(upgrade_list)



# for i in range(0,len(upgrade_list),2):
#     # print(upgrade_list[i].text.split(' -'))
#     # upgrade_list[i]
#     print(upgrade_list[i].text)

# upgrade_list_text = []
# for i in upgrade_list:
#     upgrade_list_text.append(i.text)
# print(upgrade_list_text)


# upgrade_list_without_description = []
# for i in range(0,len(upgrade_list)):
#     upgrade_list_without_description.append(upgrade_list[i+1])
#
#

