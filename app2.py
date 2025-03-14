import os
import requests
from dotenv import load_dotenv

# Load API keys securely from .env file
load_dotenv()
STYTCH_PROJECT_ID = os.getenv("STYTCH_PROJECT_ID")
STYTCH_SECRET = os.getenv("STYTCH_SECRET")

# Stytch API endpoint for sending magic links
STYTCH_MAGIC_LINK_URL = "https://test.stytch.com/v1/magic_links/email/send"

if not STYTCH_PROJECT_ID or STYTCH_SECRET:
    print('missing auth')

auth = (STYTCH_PROJECT_ID, STYTCH_SECRET)

header = {'Content-Type':'application/json'}

payload = {
    'email':'dan.paul.schechter@gmail.com',
    'login_magic_link_url':'http://localhost:3000/authenticate'
}

try:
    response = requests.post(url=STYTCH_MAGIC_LINK_URL, auth=auth, headers=header, json=payload)
    if response.status_code == 200:
        print('yay')
        print(response.json)
    else:
        print(response.status_code)
        print(response.text)

except requests.exceptions.RequestException as e:
    print(e)