# from firebase import firebase  
# firebase = firebase.FirebaseApplication('https://recruitai-27ea6.firebaseio.com/', None)  
# data =  { 'Name': 'Vivek',  
#           'RollNo': 1,  
#           'Percentage': 76.02  
#           }  
# result = firebase.post('/recruitai-27ea6/Profiles/',data)  
# print(result) 


#!/usr/bin/env python
import argparse
import json
import sys
import requests
import pyrebase

def die(message, status=1):
    sys.stderr.write("Error: {}\n".format(message))
    sys.exit(status)
# end

def firebase_db_init():
    config = {
        "apiKey": "AIzaSyDkEEDaLbDmfe-TgmL1zkbBFy6abMBmbEg",
        "authDomain": "recruitai-27ea6.firebaseapp.com",
        "databaseURL": "https://recruitai-27ea6.firebaseio.com",
        "projectId": "recruitai-27ea6",
        "storageBucket": "recruitai-27ea6.appspot.com",
        "messagingSenderId": "978296144862"
    }
    # config["serviceAccount"] = '/path/to/firebase_service_key.json'

    try:
        firebase = pyrebase.initialize_app(config)
        return firebase.database()
    except Exception as e:
        die("db_init failed. {}".format(e))
    # try 
# end

def get_url(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    else:
        die("HTTP GET {} failed with status={}".format(url, r.status_code))
# end

def set_record(dbHandle, tableName, keyName, data):
    try:
        dbHandle.child(tableName).child(keyName).set(data)
    except Exception as e:
        die("set_record failed. {}".format(e))
    # try 
# end

def get_record(dbHandle, tableName, keyName):
    try:
        return dbHandle.child(tableName).child(keyName).get().val()
    except Exception as e:
        die("get_record failed. {}".format(e))
    # try
# end

def delete_record(dbHandle, tableName, keyName):
    try:
        dbHandle.child(tableName).child(keyName).remove()
    except Exception as e:
        die("delete_record failed. {}".format(e))
    # try
# end

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--table', help='name of the DB table', required=True)
    parser.add_argument('-k', '--key', help='key in the DB table', required=True)
    parser.add_argument('-a', '--action', help='type of operation', default='get', choices=['get', 'set', 'delete'])
    parser.add_argument('-u', '--url', help='url to fetch the data', required=False)

    args = parser.parse_args()

    if (args.action == 'set') and not args.url:
        die("--url <url> is mandatory for --action=set")
    # if

    dbHandle = firebase_db_init()
    if (args.action == 'set'):
        data = get_url(args.url)
        set_record(dbHandle, args.table, args.key, data)
    elif (args.action == 'delete'):
        delete_record(dbHandle, args.table, args.key)
    else:
        data = get_record(dbHandle, args.table, args.key)
        print("{}".format(json.dumps(data, indent=4, sort_keys=True)))
    # if
# end