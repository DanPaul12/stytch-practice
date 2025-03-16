import requests
import os
from dotenv import load_dotenv

load_dotenv()
PROJECT_ID = os.getenv('STYTCH_PROJECT_ID')
SECRET = os.getenv('SYTCH_SECRET')

STYTCH_API_URL = 'https://test.stytch.com/v1/magic_links/email/send'

headers = {'Content-Type':'application/json'}

auth = (PROJECT_ID, SECRET)

payload = {'email':'dan.paul.schechter@gmail.com'}

try:
    response = requests.post(url=STYTCH_API_URL, auth=auth, headers=headers, json=payload)
    response.raise_for_status()
    if response.status_code == 200:
        print('email sent!')
    else:
        print(f'Error code: {response.status_code}')
        print(response.text)
except requests.exceptions.RequestException as e:
    print(f'Unexpected error: {e}')
