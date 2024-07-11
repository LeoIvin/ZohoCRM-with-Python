import os
import requests
from dotenv import load_dotenv
from init import SDKInitializer
import json

initializer = SDKInitializer()
initializer.initialize()

load_dotenv()

# starter api example code
def get_org():
    access_token = os.getenv('ACCESS_TOKEN')

    api_domain = "https://www.zohoapis.com/crm/v6/org"

    headers = {
        "Authorization": f"Zoho-oauthtoken {access_token}",
        "Content-Type": "application/json"
    }

    response = requests.get(url=api_domain, headers=headers)

    if response.status_code == 200:
        print(response.json())
    else:
        print(response.status_code, response.text)


def get_currency():
    access_token = os.getenv('ACCESS_TOKEN')

    api_domain = "https://www.zohoapis.com/crm/v6/org/currencies"

    headers = {
        "Authorization": f"Zoho-oauthtoken {access_token}",
        "Content-Type": "application/json"
    }

    response = requests.get(url=api_domain, headers=headers)

    if response.status_code == 200:
        print(response.json())
    else:
        print(response.status_code, response.text)





