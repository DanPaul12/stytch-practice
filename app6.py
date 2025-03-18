import requests
import os
from dotenv import load_dotenv

load_dotenv()
STYTCH_PROJECT_ID = os.getenv('STYTCH_PROJECT_ID')
STYTCH_SECRET = os.getenv('STYTCH_SECRET')
if not STYTCH_PROJECT_ID or not STYTCH_SECRET:
    print('missing auth')

header = {'Content-Type':'application/json'}
auth = (STYTCH_PROJECT_ID, STYTCH_SECRET)

def login_with_password():
    try:
        response = requests.post(url='https://test.stytch.com/v1/passwords/authenticate', auth=auth, headers=header, json={'email':'dan.paul.schechter@gmail.com',
                                                                                                                        'password':'IAsb%^56HHHJ127@&6JHhajad'})
        if response.status_code == 200:
            print('logged in with password')
            send_sms_code()
        else:
            print(f'login with passsword error: {response.text}')
    except requests.exceptions.RequestException as e:
        print(e)

def send_sms_code():
    try:
        response = requests.post(url='https://test.stytch.com/v1/otps/sms/send', auth=auth, headers=header, json={'phone_number':'+18052174796'})
        if response.status_code == 200:
            print('sms code sent')
            data = response.json()
            phone_id = data['phone_id']
            authenticate_sms_code(phone_id)
        else:
            print(f'sms code send error: {response.text}')
    except requests.exceptions.RequestException as e:
        print(e)

def authenticate_sms_code(method_id):
    try:
        sms_code = input('please enter sms code:')
        response = requests.post(url='https://test.stytch.com/v1/otps/authenticate', auth=auth, headers=header, json={'method_id':method_id,
                                                                                                                      'code':sms_code})
        if response.status_code == 200:
            print('sms code authenticated')
        else:
            print(f'sms authenticate error: {response.text}')
    except requests.exceptions.RequestException as e:
        print(e)

login_with_password()