from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from parsel import Selector
from bs4 import BeautifulSoup 
from itertools import cycle

import time
import link_generator
import proxy_generator
import traceback
import re

chrome_settings = Options()

class LinkedinScraper:

    def __init__(self, email, password, category):
        super().__init__()

        self.email = email
        self.password = password
        self.category = category
        self.links = link_generator.generate(self.category)

        proxies = proxy_generator.get_proxies()
        for proxy in proxies:
            if proxy_generator.test_proxy(proxy):
                self.proxy = proxy
                break

        try:
            prox = Proxy()
            prox.proxy_type = ProxyType.MANUAL
            prox.http_proxy = self.proxy
            capabilities = webdriver.DesiredCapabilities.CHROME
            prox.add_to_capabilities(capabilities)
            self.driver = webdriver.Chrome(chrome_options=chrome_settings, desired_capabilities=capabilities)
        except Exception as e:
            print("Driver Error: ", e)
        # self.driver = webdriver.Chrome(chrome_options=chrome_settings)
        self.scrapedData = []
    
    def openLinkedin(self):

        print("......................OpenLinkedin Started....................")

        try:
            self.driver.get("https://www.linkedin.com/login")
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
            email_elem = self.driver.find_element_by_id("username")
            email_elem.send_keys(self.email)
            password_elem = self.driver.find_element_by_id("password")
            password_elem.send_keys(self.password)
            self.driver.find_element_by_tag_name("button").click()

        except Exception as e:
            print("Error: ", e)

        

    def scrape(self):
        
        
        for page in range(link_generator.no_of_pages):
            for link in self.links[page]:

                data_profile = {}
                data_profile['category'] = self.category
                try:
                    # print("URL: ", link)
                    data_profile['URl'] = link
                    self.driver.get(link)
                    try:
                        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "profile-nav-item")))
                    except Exception as e:
                        print(e)
                    
                    time.sleep(5)
                    y_coord = 500
                    for i in range(5):
                        self.driver.execute_script("window.scrollTo(0, " + str(y_coord) + ");")
                        time.sleep(2)
                        y_coord += 500 

                    source=self.driver.page_source
                except:
                    print("Error while waiting")
                    traceback.print_exc()

                print("..................Waited for page to load.................")

                time.sleep(3)

                # Profile Picture and About data
                
                profile_pic = ""
                soup = BeautifulSoup(source, 'html.parser')
                try:
                    try:
                        see_more = self.driver.find_element_by_xpath("//a[@class='lt-line-clamp__more']")
                        self.driver.execute_script("arguments[0].click();", see_more)
                    except:
                        print("Could not expand 'See More' ")

                    img = soup.findAll("img", {"class": "pv-top-card__photo"})
                    profile_pic = img[0]['src']
                    
                except:
                    print("Error in about")
                    traceback.print_exc()

                # print("Image URL: ", profile_pic)
                data_profile['image_url'] = profile_pic
                about_data=[]

                try:
                    about = soup.findAll("p", {"class":"pv-about__summary-text"})
                    
                    for e in about[0].children:
                        try:
                            about_data.append(e.text.strip())
                            if '...' in e.text :
                                break
                        except:
                            continue
                except:
                        print("error in about in loop")
                        traceback.print_exc()

                
                main_about_string=""
                if(len(about_data)>0):
                    for e in about_data:
                        main_about_string = main_about_string + e

                # print("About: ", main_about_string)
                data_profile['about'] = main_about_string

                # Experience data
                try:
                    expdiv = soup.find("div",{"class":"pv-profile-section-pager ember-view"})
                    section = expdiv.find("section",{"class":"pv-profile-section"})
                    a = section.find("ul").findAll("li")
                except:
                    print("error in experience")
                    traceback.print_exc()
                    a=[]
                exp=[]
                for e in a:
                    data=e.text
                    if(data=="/n"):
                        continue
                    else:
                        exp.append(data)

                expdata=[]
                for e in exp:
                    ls=e.splitlines()
                    for str1 in ls:
                        if(str1.isspace() or str1=='' or str1.strip()=='see more' or str1=='...'):
                            continue
                        else:
                            expdata.append(str1.strip())
                
                main_exp_data=""
                for d in expdata:
                    main_exp_data = main_exp_data+d.strip()

                main_exp_data = re.sub('•','', main_exp_data)
                main_exp_data = re.sub('  ','', main_exp_data)       
                # print("Experience: ", main_exp_data)
                data_profile['experience'] = main_exp_data

                # Name, Title, Location
                try:
                    intro=soup.find("div",{"class":"flex-1 mr5"})
                    name=intro.ul.li.text.strip()
                    title=intro.h2.text.strip()
                    ul=intro.findAll("ul")
                    location=ul[1].li.text.strip()
                except:
                    name=""
                    title=""
                    location=""
                    print("error in name title")
                    traceback.print_exc()
                    
                # print("Name, Title, Location : ", name, title, location)
                data_profile['name'] = name
                data_profile['title'] = title
                data_profile['location'] = location

                try:
                    try:
                        self.driver.find_element_by_xpath("//button[@class='pv-profile-section__card-action-bar pv-skills-section__additional-skills artdeco-container-card-action-bar artdeco-button artdeco-button--tertiary artdeco-button--3 artdeco-button--fluid']").click()
                    except Exception as e:
                        print("Error: ", e)
                        print("Could not Expand Skills")
                    sel=Selector(text=self.driver.page_source)
                    
                    skills = sel.xpath('//*[@class="pv-skill-category-entity__name-text t-16 t-black t-bold"]/text()').extract()
                    


                    skill_array_temp = []
                    skills_str = str(skills)
                    
                    skills = re.sub('\n', '', skills_str)
                    skills = re.sub('  ', '', skills)

                    # print(skills)
                    data_profile['skills'] = skills


                except:
                    print("error in skills")
                    traceback.print_exc()
                print()
                # crud.insertDB(name, location, skills_string, main_exp_data, main_about_string, title, profile_pic)
                print(data_profile)
                self.scrapedData.append(data_profile)
                
        
        for profile in self.scrapedData:
            for item in profile:
                print (item)
            print('\n')
        
    def start(self):

        self.openLinkedin()
        self.scrape()
        self.driver.quit()
        

categories = ['HR', 'Designing', 'Managment', 'Information Technology',
       'Education', 'Advocate', 'Business Development',
       'Health & Fitness', 'Agricultural', 'BPO', 'Sales', 'Consultant',
       'Digital Media', 'Automobile', 'Food & Beverages', 'Finance',
       'Apparel', 'Engineering', 'Accountant', 'Building & Construction',
       'Architects', 'Public Relations', 'Banking', 'Arts', 'Aviation']

if __name__ == "__main__":

    for category in categories:

        email = "kjoe4773@gmail.com"
        password = "S&{%|X^(ea>Z;2o"
        obj = LinkedinScraper(email, password, category)
        obj.start()