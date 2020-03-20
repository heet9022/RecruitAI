from pyresparser import ResumeParser
import os
import json

os.chdir('Data/resumes')
ls_files = os.listdir()

relevant_dataset = []
raw_dataset = []
for f in ls_files:

    print("...........Processing....... "+f)
    raw_data = ResumeParser(f).get_extracted_data()
    raw_dataset.append(raw_data)

    relevant_data = {}

    relevant_data['name'] = raw_data['name']
    relevant_data['email'] = raw_data['email']
    relevant_data['mobile_number'] = raw_data['mobile_number']
    skills = []
    for element in raw_data['skills']:
        skills.append(element)
    relevant_data['skills'] = skills

    relevant_dataset.append(relevant_data)

print("...........Writing to Json....... "+f)

# with open('relevant_dataset.json', 'w') as fp:
#     json.dump(relevant_dataset, fp)
# with open('raw_dataset.json', 'w') as fp:
#     json.dump(raw_dataset, fp)
