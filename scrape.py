from bs4 import BeautifulSoup
from nltk import tokenize

# def removesubstr(lstr,smallstr):
#     for i in range(len(lstr)):
#         b=False
#         for j in range(0,len(smallstr)):
#             if(lstr[i+j]!=smallstr):




f = open("MyFile2.txt","r")
string = f.read()
soup = BeautifulSoup(string, 'html.parser')
#print(soup.prettify())
img = soup.findAll("img", {"class": "pv-top-card__photo"})
profile_pic=img[0]['src']
about =soup.findAll("p",{"class":"pv-about__summary-text"})
#print(about[0].span.text)
about_data=[]
for e in about[0]:
    try:
        ls.append(e.text.strip())
        if '...' in e.text :
            break
    except:
        continue
#print(ls)

expdiv =soup.find("div",{"class":"pv-profile-section-pager ember-view"})
#print(expdiv)
section=expdiv.find("section",{"class":"pv-profile-section"})
a=section.find("ul").findAll("li")
exp=[]
for e in a:
   data=e.text
   if(data=="/n"):
       continue
   else:
       exp.append(data)
   #print("~~~~~~~~~~~~~~~~~~~")
#print(exp)
expdata=[]
for e in exp:
    ls=e.splitlines()
    for str1 in ls:
        if(str1.isspace() or str1=='' or str1.strip()=='see more' or str1=='...'):
            continue
        else:
            expdata.append(str1.strip())
print(expdata)


