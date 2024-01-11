from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import  Select
import  csv
driver = webdriver.Chrome()
driver.get('https://lms.ou.edu.vn/')
(driver.find_element(By.CLASS_NAME, 'main-btn')).click()
(driver.find_element(By.CLASS_NAME, 'login100-form-btn')).click()
utype = Select(driver.find_element(By.ID,'form-usertype'))
utype.select_by_index(0)
with open('test.csv','r', newline='') as f:
    reader=csv.DictReader(f)
    for i in reader:
        user = i['user']
        password = i['password']
(driver.find_element(By.ID, 'form-username')).send_keys(user)
(driver.find_element(By.ID, 'form-password')).send_keys(password)
(driver.find_element(By.CLASS_NAME, 'm-loginbox-submit-btn')).click()
driver.implicitly_wait(15)
subjs = driver.find_elements(By.CSS_SELECTOR, '.dashboard-card .course-info-container .align-items-start a')
for s in subjs:
    print(s.text)
