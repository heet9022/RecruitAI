import csv
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from parsel import Selector
from selenium import webdriver
from bs4 import BeautifulSoup 



no_of_pages = 1

def generate(category):

    print("Generating links.....................")
    
    driver=webdriver.Chrome()
    driver.get("https://www.google.com")
    search_query=driver.find_element_by_name('q')
    sleep(0.5)
    search_query.send_keys('site:linkedin.com/in/ AND '+category)
    search_query.send_keys(Keys.RETURN)

    links = []
    for _ in range(no_of_pages):

        soup = BeautifulSoup(driver.page_source)
        next_pg = driver.find_element_by_class_name('pn')
        next_pg.send_keys(Keys.RETURN)
        sleep(1)
        url = [x.a['href'] for x in soup.find_all("div", class_="r")]
        links.append(url)
        print(links)

    print("..................Links generated!")
    driver.quit()
    return links

if __name__ == "__main__":
    generate()