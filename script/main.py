from os import environ, getenv
from dotenv import load_dotenv

load_dotenv()

print(getenv('FIRST_NAME'))
