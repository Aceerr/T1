from selenium import webdriver
from selenium.webdriver.common.by import  By
driver = webdriver.Chrome()
driver.get('https://www.google.com/')
str = input('Nhap du dieu can tim: ')
driver.implicitly_wait(10)
cosn = driver.find_element(By.NAME,'q')
cosn.send_keys(str)
cosn.submit()
result = driver.find_elements(By.CSS_SELECTOR,'div.g')
for re in result:
    text = re.find_element(By.CSS_SELECTOR,'a').text
    link = re.find_element(By.CSS_SELECTOR,'a').get_attribute('href')
    img = re.find_element(By.CSS_SELECTOR,'')
    print(text)
    print(link)
    print('▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀')
driver.close()