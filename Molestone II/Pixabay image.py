from requests import get
from pprint import pprint
api_key = '357c593c5ddc085a2c15fa773'
query = 'yellow+flowers'
api_url = f'https://pixabay.com/api/?key=32100689-{api_key}&q={query}&'
res = get(api_url)
api_data = res.json().get('hits')
# pprint(api_data)
for data in api_data:
    image_url = data.get('webformatURL')
    # pprint(image_url)
    file = open('images.txt', 'a+')
    file.writelines(image_url+'\n')
    file.close()