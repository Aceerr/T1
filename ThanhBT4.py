from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome(executable_path='.venv/chromedriver.exe')
driver.get('https://www.facebook.com/')
try:
    driver.find_element(By.XPATH, "//*[text()='Create new account']").click()
    driver.implicitly_wait(20)
    driver.find_element(By.NAME, "firstname").send_keys("Thanh")
    driver.find_element(By.NAME, "lastname").send_keys("Tran")
    driver.find_element(By.NAME, "reg_email__").send_keys("Thanh99916354564@email.com")
    driver.implicitly_wait(10)
    driver.find_element(By.NAME, "reg_email_confirmation__").send_keys("Thanh99916354564@email.com")
    driver.find_element(By.NAME, "reg_passwd__").send_keys("P@ssW0rd")
    ngay = Select(driver.find_element(By.NAME, "birthday_day"))
    ngay.select_by_visible_text("19")
    thang = Select(driver.find_element(By.NAME, "birthday_month"))
    thang.select_by_visible_text("Dec")
    nam = Select(driver.find_element(By.NAME, "birthday_year"))
    nam.select_by_visible_text("2003")
    driver.find_element(By.XPATH, "//label[text()='Male']").click()

    driver.find_element(By.NAME, "websubmit")

except Exception as ex:
    print(ex)
driver.close()
