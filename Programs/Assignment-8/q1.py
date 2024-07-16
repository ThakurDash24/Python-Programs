products = [
    {'Name': 'Orange', 'Price': 20}, 
    {'Name': 'Apple', 'Price': 8},
    {'Name': 'Banana', 'Price': 10},
    {'Name': 'Kiwi', 'Price': 30}
]
res=[product['Name'] for product in products if product['Price']>=10]
print('Products with price greater than 10 is :' ,res)

