# 1
# d = {"name":"Alice","age":30,"city":"New York"}
# print(d.get("age"))

# 2
# inventory = {"apples":10,"bananas":5}
# inventory.update({"apples":15})
# inventory.update({"ornages":8})
# print(inventory)

# 3 and 1
# for key, value in d.items():
#     print(f"Key: {key},Value: {value}")

# 4 and 1
# print(d.get("salary",0))
# print(d["salary",0])

# 5
# l = [1,2,3,4,5]
# squares = {num: num * num for num in l}
# print(squares)

# 6
# d1 = {"a": 1, "b": 2}
# d2 = {"c": 3, "b": 4}
# merged_dict = {**d2, **d1}
# merged_dict = d1 | d2
# print(merged_dict)

# 7
# word = input("Enter a word: ")
# length = len(word)
# def fun(word,length):
#   return({word:length})
# print(fun("Shiva"))

# for i in range(1,79):
#     for j in range(i):
#         print(i, end=" ")
#     print()

# text = "Python logic for kids"
# for i in text:
#     if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
#         continue
#     print(i,end=" ")

# for i in range(1,4):
#     for j in range(i):
#         print("*", end = " ")
#     print()
# for i in range(4, 1, -1):
#     for j in range(i):
#         print("*", end = " ")
#     print()

# for i in range(1,5):
#     for j in range(i):
#         print("*", end = "")
#     print()

# for i in range(1,8,2):
#     for j in range(i):
#         print("*", end = "")
#     print()

# alp = 65
# for i in range(1,6):
#     for j in range(i):
#         print(chr(alp), end = " ")
#         alp += 1
#     print()

# alp = 65
# for i in range(1,6):
#     for j in range(i):
#         print(chr(alp), end = " ")
#     alp += 1
#     print()

# for i in range(3):
#     for j in range(3):
#         print("Shiva",end= " ")
#     print()

# for i in range(1,11):
#     for j in range(1, 11):
#         print("*", end= "")
#     print()

# a = int(input("Enter any number: "))
# for i in range(a):
#     for j in range(a):
#         print("*", end = " ")
#     print()

n = int(input("Enter side of triangle: "))
for i in range(1,n):
    for j in range(i):
        print("$", end = " ")
    print()
for i in range(n,0, -1):
    for j in range(i):
        print("$", end = " ")
    print()