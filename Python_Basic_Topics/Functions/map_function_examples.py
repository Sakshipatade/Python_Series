countries = ['india', 'china', 'japan', 'america', 'finland', 'netherland','russia', 'switzerland', 'england', 'europe']



# increase the each value by 5 in the below list
# nums = [1, 2, 3, 4, 5]

# def increaseValue(x):
#     return x+5

# result = list(map(increaseValue, nums))
# print(result)






# Use map to create a new list by changing each 
# country to uppercase in the countries list

# new_list = list(map(lambda name:name.upper(), countries))
# print(new_list)





# Use filter to filter out countries containing 'land'.

# def containsLand(name):
#     if 'land' in name:
#         return name

# OR
# result = filter(lambda name:'land' in name, countries)
# print(list(result))

# result = filter(containsLand, countries)
# print(list(result))
# both solution printing 




# Use filter to filter out countries
# containing six letters and more in the country list.


# def checkSize(name):
#     if len(name)>=8:
#         return name
    
# new_list = filter(checkSize, countries)
# print(list(new_list))





# use filter to check the country name starts with E
# def startWithE(name):
#     if name.startswith('e'):
#         return name
    

# result = filter(startWithE, countries)
# print(list(result))






