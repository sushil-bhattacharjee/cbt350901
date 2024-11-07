from dotenv import load_dotenv
import os

load_dotenv()

usern = os.environ.get('USERNAME')
passw = os.environ.get('PASSWORD')

print(usern)
print(passw)