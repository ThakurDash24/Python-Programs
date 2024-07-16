def calculate_discounted_price(original_price, discount_percent):
    discount_amount = (discount_percent / 100) * original_price
    discounted_price = original_price - discount_amount
    return discounted_price

original_price = 100.0
discount_percent = 40
print(calculate_discounted_price(original_price, discount_percent))  
