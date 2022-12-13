#Automation testing https://www.saucedemo.com/ using selenium python
#Ncl.12.13.22

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#Remove product from chart         
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID,"user-name").send_keys("standard_user")   
driver.find_element(By.ID,"password").send_keys("secret_sauce") 
driver.find_element(By.ID,"login-button").click()
time.sleep(1)
driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light").click()
time.sleep(1)
driver.find_element(By.ID,"shopping_cart_container").click()    
time.sleep(2)
driver.find_element(By.ID,"remove-sauce-labs-bike-light").click()    
time.sleep(1)
driver.close()

#Success login         
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID,"user-name").send_keys("standard_user")   
driver.find_element(By.ID,"password").send_keys("secret_sauce") 
driver.find_element(By.ID,"login-button").click()  
time.sleep(2)
driver.close()

#failed login         
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID,"user-name").send_keys("lala")   
driver.find_element(By.ID,"password").send_keys("secret_sauce") 
driver.find_element(By.ID,"login-button").click()  
time.sleep(2)
driver.close()

#Add one product to chart
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID,"user-name").send_keys("standard_user")   
driver.find_element(By.ID,"password").send_keys("secret_sauce") 
driver.find_element(By.ID,"login-button").click()
time.sleep(1)
driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light").click()
time.sleep(1)
driver.find_element(By.ID,"shopping_cart_container").click()    
time.sleep(2)
driver.close()

#Test logout button        
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID,"user-name").send_keys("standard_user")   
driver.find_element(By.ID,"password").send_keys("secret_sauce") 
driver.find_element(By.ID,"login-button").click()  
driver.find_element(By.ID,"react-burger-menu-btn").click()
time.sleep(1)
driver.find_element(By.ID,"logout_sidebar_link").click()    
time.sleep(2)
driver.close()