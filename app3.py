import requests
import os
from dotenv import load_dotenv

load_dotenv()
PROJECT_ID = os.getenv('STYTCH_PROJECT_ID')
SECRET = os.getenv('STYTCH_SECRET')
STYTCH_URL = 'https://test.stytch.com/v1/otps/sms/send'

header = {'Content-Type': 'application/json'}

payload = {'phone_number':'+18052174796'}

auth = (PROJECT_ID, SECRET)

try:
    response = requests.post(url=STYTCH_URL, auth=auth, headers=header, json=payload )
    print(response.text)
except requests.exceptions.RequestException as e:
    print(e)

