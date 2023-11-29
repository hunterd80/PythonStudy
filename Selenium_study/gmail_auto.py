from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time


driver = webdriver.Chrome()
url = 'https://google.com'
driver.get(url)
driver.maximize_window()

time.sleep(1)

action = ActionChains(driver)


driver.find_element(By.CSS_SELECTOR,"[class='gb_za gb_jd gb_Ld gb_ie']").click()
#driver.find_element(By.LINK_TEXT,"로그인").click
   
# class="gb_za gb_jd gb_Ld gb_ie" 클래스 명