from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.environ.get("API_KEY", "")
print(f"API_KEY={api_key[:4]}...")
print(f"SEC_USER_AGENT={os.environ.get('SEC_USER_AGENT', '')}")
