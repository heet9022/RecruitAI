from pyresparser import ResumeParser
import os
import glob

os.chdir('resumes')
ls_files=os.listdir()
#get files from folder
#print(os.listdir('/resumes')) 
main_dict=[]
for f in ls_files:
    print(f)
    data = ResumeParser(f).get_extracted_data()
    name=data['name']
    about=' College: '+str(data['college_name'])+' Degree: '+str(data['degree'])+' mobile number: '+str(data['mobile_number'])
    skills=[]
    for element in data['skills']:
        skills.append(element)
    location="mumbai maharashtra"
    dic={}
    #dic['id'] = x[0]
    dic['name'] = name
    dic['location'] = location

    dic['skills'] = skills

    dic['experience'] = ""
    dic['about'] = about
    dic['title'] = data['degree']

    # for key, value in dic.items:
    #     if value == 'None':
    #         dic[key] = ""

    main_dict.append(dic)
    #dic['image-url'] =x[7]

    
