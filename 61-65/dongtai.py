from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.baidu.com/')
kw_input = browser.find_element(By.ID,'kw')
kw_input.send_keys('Python')
su_button = browser.find_element(By.CSS_SELECTOR,'#su')
su_button.click()