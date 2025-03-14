import requests
import os
from dotenv import load_dotenv

load_dotenv()
project = os.getenv('STYTCH_PROJECT_ID')
secret = os.getenv('STYTCH_SECRET')
url = "https://test.stytch.com/v1/magic_links/email/send"

headers = {
    "Content-Type": "application/json"
}

payload = {
    "email": "dan.paul.schechter@gmail.com",
    "login_magic_link_url": "https://yourapp.com/auth/callback",
    "signup_magic_link_url": "https://yourapp.com/signup/callback",
}

auth = (
    project,
    secret
)

response = requests.post(url, json=payload, headers=headers, auth=auth)
response.raise_for_status()
print(response.status_code)
print(response.text)