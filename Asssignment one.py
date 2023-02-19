mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.67 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchange_rate': 103.25
}

for data in mobile_data:
    name = mobile_data.get('data')[3].get('name')
    price = mobile_data.get('data')[3].get('price')
    country = mobile_data.get('data')[3].get('made')
    exchange_rate = mobile_data.get('exchange_rate')
    price_usd = price.replace('USD', ' ')

bdt = (float(price_usd))*exchange_rate
sentence = f'{name} is made in {country}. ' \
           f'The price is {price} which is almost equal to {bdt}BDT'
print(sentence)