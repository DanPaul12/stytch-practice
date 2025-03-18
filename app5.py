import requests
import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request

load_dotenv()
STYTCH_PROJECT_ID = os.getenv('STYTCH_PROJECT_ID')
STYTCH_SECRET = os.getenv('STYTCH_SECRET')
if not STYTCH_PROJECT_ID or not STYTCH_SECRET:
    print('missing auth')

SEND_MAGIC_LINK_API = 'https://test.stytch.com/v1/magic_links/email/send'

header = {'Content-Type':'application/json'}
auth = (STYTCH_PROJECT_ID, STYTCH_SECRET)

try:
    ml_response = requests.post(headers=header, auth=auth, json={'email':'dan.paul.schechter@gmail.com'}, url=SEND_MAGIC_LINK_API)
    if ml_response.status_code == 200:
        print('magic link sent!')
    else:
        print(ml_response.text)
except requests.exceptions.RequestException as e:
    print(f'Request exception: {e}')

app = Flask(__name__)

@app.route('/authenticate', methods=['GET'])
def ml_authenticate():
    auth_token = request.args.get('token')
    try:
        response = requests.post(url='https://test.stytch.com/v1/magic_links/authenticate',
                                 auth=auth,
                                 headers=header,
                                 json={'token':auth_token,
                                       'session_duration_minutes':60})
        if response.status_code == 200:
            print('logged in and session started')
            data = response.json()
            session_jwt = data['session_jwt']
            print(session_jwt)
            session_token = data['session_token']
            if not session_jwt or not session_token:
                print('missing tokens')
            session_authenticate(session_token)
            return('logged in and session authenticated')
        else:
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(e)

def session_authenticate(session_token):
    try:
        response = requests.post(url='https://test.stytch.com/v1/sessions/authenticate', auth=auth, headers=header, json={'session_token':session_token})
        if response.status_code == 200:
            data = response.json()
            new_jwt = data['session_jwt']
            print('session authhenticated')
            return ('session authenticated')
        else:
            return jsonify({'message': response.status_code})
    except requests.exceptions.RequestException as e:
        print(e)
    
if __name__ == '__main__':
    app.run(port=3000, debug=True)
