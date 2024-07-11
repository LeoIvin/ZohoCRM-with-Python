import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Define the necessary parameters
grant_token = os.getenv('GRANT_TOKEN')
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
redirect_uri = os.getenv('REDIRECT_URL')

# Print the environment variables to ensure they are loaded correctly
print("Grant Token:", grant_token)
print("Client ID:", client_id)
print("Client Secret:", client_secret)
print("Redirect URI:", redirect_uri)

# Zoho token endpoint
accounts_url = " https://accounts.zoho.com/oauth/v2/token"

# Define the data payload for the token request
data = {
    "grant_type": "authorization_code",
    "client_id": client_id,
    "client_secret": client_secret,
    "redirect_uri": redirect_uri,
    "code": grant_token
}

# Make the POST request to exchange the grant token for access and refresh tokens
response = requests.post(accounts_url, data=data)

# Print the response status code and entire response JSON for debugging
print(f"Status Code: {response.status_code}")
print("Response JSON:", response.json())

# Check the response
if response.status_code == 200:
    token_info = response.json()
    access_token = token_info.get("access_token")
    refresh_token = token_info.get("refresh_token")
    print("Access Token:", access_token)
    print("Refresh Token:", refresh_token)
else:
    print(f"Failed to obtain access token. Status code: {response.status_code}")
    print(f"Response: {response.text}")
