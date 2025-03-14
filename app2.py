import os
import requests
from dotenv import load_dotenv

# Load API keys securely from .env file
load_dotenv()
STYTCH_PROJECT_ID = os.getenv("STYTCH_PROJECT_ID")
STYTCH_SECRET = os.getenv("STYTCH_SECRET")

# Stytch API endpoint for sending magic links
STYTCH_MAGIC_LINK_URL = "https://test.stytch.com/v1/magic_links/email/send"

def send_magic_link(email):
    headers = {
        "Content-Type": "application/json",
    }
    auth = (STYTCH_PROJECT_ID, STYTCH_SECRET)
    payload = {
        "email": email,
        "login_magic_link_url": "https://yourapp.com/auth/callback",
        "signup_magic_link_url": "https://yourapp.com/signup/callback",
    }

    try:
        response = requests.post(STYTCH_MAGIC_LINK_URL, json=payload, headers=headers, auth=auth)
        #response.raise_for_status()  # Raise an error for non-2xx responses
        print(f"✅ Magic link sent successfully to {email}")
    except requests.exceptions.HTTPError as err:
        print(f"❌ Failed to send magic link: {err.response.status_code} - {err.response.json()}" if err.response else str(err))
    except Exception as e:
        print(f"❌ An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    print(STYTCH_PROJECT_ID)
    print(STYTCH_SECRET)
    user_email = input("Enter the user's email: ").strip()
    send_magic_link(user_email)
