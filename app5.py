import requests
import os
from dotenv import load_dotenv

load_dotenv()
PROJECT_ID = os.getenv('STYTCH_PROJECT_ID')
SECRET = os.getenv('STYTCH_SECRET')
STYTCH_URL = 'https://test.stytch.com/v1/otps/authenticate'

header = {'Content-Type': 'application/json'}

payload = {"method_id":"phone-number-test-879ef6c7-5ee9-40c7-bbd4-b0af3c9e0c05",
           "code":"157196"}

auth = (PROJECT_ID, SECRET)

try:
    response = requests.post(url=STYTCH_URL, headers=header, auth=auth, json=payload)
    if response.status_code == 200:
        print('gotem')
    else:
        print(response.status_code, response.text)
except requests.exceptions.RequestException as e:
    print(e)
    