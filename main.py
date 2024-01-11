from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Chrome()
driver.get('https://www.conferenceseries.com/past-conference-reports.php')
header = driver.find_elements(By.TAG_NAME, 'h2')
article = driver.find_elements(By.CSS_SELECTOR, 'beatmapsets_item')
driver.implicitly_wait(15)
for ar in article:
    try:
        text = ar.find_element(By.CSS_SELECTOR,'a').get_attribute('href')
        print(text)
        print('')
    except NoSuchElementException:
        print('Lmao')
driver.close()
