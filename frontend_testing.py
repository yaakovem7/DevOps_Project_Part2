from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:/Utils/chromedriver_win32/chromedriver.exe")
driver.get("http://127.0.0.1:5001/get_user_name/2")

my_list = driver.find_element(By.ID,value="2").text

print(my_list)
