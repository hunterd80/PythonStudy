from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from datetime import date
import pyautogui
import time

options = Options()
options.add_experimental_option('detach', True)

chrome_driver = ChromeDriverManager().install()
#print(chrome_driver)

driver = webdriver.Chrome(service=Service(chrome_driver), options=options)
url = 'https://www.millie.co.kr/'

#크롬브라우져 열기 
driver.get(url)
driver.maximize_window()


#스크린샷
time.sleep(1)
pyautogui.screenshot('C:\\Users\\user\\Downloads\\'+str(date.today())+'_메인.png') 

#메인페이지(미로그인)_로그인 클릭
driver.find_element(By.CSS_SELECTOR,"[class='brand-login']").click()


#로그인 페이지
#스크린샷
time.sleep(1)
pyautogui.screenshot('C:\\Users\\user\\Downloads\\'+str(date.today())+'_로그인.png') 


# ID/PW 입력 후 로그인



#메인 페이지(로그인)


#action = ActionChains(driver)


#driver.find_element(By.CSS_SELECTOR,"[class='gb_za gb_jd gb_Ld gb_ie']").click()
#driver.find_element(By.LINK_TEXT,"로그인")
   
# class="gb_za gb_jd gb_Ld gb_ie" 클래스 명