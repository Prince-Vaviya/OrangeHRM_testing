import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("ORANGEHRM_URL")
USERNAME = os.getenv("ORANGEHRM_USERNAME")
PASSWORD = os.getenv("ORANGEHRM_PASSWORD")