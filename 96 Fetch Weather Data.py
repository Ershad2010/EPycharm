import requests
import pprint
apikey ='4eed95075f6363b5d84bad0d97d76667'
city_name = 'Dhaka'
api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={apikey}'
# print(api_url)
res = requests.get(api_url)
# print(res.status_code)
api_data = res.json()
# print(api_data)
pprint.pprint(api_data)