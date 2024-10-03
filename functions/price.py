discount = 0 
tax = 0.08 

def apply_discount(price, discount_percentage): 
    discount = price * discount_percentage / 100
    return discount

product_price = float(input("Enter price: "))

def calculate_tax(product_price):
    return product_price * tax

if product_price > 100 and product_price <= 200: 
    discount = apply_discount(product_price, 10)
elif product_price > 200: 
    discount = apply_discount(product_price, 25) 

total_price = product_price - discount + calculate_tax(product_price) 

print(f"Total price: {total_price}")
