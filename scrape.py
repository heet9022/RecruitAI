from bs4 import BeautifulSoup



f = open("MyFile2.txt","r")
string = f.read()
soup = BeautifulSoup(string, 'html.parser')
img = soup.findAll("img", {"class": "pv-top-card__photo"})
profile_pic=img[0]['src']
about =soup.findAll("p",{"class":"pv-about__summary-text"})
about_data=[]
for e in about[0]:
    try:
        ls.append(e.text.strip())
        if '...' in e.text :
            break
    except:
        continue

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

intro=soup.find("div",{"class":"flex-1 mr5"})
name=intro.ul.li.text.strip()
title=intro.h2.text.strip()
ul=intro.findAll("ul")
location=ul[1].li.text.strip()
print(name,title,location)
