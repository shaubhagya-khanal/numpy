total=0
def total_cost(cart):
    for items in cart:
    total=total+(['price']*['quantity'])

cart = [
    {"name": "wheat", "price": 30, "quantity": 4},
    {"name": "maize", "price": 40, "quantity": 5},
    {"name": "apple", "price": 100, "quantity": 6}
]
for items in cart:
    total=total+(['price']*['quantity'])
    