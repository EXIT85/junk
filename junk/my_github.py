import requests

r = requests.get('http://www.hackaday.com')

print(r.text)