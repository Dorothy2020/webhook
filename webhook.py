import requests
import json

webhook_url = 'https://webhook.site/711e33e3-9ba1-4846-a476-2b6f8486276d'

data = {'name': 'Data Analyst'}

r = requests.post(webhook_url, data = json.dumps(data), headers={'Content-Type':'application/json'})