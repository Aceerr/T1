from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Chrome()
driver.get('https://vnexpress.net/')
article = driver.find_elements(By.CSS_SELECTOR, 'article.item-news')
for ar in article:
    try:
        text = ar.find_element(By.TAG_NAME, 'h3').text
        print(text)
        print('')
        print('▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀')
    except NoSuchElementException:
        print('Lmao')
driver.close()

