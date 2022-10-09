from distutils.log import log
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

#using service method
ser = Service("C:\\Users\\sonuc\\Downloads\\Compressed\\chromedriver.exe")
driverr= webdriver.Chrome(service=ser)

#maximize window
driverr.maximize_window()


#geting URL
driverr.get("http://43.224.136.41/")

#using element by xpath

username = driverr.find_element(By.XPATH, "//*[@id='username']")

username.send_keys("mamta545chauraamicconsultancy.in")  # ID is worng
#using element by xpath
password = driverr.find_element(By.XPATH, "//*[@id='password']")   
password.send_keys("Gy#e643%") # password is worng
#using element by xpath     
login_buttion = driverr.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form/table/tbody/tr[3]/td[2]/input[2]")
login_buttion.click()

#import time 
time.sleep(5)

# clicking drop-down after login
dropDown_buttion = driverr.find_element(By.XPATH, "//*[@id='DWT28_dropdown']")
dropDown_buttion.click()

time.sleep(5)

# click on Sign Out
selectt = (driverr.find_element(By.XPATH, '//*[@id="logOff_title"]'))  
#select.select_by_visible_text("Sign Out")
selectt.click()
# driverr.quit()

