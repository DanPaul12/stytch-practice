import requests
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify

load_dotenv()
PROJECT_ID = os.getenv('STYTCH_PROJECT_ID')
SECRET = os.getenv('STYTCH_SECRET')
if not PROJECT_ID or not SECRET:
    print('missing auth')

MAGICLINK_AUTHENTICATE_URL = 'https://test.stytch.com/v1/magic_links/authenticate'
OTP_SMS_SEND_URL = 'https://test.stytch.com/v1/otps/sms/send'
OTP_AUTHENTICATE_API = 'https://test.stytch.com/v1/otps/authenticate'
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
    print(response.text)


app = Flask(__name__)

@app.route('/authenticate', methods=['GET'])
def authenticate():
    token = request.args.get('token')
    if not token:
        print('no token gathered')

    auth = (PROJECT_ID, SECRET)
    header= {'Content-Type':'application/json'}
    payload= {'token': token}

    try:
        response = requests.post(url=MAGICLINK_AUTHENTICATE_URL, auth=auth, headers=header, json=payload)
        response.raise_for_status()
        if response.status_code == 200:
            print('authentication level 1 successful')
            try:
                response2 = requests.post(url=OTP_SMS_SEND_URL, auth=auth, headers=header, json= {'phone_number':'+18052174796'})
                response2.raise_for_status()
                if response2.status_code == 200:
                    print('sms otp sent')
                    data = response2.json()
                    otp_code = input('Please enter otp_code:')
                    phone_id = data['phone_id']
                    if not otp_code or not phone_id:
                        print('missing otp code or phone_id')
                    try:
                        response3 = requests.post(url=OTP_AUTHENTICATE_API, headers=header, auth=auth, json={'method_id':phone_id, 'code':otp_code})
                        response3.raise_for_status()
                        if response3.status_code == 200:
                            print('fully authenticated')
                            return 'fully authenticated'
                    except requests.exceptions.RequestException as e:
                        print(e)
                        print(response3.text)
                else:
                    print(response2.status_code)
                    print(response2.text)
            except requests.exceptions.RequestException as e:
                print(f'Unexpected error: {e}')
                print(response2.text)
        else:
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f'Unexpected error: {e}')
        print(response.text)

if __name__ == '__main__':
    app.run(port=3000, debug=True)