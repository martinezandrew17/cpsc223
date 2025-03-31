from collections import deque

today_sale = {}

def get_total_price(cart):
    return sum(cart.values())

def checkout_queue(*names):
    return deque(names)

def add_customer_cart(name, **items):
    today_sale[name] = items
    print(f"Added {name} cart into today sale")

def lookup_cart(name):
    if name in today_sale:
        cart = today_sale[name]
        print(f"{name} cart contains:")
        for item, price in cart.items():
            print(f"{item}: {price}")
        total = get_total_price(cart)
        discount = apply_discount(name)
        final_total = total * (1 - discount/100)
        print(f"Total price: {final_total}")

def remove_item(name, item):
    if name in today_sale and item in today_sale[name]:
        del today_sale[name][item]
        print(f"Removed {item} from {name}'s cart")
    else:
        print("Item not found")

def apply_discount(name):
    discount = 0
    if len(name) % 3 == 0:
        discount += 10
        print("10% discount applied (name length divisible by 3)")
    if name[0].lower() in 'aeiou':
        discount += 10
        print("10% discount applied (name starts with vowel)")
    return discount

def add_item(name, item, price=0):
    if name in today_sale:
        today_sale[name][item] = price
        if price == 0:
            print(f"Added {item} to {name}'s cart (free item)")
        else:
            print(f"Added {item} to {name}'s cart")
    else:
        print("Name not found")

def sale(queue):
    while queue:
        print(f"Current queue: {queue}")
        current = queue.popleft()
        print(f"Serving {current}")
        lookup_cart(current)
    print("No more in queue")




    



