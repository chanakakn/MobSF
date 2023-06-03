#!/usr/bin/env python3
import os
import requests
import argparse
import json
import logging
from requests_toolbelt.multipart.encoder import MultipartEncoder

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def upload(file_path, server_url, api_key):
    try:
        """Upload File"""
        logger.info("Uploading file")
        multipart_data = MultipartEncoder(fields={'file': (os.path.basename(file_path), open(file_path, 'rb'), 'application/octet-stream')})
        headers = {'Content-Type': multipart_data.content_type, 'Authorization': api_key}
        response = requests.post(f"{server_url}/api/v1/upload", data=multipart_data, headers=headers)
        response.raise_for_status()
        logger.info(response.text)
        return response.text      
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error occurred: {e}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")  


def scan(data, server_url, api_key):
    try:
        """Scan the file"""
        logger.info("Scanning file")
        post_dict = json.loads(data)
        headers = {'Authorization': api_key}
        response = requests.post(f"{server_url}/api/v1/scan", data=post_dict, headers=headers)
        response.raise_for_status()
        logger.info(response.text)      
    except json.JSONDecodeError as e:
        logger.error(f"Error parsing response as JSON: {e}")
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error occurred: {e}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")  


def pdf(data, server_url, api_key):
    try:
        """Generate PDF Report"""
        logger.info("Generate PDF report")
        headers = {'Authorization': api_key}
        data = {"hash": json.loads(data)["hash"]}
        response = requests.post(f"{server_url}/api/v1/download_pdf", data=data, headers=headers, stream=True)
        response.raise_for_status()
        with open("report.pdf", 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        logger.info("Report saved as report.pdf")     
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error occurred: {e}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")  


def json_resp(data, server_url, api_key):
    try:
        """Generate JSON Report"""
        logger.info("Generate JSON report")
        headers = {'Authorization': api_key}
        data = {"hash": json.loads(data)["hash"]}
        response = requests.post(f"{server_url}/api/v1/report_json", data=data, headers=headers)
        response.raise_for_status()
        with open("report.json", "a") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        logger.info("Report saved as report.json")
        logger.info(response.text)
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error occurred: {e}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")  


def delete(data, server_url, api_key):
    try:
        """Delete Scan Result"""
        logger.info("Deleting Scan")
        headers = {'Authorization': api_key}
        data = {"hash": json.loads(data)["hash"]}
        response = requests.post(f"{server_url}/api/v1/delete_scan", data=data, headers=headers)
        response.raise_for_status()
        logger.info(response.text)     
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error occurred: {e}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")  


def main():
    parser = argparse.ArgumentParser(description='File Upload and Scan Script')
    parser.add_argument('file', type=str, help='Path to the file')
    parser.add_argument('server', type=str, help='Server URL')
    parser.add_argument('apikey', type=str, help='API Key')
    parser.add_argument('action', choices=['upload', 'scan', 'pdf', 'json', 'delete'], help='Action to perform')
    args = parser.parse_args()

    file_path = args.file
    server_url = args.server
    api_key = args.apikey
    action = args.action

    if action == 'upload':
        response = upload(file_path, server_url, api_key)
    elif action == 'scan':
        response = scan(upload(file_path, server_url, api_key), server_url, api_key)
    elif action == 'json':
        response = json_resp(upload(file_path, server_url, api_key), server_url, api_key)
    elif action == 'pdf':
        response = pdf(upload(file_path, server_url, api_key), server_url, api_key)
    elif action == 'delete':
        response = delete(upload(file_path, server_url, api_key), server_url, api_key)

if __name__ == "__main__":
    main()
