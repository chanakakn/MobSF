#!/usr/bin/env python3
import os
import sys
import requests
import argparse
import time
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder

FILE = str(sys.argv[1])
SERVER = str(sys.argv[2])
APIKEY = str(sys.argv[3])
ACTION = str(sys.argv[4])

def upload():
    try:
        """Upload File"""
        print("Uploading file")
        multipart_data = MultipartEncoder(fields={'file': (FILE, open(FILE, 'rb'), 'application/octet-stream')})
        headers = {'Content-Type': multipart_data.content_type, 'Authorization': APIKEY}
        response = requests.post(SERVER + '/api/v1/upload', data=multipart_data, headers=headers)
        print(response.text)
        return response.text      

    except Exception as e:
        print(e)  


def scan(data):
    try:
        """Scan the file"""
        print("Scanning file")
        post_dict = json.loads(data)
        headers = {'Authorization': APIKEY}
        response = requests.post(SERVER + '/api/v1/scan', data=post_dict, headers=headers)
        print(response.text)      

    except Exception as e:
        print(e)      


def pdf(data):
    try:
        """Generate PDF Report"""
        print("Generate PDF report")
        headers = {'Authorization': APIKEY}
        data = {"hash": json.loads(data)["hash"]}
        response = requests.post(SERVER + '/api/v1/download_pdf', data=data, headers=headers, stream=True)
        with open("report.pdf", 'wb') as flip:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    flip.write(chunk)
                    print("Report saved as report.pdf")     

    except Exception as e:
        print(e)      


def json_resp(data):
    try:
        """Generate JSON Report"""
        print("Generate JSON report")
        headers = {'Authorization': APIKEY}
        data = {"hash": json.loads(data)["hash"]}
        response = requests.post(SERVER + '/api/v1/report_json', data=data, headers=headers)
        with open("report.json", "a") as flip:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    flip.write(chunk)
                    print("Report saved as report.json")
                    print(response.text)
              
    except Exception as e:
        print(e)      


def delete(data):
    try:
        """Delete Scan Result"""
        print("Deleting Scan")
        headers = {'Authorization': APIKEY}
        data = {"hash": json.loads(data)["hash"]}
        response = requests.post(SERVER + '/api/v1/delete_scan', data=data, headers=headers)
        print(response.text)     

    except Exception as e:
        print(e)      


def main():
    try:
        if (ACTION == 'upload'):
            RESP = upload() 
            
        elif (ACTION == 'scan'):
            scan(upload())    
            
        elif (ACTION == 'json'):
            json_resp(upload())
            
        elif (ACTION == 'pdf'):
            pdf(upload())
            
        elif (ACTION == 'delete'):
            delete(upload())        
          
    except Exception as e:
        print(e)       

if __name__ == "__main__":
    main()
