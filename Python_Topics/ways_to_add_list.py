#for comnining two lists we can make use of:
# lst_one = ['table', 'jug', 'box']
# lst_two = ['bottle', 'shoes', 'pencil']



#using + operator
# lst_three = lst_one + lst_two
# print(lst_three)



#we can make use of list unpacking method like below
# lst_three = [*lst_one, *lst_two]
# print(lst_three)




#using itertools.chain()
# from itertools import chain
# lst_three = list(chain(lst_one, lst_two))
# print(lst_three)



# use of extend() method
# lst_one.extend(lst_two)
# print(lst_one)


# Note: we can make use of append but the output will be ['table', 'box', 'jug', ['bottle', 'shoes','pencil']]
# it treats one whole list as single object and append it to another hence do not use this technique


# use of list comprehension
# lst_three = [i for lst in (lst_one, lst_two) for i in lst]
# print(lst_three)



names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_countries, es, ru = names 
print(nordic_countries)
print(es)
print(ru)