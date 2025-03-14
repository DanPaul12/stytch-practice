import requests
import os
from dotenv import load_dotenv

load_dotenv()
project = os.getenv('STYTCH_PROJECT_ID')
secret = os.getenv('STYTCH_SECRET')

url = 'https://test.stytch.com/v1/otps/sms/send'

auth = (project, secret)
if not auth:
    print('missing auth')

header = {'Content-Type': 'application/json'}

payload = {'phone_number':'+18052174796'}

response = requests.post(url=url, auth=auth, headers=header, json=payload)