def my_function():
    first_name = "sakshi"
    last_name = 'patade'
    space = ' '
    full_name = first_name + space + last_name
    return full_name


print(my_function())


# ==============================================================================================
def my_name(f_name, l_name):
    space = ' '
    full_name = f_name + space + l_name
    return full_name


print(my_name(l_name = 'patade', f_name = 'sakshi'))


# ==============================================================================================
def is_number_even(num):
    if num % 2 == 0:
        return True
    return False


print(is_number_even(3))
print(is_number_even(10))


# ==============================================================================================
def return_name(name = 'medialoop user'):
    space = ' '
    message = name + space + 'welcome dear!'
    return message


print(return_name())
# print(return_name('vaishu'))


# ==============================================================================================
def func(lst=[]):
    lst.append(1)
    return lst

print(func())
print(func())
print(func())


# ==============================================================================================
def func(lst=[]):
    lst = lst + [1]
    return lst

print(func())
print(func())
print(func())


# ==============================================================================================
def add_user(user, users= None):
    if users is None:
        users = []
    users.append(user)
    return users


print(add_user('sakshi'))
print(add_user('vaihsu'))
print(add_user('meira'))
print(add_user('rita'))


# ==============================================================================================
def func(a, b=5, c=10):
    return a + b * c

print(func(2))
print(func(2, 3))
print(func(2, 3, 4))
print(func(2, c=3))


# ==============================================================================================
def func(a, b=[], c=10):
    b.append(a)
    return b, c

print(func(1))
print(func(2))
print(func(3, [100]))


# ==============================================================================================
def func(lst=[]):
    lst.append(1)
    return lst

print(func())
print(func())
print(func())


# ==============================================================================================
def func(lst=None):
    if lst is None:
        lst = []
    lst.append(1)
    return lst


print(func([10]))
print(func())

# ==============================================================================================
# def my_team(team, *names_of_players):
#     print(f'team name is: {team}')

#     for i in names_of_players:
#         print(f"team player is: {i}")


# print(my_team('coco-melon','sakshi', 'vaishu', 'mira', 'jaara', 'ruoko'))

# ==============================================================================================
# def my_players(*players):
#     return f"team players are: {players}"


# print(my_players('sakshi', 'seuija', 'saloun', 'vcera'))


# ==============================================================================================
# def area(radius):
#     pi = 3.14
#     area_of_circle = pi * radius ** 2
#     return int(area_of_circle)


# print(area(20))


# ==============================================================================================
# important one
# def add_all_nums(*nums):
#     for i in nums:
#         if not isinstance(i, (int, float)):
#             return f"'{i}' is not a number. Enter a valid number."
#     return sum(nums)

# # Take input and convert properly
# user_input = input('Enter numbers separated by comma: ')

# try:
#     nums = [float(x.strip()) for x in user_input.split(',')]  # [5.0, 4.0, 2.0]
#     print(add_all_nums(*nums))  # *nums unpacks the list → add_all_nums(5.0, 4.0, 2.0)
# except ValueError:
#     print("Invalid input! Please enter numbers separated by commas.")



# ==============================================================================================
# def reverse_list(arr):
#         nums = [i for i in reversed(arr)]
#         print(nums)


# reverse_list(['a', 'b', 'c', 'd'])
# reverse_list([3, 4, 2, 1])


# ==============================================================================================
# food_stuff= ['Potato', 'Tomato', 'Mango', 'Milk']

# def add_item(lst,item):
#     lst.append(item)
#     return lst


# print(add_item(food_stuff, 'cherry'))


# ==============================================================================================
# def sum_of_numbers(num):
#     total = 0
#     for i in range(num+1):
#         total += i
#     return total
# print(sum_of_numbers(5))



# ==============================================================================================
# def sum_of_odds(num):
#     total = 0
#     for i in range(num+1):
#         if i % 2 == 1:
#             total += i
#     return total
    

# print(sum_of_odds(10))



# ==============================================================================================
# def evens_and_odds(num):
#     even = 0
#     odd = 0
#     for i in range(num+1):
#         if i % 2 == 0:
#             even += 1
#         else:
#             odd += 1
#     print(f'The total even numbers are: {even}')
#     print(f'The total odd numbers are: {odd}')
    
    
# evens_and_odds(100)



# ==============================================================================================
# def factorial(num):
#     mul = 1
#     for i in reversed(range(1, num+1)):
#         mul = mul * (i)
#     return mul
     
# print(factorial(5))



# ==============================================================================================
# def is_empty(param):
#     if not param:
#         return f'argument is empty'
#     return param
    


# print(is_empty())
