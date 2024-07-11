import requests
import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
refresh_token = os.getenv('REFRESH_TOKEN')

# Zoho token endpoint
accounts_url = " https://accounts.zoho.com"  # Adjust based on your region
token_url = f"{accounts_url}/oauth/v2/token"

data = {
    "grant_type": "refresh_token",
    "client_id": client_id,
    "client_secret": client_secret,
    "refresh_token": refresh_token
}

try:
    response = requests.post(token_url, data=data)
    response_data = response.json()

    print("Status Code:", response.status_code)
    print("Response JSON:", response_data)

    if response.status_code == 200:
        access_token = response_data.get("access_token")
        api_domain = response_data.get("api_domain")
        token_type = response_data.get("token_type")
        expires_in = response_data.get("expires_in")
        print("Access Token:", access_token)
        print("API Domain:", api_domain)
        print("Token Type:", token_type)
        print("Expires In:", expires_in)
    else:
        print(f"Failed to refresh access token. Status code: {response.status_code}")
        print(f"Response: {response.text}")

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
