import os
import base64
from requests import post
from dotenv import load_dotenv
load_dotenv()
from amazon_paapi import AmazonApi
KEY = os.getenv('KEY')
SECRET = os.getenv('SECRET')
TAG = os.getenv('TAG')
COUNTRY =os.getenv('COUNTRY')
amazon = AmazonApi(KEY, SECRET, TAG, COUNTRY)
item = amazon.get_items('B07PBGGW39')[0]
print(item.item_info)
# def wp_heading_two(text):
#     code = f'<!-- wp:heading -->' \
#            f'<h2>{text}</h2>' \
#            f'<!-- /wp:heading -->'
#     return code
#
# def wp_image_url(url, product_name):
#     code = f'<!-- wp:image {{"align":"center","sizeSlug":"large"}} -->' \
#            f'<figure class="wp-block-image aligncenter size-large">' \
#            f'<img src="{url}" alt="{product_name}image"/>' \
#            f'<figcaption class="wp-element-caption">{product_name} image</figcaption>' \
#            f'</figure><!-- /wp:image -->'
#     return code
#
# def wp_button(link):
#     code = f'<!-- wp:buttons --><div class="wp-block-buttons">' \
#            f'<!-- wp:button {{"align":"center"}} --><div class="wp-block-button aligncenter">' \
#            f'<a class="wp-block-button__link wp-element-button" href="{link}" target="_blank" rel="noreferrer noopener">Buy now</a></div>' \
#            f'<!-- /wp:button --></div>' \
#            f'<!-- /wp:buttons -->'
#     return code
#
# def list_html(info_list):
#     code = '<!-- wp:list --><ul>'
#     for info in info_list:
#         item = f'<!-- wp:list-item --><li>{info}</li><!-- /wp:list-item -->'
#         code +=item
#     last_line = '</ul><!-- /wp:list -->'
#     code = code + last_line
#     return code
# file = open('keywords.txt')
# keywords = file.readlines()
# file.close()
# for keyword in keywords:
#     keyword = keyword.strip('\n')
#     search_result = amazon.search_items(keywords=keyword)
#     content = ''
#     for item in search_result.items:
#         title = item.item_info.title.display_value
#         wp_title = wp_heading_two(title)
#         product_image_url = item.images.primary.large.url
#         wp_image = wp_image_url(product_image_url, title)
#         try:
#             product_info = item.item_info.features.display_values
#         except:
#             product_info = ''
#         wp_list = list_html(product_info)
#         product_link = item.detail_page_url
#         wp_button_link = wp_button(product_link)
#         content = content + f'{wp_title}{wp_image}{wp_list}{wp_button_link}'
#
#         wp_user ='Ahmad'
#         wp_pass ='W444 GVr5 ghQA TFn1 ooSd ATBK'
#         wp_credential = f'{wp_user}:{wp_pass}'
#         wp_token = base64.b64encode(wp_credential.encode())
#         wp_headers = {'Authorization': f'Basic {wp_token.decode("utf-8")}'}
#
#     my_title = f'top 10 {keyword}'
#
#     def slugify(text):
#         code = text.strip().replace(' ', '-')
#         return code
#     my_slug = slugify(my_title)
#
#     def wp_posting(my_title, slug, content):
#         data = {
#             'title': my_title.title(),
#             'slug': slug,
#             "content": content
#         }
#         api_url = 'https://bestjobinuae.com/wp-json/wp/v2/posts'
#         res = post(api_url, data = data, headers = wp_headers)
#         if res.status_code == 201:
#             print('successfully posted')
#         else:
#             print('something wrong')
# wp_posting(my_title, my_slug, content)