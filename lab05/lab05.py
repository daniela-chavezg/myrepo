import requests
import json

url = "https://michaelgathara.com/api/python-challenge"

response = requests.get(url)

challenges = response.json()
print(challenges)