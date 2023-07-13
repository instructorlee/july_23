# price = 12

# if price < 10:
#     print("A")

# elif price > 15 and price < 22:
#     print("B")

# elif price < 20:
#     print("C")

# elif int(price / 2) == 22:
#     print("D")

# elif price < 30 and price % 2 == 0:
#     print("E")

# elif price > 19:
#     print("F")

# else:
#     print("oops")


"""
    List -
        - mutable
        - can add/remove/update/rearrange elements
        - indexed
        - use: when you need to update elements 

    tuples -
        - immutable
        - CANNOT add/remove/update/rearrange elements
        - indexed
        - use: when you want a fixed list that cannot be changed
    
"""
# some_tuple = (1, 2, 3, 4)

# # Dictionaries / objects

# name = "Fred"
# hair_colour = "Brown"
# age = 34

# fred = {
#     "name": "Fred",
#     "hair_colour": "Black",
#     "age": 34
#     }

# wilma = {
#     "name": "Wilma",
#     "hair_colour": "Brown",
#     "age": 34
#     }

# print(wilma['hair_colour'])

print ({
    "name": "Wilma",
    "hair-colour": "Brown",
    "age": 34
    }['hair_colour'])

# new_shopping_list = [
#     {"name": "milk", "completed": False},
#     {"name": "chocolate", "completed": True},
#     {"name": "crackers", "completed": False},
# ]

# print (new_shopping_list[0]['name'])

# for item in new_shopping_list:
#     for key in item.keys():
#         print(item[key])


# Functions
def display():
    print("Hello City!")

display() 

def display_message(message):
    print(message)

display_message("Hello World!")

def display_message_b(message, shout=True):
    if (shout):
        print(message.upper())
    else:
        print(message)

display_message_b("Hello Dave")

def calculate_tax(num_1, num_2):
    return num_1 + num_2

print(calculate_tax(2, 2))

