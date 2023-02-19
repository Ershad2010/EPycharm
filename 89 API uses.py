import requests
api_url = 'https://api.ipify.org?format=json'
response = requests.get(api_url)
print(response.status_code)
print(response.json())
