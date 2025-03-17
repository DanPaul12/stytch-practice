import requests
import os
from dotenv import load_dotenv

load_dotenv()
STYTCH_PROJECT_ID = os.getenv('STYTCH_PROJECT_ID')
STYTCH_SECRET = os.getenv('STYTCH_SECRET')
STYTCH_PASSWORD_MIGRATE_API = 'https://test.stytch.com/v1/passwords/migrate'
if not STYTCH_PROJECT_ID or not STYTCH_SECRET:
    print('missing auth')

header = {'Content-Type':'application/json'}
auth = (STYTCH_PROJECT_ID, STYTCH_SECRET)
payload = {
    'email':'dan.paul.schechter@gmail.com',
    'hash': '$2y$10$76Lwt/9Gz4L31SgejEZIh./Z2nTz6Wxy0X.Zoe0LHY3ean2SMdV46',
    'hash_type':'bcrypt'
}

try:
    response = requests.post(headers=header, auth=auth, url=STYTCH_PASSWORD_MIGRATE_API, json=payload)
    response.raise_for_status()
    if response.status_code == 200:
        print('password added')
    else:
        print(response.text)
except requests.exceptions.RequestException as e:
    print(e)