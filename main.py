'''import math

radius = float(input("Enter the radius of the Circle: "))
area = round(math.pi * math.sqrt(radius), 2)
print(f"The Area of the circle is {area} units squares")'''

'''age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible😊")
else:
    print("You are not eligible")'''


'''feedback = input("Is the food tasty😊(Y/N):")

if feedback == "Y":
    print("Thanks for the feedback, make sure to come again!")
elif feedback == "y":
    print("Thanks for the feedback, make sure to come again!")
elif feedback == "n":
    print("Sorry for your disappointment, we will make sure to improve.")
else:
    print("Sorry for your disappointment, we will make sure to improve.")'''

#Puthon Calculator

'''operator = input("Enter an operator +, /, -, * :")
num_1 = float(input("Enter your 1st number: "))
num_2 = float(input("Enter your 2nd number: "))

if operator == "+":
    print(round(num_1 + num_2))
elif operator == "-":
    print(num_1 - num_2)
elif operator == "/":
    print(round(num_1 / num_2, 2))
elif operator == "*":
    print(num_1 * num_2)
else:
    print(f"{operator} is not a valid operator")'''

# Weight Converter

'''weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds(K/P): ")

if unit == "K":
    weight *= 2.205
    unit = "Lbs."
    print(f"Your weight is {round(weight, 1)} {unit}")
elif unit == "P":
    weight /= 2.205
    unit = "kgs."
    print(f"Your weight is {round(weight, 1)} {unit}")
else:
    print(f"{unit} is not vaild unit")'''

#logical operators = evaluate multiple conditions (or, and, not)
#                    or = atleast one condition must be true
#                    and = both conditions must be true
#                    not = inverts the condition(not  False, not True)

''' temp = 20
is_raining = True

if temp > 40 or temp < 0 or is_raining:
    print("Better to stay at home")
else:
    print("its time to go out")'''



'''temp = 100
is_sunny = True

if temp < 15 and is_sunny:
    print("It is COLD outside")
    print("It is NOT RAINING")
elif temp < 15 and not is_sunny:
    print("It is COLD outside")
    print("It is RAINING")
elif temp >= 30 and is_sunny:
    print("It is HOt outside🥵")
    print("It is SUNNY")
elif temp >= 30 and not is_sunny:
    print("It is WARM outside")
    print("it is CLOUDY")
elif temp <=29 >= 15 and is_sunny:
    print("It is WARM outside")
    print("It is SUNNY")
elif temp <=29 >= 15 and not is_sunny:
    print("It is WARM outside")
    print("It is NOT SUNNY")'''


# conditional expression = A one-line shortcut for the if-else statement(ternary opreator)
#                          Print or assign ine of two values based on a condition
#                          X if condition else Y

'''num = 876879
a = 10
b = 9.5

max_num = a if a>b else b
min_num = a if a<b else b

print(max_num)
print(min_num)
# print("It is a even number" if num % 2 == 0 else "It is a odd number")'''

# name = input("Enter Your Full Name: ")

# result = len(name)
# result = name.find("a")
# result = name.rfind("a") It reads from back
# result = name.capitalize() First letter capital
# result = name.upper()
# result = name.lower()
# result = name.isdigit() only numbers True, else False
# result = name.isalpha()
# result = name.count("a")
# result = name.replace("p", "d")

# print(help(str))

# print(result)


# validate user input exercise
# 1. username is no more than 12 characters
# 2.username must not contain spaces
# 2.username must not contain digits

'''user_name = input("Enter the username: ")

if len(user_name) > 12:
    print("The username is no more than 12 characters")
elif not user_name.find(" ") == -1:
    print("Username must not contain spaces")
elif not user_name.isalpha():                  
    print("Username must not contain digits")
else:
    print(f"Hello {user_name}")'''

# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

'''phone_no = "6300804873"
print(phone_no[6])
print(phone_no[0: 4])
print(phone_no[:7])
print(phone_no[0: ])
print(phone_no[3:7])
print(phone_no[-1])
print(phone_no[-2])
print(phone_no[-3:])
print(phone_no[:-3])
print(phone_no[::3])
print(phone_no[::2])
print(phone_no[::1])

last_digits = phone_no[-3:]
print(f"xxxxxxx{last_digits}")

print(phone_no[::-1]) #reverse the str'''

# format specifiers = {values:flags} format a value based in what
#                                    flags are insereted

# .(number)f = round to that many decimal places(fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place to leftmost position
# :  = insert a space before positive numbers
# :, = commma separator

'''price1 = 38687.14159
price2 = 37876.637
price3 = -76868.88

print(f"Price 1 is ${price1:.1f}")
print(f"Price 2 is ${price2:.1f}")
print(f"Price 3 is ${price3:.1f}")

print(f"Price 1 is ${price1:10}")
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:10}")

print(f"Price 1 is ${price1:010}")
print(f"Price 2 is ${price2:010}")
print(f"Price 3 is ${price3:010}")

print(f"Price 1 is ${price1:<10}")
print(f"Price 2 is ${price2:<10}")
print(f"Price 3 is ${price3:<10}")

print(f"Price 1 is ${price1:>10}")
print(f"Price 2 is ${price2:>10}")
print(f"Price 3 is ${price3:>10}")

print(f"Price 1 is ${price1:^10}")
print(f"Price 2 is ${price2:^10}")
print(f"Price 3 is ${price3:^10}")

print(f"Price 1 is ${price1:,}")
print(f"Price 2 is ${price2:,}")
print(f"Price 3 is ${price3:,}")

print(f"Price 1 is ${price1:+}")
print(f"Price 2 is ${price2:+}")
print(f"Price 3 is ${price3:+}")

print(f"Price 1 is ${price1:+,.1f}")
print(f"Price 2 is ${price2:+,.1f}")
print(f"Price 3 is ${price3:+,.1f}")'''


# while loop = execute some code WHILE some condition remains true

'''name = input("Enter your name: ")

while name == "":
    print("You did nor entered your name")
    name = input("Enter your name: ")

    
print(f"helloo {name}")

age = int(input("Enter your age: "))

while age < 0:
    print("Your age cannot be negative")
    age = int(input("Enter your age: "))

print(f"Your are {age} years old")

food = input("Enter your favourite food(q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter your another favourite food(q to quit): ")
print("tata")'''


'''num = int(input("Enter a number between 1 - 10: "))

while  num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1 - 10: "))
print(f"Your number is {num}")'''


# Python compound interest calculator

'''principle_amount = 0
interest = 0
time = 0

while principle_amount <= 0:
    principle_amount = float(input("Enter the Priciple Amount: "))
    if principle_amount <= 0:
        print("Priciple Amount cannot be negative pr zero")

while interest <= 0:
    interest = float(input("Enter the interest: "))
    if interest <= 0:
        print("interest cannot be negative pr zero")

while time <= 0:
    time = int(input("Enter the Period of Time: "))
    if time <= 0:
        print("Time cannot be negative or zero")



total = principle_amount * pow((1 + interest/100), time)
interest = round(total - principle_amount,2)
print(f"Your total amount is ${total:.2f}")
print(f"Your total interest for {time} years is ${interest}")'''


'''priciple_amount = 0
interest = 0
time = 0

while True:
    priciple_amount = float(input("Enter Your Priciple Amount: "))
    if priciple_amount < 0:
        print("Principle Amount cannot be negative")
    else:
        break

while True:
    interest = float(input("Enter Your interest: "))
    if interest < 0:
        print("Interest cannot be negative")
    else:
        break

while True:
    time = int(input("Enter Your Period(Years): "))
    if time < 0:
        print("time cannot be negative")
    else:
        break

total = round(priciple_amount * pow((1 + interest/100), time),2)
interest = total - priciple_amount
print(f"Your Total Amount is ${total}")
print(f"Your total interest amount is ${interest:.2f}")'''


# for loops = execute a block of code a fixed number of times.
#             You can iterate over a range , string, sequence, etc.

'''print("code" == "zzzz")
print("code" != "zzzz")
print("code" < "zzzz")
print("code" > "zzzz")
print("code" <= "zzzz")
print("code" >= "zzzz")
print("code" <= "edocz")'''

'''mf = input()
age = int(input())
if mf == "M" and age >= 65 or mf == "F" and age >= 60:
    print("Eligible")
else:
    print("not eligible")'''

# for loops = execute a block of code a fixed number if times.
#             You can itearte over a range, string, seqeunce, etc.

# for x in range(1, 101):
    # print(x)

'''for x in reversed(range(1 ,11, 2)):
    print(x)

phone_num = "9392209185"
for x in phone_num:
    print(x)

for x in range(1, 21):
    if x == 16:
        continue
    else:
        print(x)

for x in range(1, 21,):
    if x == 16:
        break
    else:
        print(x)'''

# countdown timer

import time
counter = int(input("Enter your time in secs: "))

# for x in reversed(range(0, counter+1)):
    # print(x)
    # time.sleep(1)
# print("TIME'S UP")

for x in range(counter, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")    # format  specifiers zero padding
    time.sleep(1)
print("TIME'S UP")



    

















































































