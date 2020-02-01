from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()   
email="dama.dj@somaiya.edu"
password="deepcr7dama"
driver.get("https://www.linkedin.com/login")
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
email_elem = driver.find_element_by_id("username")
email_elem.send_keys(email)
password_elem = driver.find_element_by_id("password")
password_elem.send_keys(password)
driver.find_element_by_tag_name("button").click()
driver.get("https://www.linkedin.com/in/heet-sakaria/")
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "profile-nav-item")))
source=driver.page_source
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "profile-nav-item")))
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(30)
showmore = driver.find_elements_by_xpath("//*[contains(text(), 'Show more')]")
print(showmore)
#showmore.click()
#print("waiting")
#element = driver.find_element_by_class_name(str1)
#print(element)
#element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ClassName, str1)))
#driver.findElement(By.className(str1)).click()
print("waited")
#print(source)
file2 = open(r"MyFile2.txt","w+") 
file2.write(source)