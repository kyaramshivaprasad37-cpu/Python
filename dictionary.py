# dictionary = a collection of {key:value} pairs
#              ordered and chnagable. No duplicates

# #capitals = {"USA":"Washinton D.C",
#             "India":"Delhi",
#             "China":"Bejing",
#             "Russia":"Moscow"}

'''for capital in capitals:
    a = input(f" Enter a name of the country: ")
    if capitals.get(a):
        print(capitals.get(a))
    else:
        print("It doesnt exist in the DICT")'''

'''capitals.update({"Germany":"Berlin"})
capitals.pop("China")
capitals.popitem() # clears latest item
capitals.clear()
print(capitals)'''

# a= capitals.keys()
# v = capitals.values()
# # for i in v:
# #     print(i)
# # print(v)

# # items = capitals.items() # [(),(),()] Dictionary in which it has tuples 
# for key, value in capitals.items():
#     print(f"{key}:{value}")
# # print(items)




#     HELLO


food = {"pizza":1.2,
        "samosa":2.9}
a = input()
print(food[a])