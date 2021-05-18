from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from parsel import Selector
from bs4 import BeautifulSoup
from itertools import cycle
from selenium.common.exceptions import NoSuchElementException
# from database_module import DatabaseConnector

import json
import time
import link_generator
import proxy_generator
import traceback
import re
import logging
import threading
import numpy as np

chrome_settings = Options()
# db = DatabaseConnector()


class LinkedinScraper:

    def __init__(self, email, password, category):
        super().__init__()

        self.email = email
        self.password = password
        self.category = category
        self.count = 1

        logging.basicConfig(
            handlers=[logging.FileHandler(
                './Logs/scraper.log', 'w', 'utf-8')],
            format = ': %(asctime)s : %(levelname)s : %(message)s : ',
        )

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        self.links = link_generator.generate(self.category)
        self.proxy = proxy_generator.get_proxy()
        self.scrapedData = []

        try:
            prox = Proxy()
            prox.proxy_type = ProxyType.MANUAL
            prox.http_proxy = self.proxy
            capabilities = webdriver.DesiredCapabilities.CHROME
            prox.add_to_capabilities(capabilities)
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_settings, desired_capabilities=capabilities)

        except Exception as e:
            self.logger.critical("Driver Error: " + str(e))

        # self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_settings)

    def openLinkedin(self):

        self.logger.info("Logging into Linkedin....................")

        try:
            self.driver.get("https://www.linkedin.com/login")
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
            email_element = self.driver.find_element_by_id("username")
            email_element.send_keys(self.email)
            password_element = self.driver.find_element_by_id("password")
            password_element.send_keys(self.password)
            self.driver.find_element_by_tag_name("button").click()

        except Exception as e:
            self.logger.critical("Error: " + str(e))

    def scrape(self):

    
        for link in self.links:

            profile_pic = ''
            about = ''
            main_exp_data = ''
            name = ''
            title = ''
            location = ''
            skills = ''

            data_profile = {}
            data_profile['category'] = self.category
            self.logger.info("Profile #"+str(self.count))
            try:

                data_profile['URl'] = link
                self.driver.get(link)
                self.logger.info("Waiting for page to completely load.................")
                try:
                    element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "profile-nav-item")))
                except Exception as e:
                    self.logger.error(str(e))

                time.sleep(5)

                y_coord = 500
                for i in range(5):
                    self.driver.execute_script("window.scrollTo(0, " + str(y_coord) + ");")
                    time.sleep(2)
                    y_coord += 500

                source = self.driver.page_source

            except Exception as e:
                self.logger.error("Error while waiting " + str(e))

            self.logger.info("..................Page loaded")

            time.sleep(1)

            # Profile Picture and About data

            soup = BeautifulSoup(source, 'html.parser')

            try:
                image = soup.findAll("img", {"class": "pv-top-card__photo"})
                profile_pic = image[0]['src']

            except NoSuchElementException as e:
                self.logger.warn(str(e))

            except Exception as e:
                self.logger.error("Error while scraping Profile Picture: " + str(e))

            data_profile['image_url'] = profile_pic

            try:
                about_elements = soup.findAll("p", {"class": "pv-about__summary-text"})

                for element in about_elements[0].children:
                    try:
                        if '...' in element.text:
                            break
                        about = about + element.text.strip()

                    except:
                        continue

            except (NoSuchElementException, IndexError) as e:
                self.logger.warn(str(e))

            except Exception as e:
                self.logger.error("Error while scraping About: " + str(e))

            data_profile['about'] = about

            # Experience data

            try:
                experience_div = soup.find("div", {"class": "pv-profile-section-pager ember-view"})
                experience_section = experience_div.find("section", {"class": "pv-profile-section"})
                lists = experience_section.find("ul").findAll("li")

            except NoSuchElementException as e:
                self.logger.warn(str(e))

            except Exception as e:
                self.logger.error("Error while scraping Experience " + str(e))
                lists = []

            exp = []
            for element in lists:
                data = element.text
                if(data == "/n"):
                    continue
                else:
                    exp.append(data)

            expdata = []
            for element in exp:
                ls = element.splitlines()
                for str1 in ls:
                    if(str1.isspace() or str1 == '' or str1.strip() == 'see more' or str1 == '...'):
                        continue
                    else:
                        main_exp_data = main_exp_data + str1.strip()

            main_exp_data = re.sub('•', '', main_exp_data)
            main_exp_data = re.sub('  ', '', main_exp_data)
            data_profile['experience'] = main_exp_data

            # Name, Title, Location
            try:
                intro = soup.find("div", {"class": "flex-1 mr5"})
                name = intro.ul.li.text.strip()
                title = intro.h2.text.strip()
                ul = intro.findAll("ul")
                location = ul[1].li.text.strip()

            except NoSuchElementException as e:
                self.logger.warn(str(e))

            except Exception as e:
                self.logger.error(
                    "Error while scraping name, title, location " + str(e))

            data_profile['name'] = name
            data_profile['title'] = title
            data_profile['location'] = location

            try:
                try:
                    self.driver.find_element_by_xpath("//button[@class='pv-profile-section__card-action-bar pv-skills-section__additional-skills artdeco-container-card-action-bar artdeco-button artdeco-button--tertiary artdeco-button--3 artdeco-button--fluid']").click()

                except NoSuchElementException as e:
                    self.logger.warn(str(e))

                except Exception as e:
                    self.logger.error("Error: " + str(e))

                sel = Selector(text=self.driver.page_source)

                skills = str(sel.xpath('//*[@class="pv-skill-category-entity__name-text t-16 t-black t-bold"]/text()').extract())

                skills = re.sub('\n', '', skills)
                skills = re.sub('  ', '', skills)

                data_profile['skills'] = skills

            except NoSuchElementException as e:
                self.logger.warn(str(e))

            except Exception as e:
                self.logger.error("error in skills " + str(e))

            self.logger.info(str(data_profile))

            if (data_profile['about'] == '' and data_profile['experience'] == '' and data_profile['skills'] == ''):
                self.logger.critical("Scraper has stopped working for some reason. Please check logs. \n You should also check "+data_profile['URl'])
                exit()

            # db.insertDB(data_profile['category'], data_profile['URl'], data_profile['image_url'], data_profile['about'],
            #             data_profile['experience'], data_profile['name'], data_profile['title'], data_profile['location'], data_profile['skills'])
            self.count += 1
            self.scrapedData.append(data_profile)

    def start(self):

        self.openLinkedin()
        self.scrape()
        self.driver.quit()
        self.logger.info("Scraping completed for " + self.category)

class Batch:

    def __init__(self, subcategories, account):
        super().__init__()
        self.subcategories = subcategories
        self.account = account

    def runBatch(self):

        for subcategory in self.subcategories:
            linkedinscraper = LinkedinScraper(self.account['email'], self.account['password'], subcategory)
            linkedinscraper.start()

if __name__ == "__main__":

    f = open('linkedin_credentials.json')
    data = json.load(f)
    accounts = data["accounts"]

    categories = ['Cloud Engineer', 'Data Scientist', 'Web Developer']

    no_of_batches = 1

    if no_of_batches <= len(categories):

        for index, subcategories in enumerate(np.array_split(np.array(categories), no_of_batches)):

            account = accounts[(index) % len(accounts)]
            batch = Batch(subcategories.tolist(), account)
            threading.Thread(target=batch.runBatch).start()
    else:
        print("Number of batches should be less than the list")
