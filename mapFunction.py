# increase the each value by 5 in the below list

nums = [1, 2, 3, 4, 5]

def increaseValue(x):
    return x+5

result = list(map(increaseValue, nums))
print(result)


# Use map to create a new list by changing each 
# country to uppercase in the countries list

countries = ['india', 'china', 'japan', 'america', 'finland', 'netherland','russia', 'switzerland']

# new_list = list(map(lambda name:name.upper(), countries))
# print(new_list)





# Use filter to filter out countries containing 'land'.
# def containsLand(name):
#     if 'land'.isinstance(name):
#         return name
    
# result = filter(containsLand, countries)
# print(list(result))


