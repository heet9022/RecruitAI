from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from parsel import Selector
from selenium import webdriver
from bs4 import BeautifulSoup

import csv
import logging



no_of_pages = 5


def generate(category='Digital Media'):

    logger = logging.getLogger()

    logger.info("Generating links.....................")

    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    search_query = driver.find_element_by_name('q')
    sleep(0.5)
    search_query.send_keys('site:linkedin.com/in/ AND '+category)
    search_query.send_keys(Keys.RETURN)

    links = []
    count = 1
    for _ in range(no_of_pages):

        sleep(1)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        url = [x.a['href'] for x in soup.find_all(
            "div", class_="r") if 'linkedin' in x.a['href']]
        links.append(url)

        if(count == 1):
            next_page = soup.find_all("a", class_="G0iuSb")[0]['href']
        else:
            next_page = soup.find_all("a", class_="G0iuSb")[1]['href']

        driver.get('https://www.google.com/'+str(next_page))
        count = count + 1
        sleep(1)

    logger.info(links)
    logger.info("..................Links generated!")

    driver.quit()
    return links


if __name__ == "__main__":
    generate()
