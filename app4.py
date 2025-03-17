import requests
import os
from dotenv import load_dotenv

load_dotenv()
STYTCH_PROJECT_ID = os.getenv('STYTCH_PROJECT_ID')
STYTCH_SECRET = os.getenv('STYTCH_SECRET')
STYTCH_PASSWORD_AUTHENTICATE_API = 'https://test.stytch.com/v1/passwords/authenticate'
if not STYTCH_PROJECT_ID or not STYTCH_SECRET:
    print('missing auth')

header = {'Content-Type':'application/json'}
auth = (STYTCH_PROJECT_ID, STYTCH_SECRET)
payload = {
    'email':'dan.paul.schechter@gmail.com',
    'password':'IAsb%^56HHHJ127@&6JHhajad'
}

try:
    response = requests.post(headers=header, auth=auth, url=STYTCH_PASSWORD_AUTHENTICATE_API, json=payload)
    response.raise_for_status()
    if response.status_code == 200:
        print('first step done')
        STYTCH_SMS_SEND_API = 'https://test.stytch.com/v1/otps/sms/send'
        phone_number = '+18052174796'
        try:
            sms_send_response = requests.post(url=STYTCH_SMS_SEND_API, headers=header, auth=auth, json={'phone_number':phone_number})
            if sms_send_response.status_code == 200:
                print('sms sent')
                STYTCH_SMS_AUTHENTICATE_API = 'https://test.stytch.com/v1/otps/authenticate'
                data = sms_send_response.json()
                method_id = data['phone_id']
                code = input('please enter code:')
                try:
                    sms_authenticate_response = requests.post(url=STYTCH_SMS_AUTHENTICATE_API, headers=header, auth=auth, json={'method_id':method_id, 'code':code})
                    if sms_authenticate_response.status_code ==200:
                        print('fully logged in')
                    else:
                        print(sms_authenticate_response.text)
                except requests.exceptions.RequestException as e:
                    print(e)
                    print(sms_authenticate_response.text)
            else:
                print(sms_send_response.status_code)
                print(sms_send_response.text)
        except requests.exceptions.RequestException as e:
            print(e)
            print(sms_send_response.text)
    else:
        print(response.text)
except requests.exceptions.RequestException as e:
    print(e)
    print(response.text)