import requests

r = requests.get('http://127.0.0.1:8000/',
headers={'content-length': "19" })

print(r.text)