age = 21
first_name = "Sam"
last_name = "Samuelson"

# print(first_name + " " + last_name)

#print (f"{first_name} {last_name} is {age} years old.")

#print (last_name - first_name) 

# which one of these will NOT work?
# a
##print (first_name + " " + last_name + " is " + int(age) + " years old.")

# b
#print (first_name + " " + last_name + " is " + str(age) + " years old.")

# c
#print (f"{first_name} {last_name}" + " is " + str(age) + " years old.")

#print ("hello", 1, 3, "world")

"""
    mutable vs immutable
"""

"""
    Lists
        - data structures
"""

shopping_list = ["chocolate", "marshmallows" , "crackers"] # zero indexed

# print (shopping_list[2])

# shopping_list.append("raspberry jam")
# shopping_list.remove("marshmallows")

# del shopping_list[2]

"""
    FOR LOOP
"""
for index in range(10):
    print(index)

print("start and finish")
for index in range(2, 10):
    print(index)

print("backwards")
for index in range(10, 2, -1):
    print(index)

for index in range(len(shopping_list)):
    print(shopping_list[index])


# - given a list of numbers, return a new list with just the even numbers

old_list = [3,6,8,9,2,5,6,0,1]
new_list = []

# your code goes here

print(new_list)