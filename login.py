from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from parsel import Selector
import time
from bs4 import BeautifulSoup
import links as L


####Database Code
import mysql.connector


db_connection = mysql.connector.connect(
host="localhost",
user="root",
passwd="",
database="recruitai"
)
my_database = db_connection.cursor()

def insertDB(name, location, skills, exp, about, title):
    print("INSERTING INTO DB")
    sql = "INSERT INTO `profiles`( `name`, `location`, `skills`, `exp`, `about`, title) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (name, location, skills, exp, about, title)
    my_database.execute(sql, val)

    db_connection.commit()

# init_DB()

####DB Code End


driver = webdriver.Chrome()   
email="codeadventurebot@gmail.com"
password="codeadventurebot"
driver.get("https://www.linkedin.com/login")
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
email_elem = driver.find_element_by_id("username")
email_elem.send_keys(email)
password_elem = driver.find_element_by_id("password")
password_elem.send_keys(password)
driver.find_element_by_tag_name("button").click()
count=0

for link in L.links[0]:
    try:
        f = open("MyFile"+str(count)+".txt","a+")
        print(link)
        driver.get(link)
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "profile-nav-item")))
        source=driver.page_source
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "profile-nav-item")))
        driver.execute_script("window.scrollTo(0, 1300);")
        time.sleep(10)

        print("waited")
        time.sleep(5)
        string = source
        soup = BeautifulSoup(string, 'html.parser')
        img = soup.findAll("img", {"class": "pv-top-card__photo"})
        profile_pic=img[0]['src']
        about =soup.findAll("p",{"class":"pv-about__summary-text"})
        about_data=[]
        for e in about[0]:
            try:
                about_data.append(e.text.strip())
                if '...' in e.text :
                    break
            except:
                continue

        print(about_data)
        main_about_string=""
        if(len(about_data>0)):
            for e in about_data:
                main_about_string=main_about_string+e
        #insert main_about_sting in db
        #exp data
        expdiv =soup.find("div",{"class":"pv-profile-section-pager ember-view"})
        section=expdiv.find("section",{"class":"pv-profile-section"})
        a=section.find("ul").findAll("li")
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
        print(expdata)
        main_exp_data=""
        for d in expdata:
            #f.write(d)
            main_exp_data=main_exp_data+d.strip()
        #insert this in db^
        


        intro=soup.find("div",{"class":"flex-1 mr5"})
        name=intro.ul.li.text.strip()
        title=intro.h2.text.strip()
        ul=intro.findAll("ul")
        location=ul[1].li.text.strip()
        print(name,title,location)
        f.write(name)
        #insert name in db
        f.write(title)
        #insert title in db
        f.write(location)
        #insert loc in db
        sel=Selector(text=driver.page_source)
        skills = sel.xpath('//*[@class="pv-skill-category-entity__name-text t-16 t-black t-bold"]/text()').extract()
        print(skills)
        skills_string = ""

        for s in skills:
            f.write(s.strip())
            skills_string=skills_string+s
        count+=1
        insertDB(name, loc, skills_string, main_exp_data, main_about_string, title)
    except:
        continue
    
    
    