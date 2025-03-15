from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
project_id = os.getenv('STYTCH_PROJECT_ID')
secret = os.getenv('STYTCH_SECRET')
authenticate_url = 'https://test.stytch.com/v1/magic_links/authenticate'

@app.route('/authenticate', methods=['GET'])
def authenticate():
    token = request.args.get('token')
    if not token:
        print('token missing')
        exit(1)
    headers = {'Content-Type':'application/json'}
    auth = (project_id, secret)
    if not project_id or not secret:
        print('auth missing')
    payload = {'token': token}

    try:
        response = requests.post(url=authenticate_url, headers=headers, auth=auth, json=payload)
        response.raise_for_status()
        return jsonify({"message": "Authentication successful!", "data": response.json()})
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Authentication failed: {e}"}), 400
    
if __name__ == '__main__':
    app.run(port=3000, debug=True)