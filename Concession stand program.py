# Concession stand program

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fried": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25
}
orders = []
total = 0

print("------------MENU-------------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------------===-------------")


while True:
    food = input("Select any food item (q to quit): ").lower()
    if food == "q":
        break 
    elif menu.get(food) is not None:
        orders.append(food)
print("-------- YOUR ORDER --------")   
for food in orders:
    total += menu.get(food)
    print(food, end = " ")
print()
print(f" Your total is: ${total}")
print("---------------------------")




        





