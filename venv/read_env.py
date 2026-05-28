from dotenv import load_dotenv
import os
 
load_dotenv()  # reads .env file in current folder
 
name = os.getenv('MY_NAME')
api_key = os.getenv('DUMMY_KEY')
 
print(f'Hello {name}, your key starts with {api_key[:4]}...')