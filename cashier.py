# products = [
#     {
#         "name": "apples",
#         "price": .2,
#         "quantity": 4 
#     },
#     {
#         "name": "carrot",
#         "price": .1,
#         "quantity": 1
#     },
#     {
#         "name": "flour",
#         "price": 1.3,
#         "quantity": 2
#     },
#     {
#         "name": "water bottles",
#         "price": .05,
#         "quantity": 10
#     },
# ]

cart =[]

def user_shopping(cart):
    user_input = input("Item (enter 'done' when finished): ")
    while user_input != "done":
        Price = float(input("Price: "))
        Quantity = int(input("Quantity: "))
        item = {"name" : user_input,
                "price" : Price,
                "quantity" : Quantity}
        cart.append(item)
        
        user_input = input("Item (enter 'done' when finished): ")
    return cart
cart = user_shopping(cart)
print(cart)
# print (item)

def receipt(cart):
    print("------------")
    print("receipt")
    print("------------")
    total = 0.0
    for item in cart:
        print("%d %s %f KWD" % (item['quantity'],item['name'],item['price']))
        total +=( item['price']* item['quantity'])
    print("Total Price : %f KWD" % total)
receipt(cart)