from distutils.log import log
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from openpyxl import Workbook

#using service method
ser = Service("C:\\Users\\sonuc\\Downloads\\Compressed\\chromedriver.exe")
driverr= webdriver.Chrome(service=ser)

#maximize window
driverr.maximize_window()


#geting URL
driverr.get("https://www.amazon.in/")
driverr.implicitly_wait(5)

#using element by xpath   id="twotabsearchtextbox"   //*[@id="p_89/Samsung"]/span/a/span

SearchBox = driverr.find_element(By.ID, "twotabsearchtextbox")

SearchBox.send_keys("Android phone")

# click on search buttion 

SearchBox = driverr.find_element(By.XPATH, "//*[@id='nav-search-submit-button']")

SearchBox.click()

#import time 
# time.sleep(1)

# clicking on samsung filter   //span[contains(@class, 'a-size-medium a-color-base a-text-normal')]

filter = driverr.find_element(By.XPATH, "//*[@id='p_89/Samsung']/span/a/span")

filter.click()

# fatching Phone result

PhoneResult = driverr.find_elements(By.XPATH, "//span[contains(@class, 'a-size-medium a-color-base a-text-normal')]")
# print(PhoneResult.text)

# fatching Phone Price result 

Price_Result = driverr.find_elements(By.XPATH, "//span[contains(@class, 'price-whole')]")
# print(Price_Result.text)

phone_data = []
price_data = []


for phone in PhoneResult:
    # print(phone.text)
    phone_data.append(phone.text)


print("*"*50)

for price in Price_Result:
    # print(price.text)
    price_data.append(price.text)


# ziping both list
final_list = zip(phone_data, price_data)

wb = Workbook()
wb["Sheet"].title = 'Samsung Data'
# grab the active worksheet
sheet1 = wb.active
sheet1.append(['Phone Data', 'Price'])

for dataa in list(final_list):
    # print(dataa)
    
    with open('readme.txt', 'a') as f:
        f.write('\n'.join(dataa))

    # creating Excel file

    
    sheet1.append(dataa)

    # Save the file
    wb.save("Phone_price_data.xlsx")

# driverr.get_screenshot_as_png('savee')
driverr.get_screenshot_as_file("Amazon.png")
driverr.quit()    



