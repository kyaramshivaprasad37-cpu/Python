'''fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery","carrots","potatoes"]
meats = ["chicken","fish","turkey"]
groceries = [fruits, vegetables, meats]
print(groceries[0][3])'''

groceries = [["apple", "orange", "banana", "coconut"],
             ["celery","carrots","potatoes"],
             ["chicken","fish","turkey"]]

for i in groceries:
    for j in i:
        print(j,end=" ")
    print()    
    
    