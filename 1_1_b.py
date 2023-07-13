if 1 == 2:
    print("true")

else:
    print ("not true")

likes_chocolate = True

if likes_chocolate:
    print("Likes chocolate")

else:
    print("Doesn't like chocolate.")

age = 21
name = "Fred"
if age <= 12:
    f"{name} is a child."

elif age <= 19:
    f"{name} is a teenager"

else:
    f"{name} is an adult"

# modulus
line_number = 10

print(line_number % 3) 

if (line_number % 2 == 0):
    print("Highlight line")
else:
    print("Don't highlight line")


"""
- Leap Year
            - Write a function that determines whether a given year is a leap year. 
            If a year is divisible by four, it is   
            a leap year, unless it is divisible by 100. 
            However, if it is divisible by 400, then it is.
            """

year = 2023