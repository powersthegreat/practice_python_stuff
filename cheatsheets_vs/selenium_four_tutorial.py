from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver_path = "C:\Program Files\Webdrivers\chromedriver.exe"
serv_object = Service(driver_path)
driver = webdriver.Chrome(service = serv_object)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(1)

# <input class="oxd-input oxd-input--active" name="username" placeholder="Username" autofocus="" data-v-844e87dc="">
# <button type="submit" class="oxd-button oxd-button--medium oxd-button--main orangehrm-login-button" data-v-7e88b27e="" data-v-30b9e6c4=""><!----> Login <!----></button>

driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
time.sleep(2)

page_title = driver.title
expected_title = "OrangeHRM"
if page_title == expected_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

driver.close()