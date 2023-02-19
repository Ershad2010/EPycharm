import requests
r = requests.get('https://jsonplaceholder.typicode.com/posts')
# r = r.status_code
print(r.json())