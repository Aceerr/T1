from selenium import webdriver
from selenium.webdriver.common.by import  By
drive = webdriver.Chrome()
drive.get('https://www.conferenceseries.com/past-conference-reports.php')
drive.implicitly_wait(10)
print(drive.find_element(By.CLASS_NAME, 'location-conf-main').text)