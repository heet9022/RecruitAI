import csv
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from parsel import Selector
from selenium import webdriver

driver=webdriver.Chrome('C:/webdrivers/chromedriver')
driver.get("https://www.google.com")
search_query=driver.find_element_by_name('q')
sleep(0.5)
search_query.send_keys('site:linkedin.com/in/ AND "python developer"')
search_query.send_keys(Keys.RETURN)
# url = driver.find_element_by_css_selector('.g a').get_attribute('href')
#links = [x.get_attribute('href') for x in driver.find_elements_by_css_selector('.g a')]
links = []
count=0
while(count<1):
    next_pg = driver.find_element_by_class_name('pn')
    next_pg.send_keys(Keys.RETURN)
    p = [x.get_attribute('href') for x in driver.find_elements_by_css_selector('.g a')]
    links.append(p)
    sleep(1)
    count+=1
#print(links)
