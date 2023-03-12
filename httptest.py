import sys

import requests

response = requests.get('http://books.toscrape.com/')
if response.ok:
    print(response.text)
else:
    print('error')
    sys.exit()
