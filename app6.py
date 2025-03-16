import requests
import os
from dotenv import load_dotenv

load_dotenv()
STYTCH_PROJECT_ID = os.getenv("STYTCH_PROJECT_ID")
STYTCH_SECRET = os.getenv("STYTCH_SECRET")

# Stytch API endpoint for sending magic links
STYTCH_MAGIC_LINK_URL = "https://test.stytch.com/v1/sessions/authenticate"

header = {'Content-Type':'application/json'}

payload = {
    "session_token":"B6w6G3puFVoFnrBozCgyectJPGzYQWcleunaNlEpNXk1"
}

auth = (STYTCH_PROJECT_ID, STYTCH_SECRET)

try:
    response = requests.post(url=STYTCH_MAGIC_LINK_URL, headers=header, auth=auth, json=payload)
    if response.status_code == 200:
        print('session authenticated')
        print(response.text)
except:
    pass