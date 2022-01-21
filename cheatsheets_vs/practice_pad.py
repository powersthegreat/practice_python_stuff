from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.google.com/")

search_bar = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
search_bar.send_keys("Tesla")
search_bar.send_keys(Keys.ENTER)

driver.implicitly_wait(2)

cybertruck_link = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/table/tbody/tr[2]/td[2]/div/h3/a').click()
driver.implicitly_wait(2)
order_now_link = driver.find_element_by_xpath('//*[@id="tesla-hero-showcase-991"]/div[2]/div[2]/div/a').click()
driver.implicitly_wait(5)
buy_now_link = driver.find_element_by_class("tds-btn tds-btn--full tds-btn--outline")
click_buy_now = driver.move_to_element(buy_now_link).click()


driver.implicitly_wait(2)
first_name_input = driver.find_element_by_xpath('//*[@id="FIRST_NAME"]')
first_name_input.send_keys("William")
last_name_input = driver.find_element_by_xpath('//*[@id="LAST_NAME"]')
driver.implicitly_wait(2)
driver.back()
driver.back()
driver.back()
driver.close()l