import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv("app/.env")

def set_env_variable():
    variable_dict = os.environ.items()
    for key, value in variable_dict:
        os.environ[key] = value
