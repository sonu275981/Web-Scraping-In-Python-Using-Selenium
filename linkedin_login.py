#from lib2to3.pgen2 import driver
from selenium import webdriver
driverr= webdriver.Chrome(executable_path="C:\\Users\\sonuc\\Downloads\\Compressed\\chromedriver.exe")

print(type(driverr))
driverr.get("https://www.google.com/")
my_page_title = driverr.title
print(my_page_title)
assert "Google" in my_page_title
driverr.quit()