from requests import post
import base64
from pprint import pprint

wp_user ='Ahmad'
wp_pass ='W444 GVr5 ghQA TFn1 ooSd ATBK'
wp_credential = f'{wp_user}:{wp_pass}'
wp_token = base64.b64encode(wp_credential.encode())
wp_headers = {'Authorization': f'Basic {wp_token.decode("utf-8")}'}

post_data = {
    'title': 'Here is my title',
    'slug':'my-awesome-slug',
    'status': 'publish',
    'content': 'This is awesome content of mine',
    'categories':'172'
}
api_end_point = 'https://bestjobinuae.com/wp-json/wp/v2/posts'
r = post(api_end_point, data = post_data, headers = wp_headers)

print(r.status_code)
pprint(r.json())