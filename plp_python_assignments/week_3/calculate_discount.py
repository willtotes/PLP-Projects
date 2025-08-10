

def calculate_discount(price, discount_percent):
    if discount_percent < 20:
        return price
    
    discount_amount = (discount_percent / 100) * price
    final_price = price - discount_amount
    return final_price

print(calculate_discount(100, 20))
print(calculate_discount(100, 15))
print(calculate_discount(100, 40))
print(calculate_discount(100, 10))




