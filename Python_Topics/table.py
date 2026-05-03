# num = 2
# while num <=2:
#     print(num)
#     num += 1

# 3 * 1 = 3
# 3 * 2 = 6
# 3 * 3 = 9
# 3 * 4 = 12
# 3 * 5 = 15
# 3 * 6 = 18
# 3 * 7 = 21
# 3 * 8 = 24
# 3 * 9 = 27
# 3 * 10 = 30

# num = int(input("enter any number: "))
# for i in range(1, 11):
#     print(f"{num} * {i} = {num * i}")

# sqare of number from 1 to 10 like [1,4,9,16,25,36,49,64,81,100]

# for i in range(1,11):
#     print(i * i)

# for num in reversed(range(1, 11)):
#     print(num)

# for num in range(10,0,-1):
#     print(num)

# num = 7

# for i in range(0, num):
#     for j in range(0, i+1):
#         print("#", end= "")
#     print()

# num = 8

# for i in range(0,num):
#     for j in range(0, num):
#         print("#", end= " ")
    # print()

# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100


# for i in range(0,11):
#     for j in range(0, 11):
#         print(f"{j} * {j} = {j * j}")
#     break

# even_sum = 0
# odd_sum = 0
# for i in range(0,101):
#     if i % 2 == 0:
#         even_sum = even_sum + i
#     else:
#         odd_sum = odd_sum + i

# print(f"total even sum is {even_sum} and odd sum is {odd_sum}")

# countries = [
#   'Afghanistan',
#   'Albania',
#   'Algeria',
#   'Andorra',
#   'Angola',
#   'Antigua and Barbuda',
#   'Argentina',
#   'Botswana',
#   'Brazil',
#   'Brunei',
#   'Bulgaria',
#   'Burkina Faso',
#   'finland'
# ];
 

# word = "land"
# new_countries = [ i for i in countries if word in i]
# print(new_countries)


# fruits = ['banana', 'orange', 'mango', 'lemon'] 
# print(fruits[::-1])


# def my_function():
#     first_name = "sakshi"
#     last_name = 'patade'
#     space = ' '
#     full_name = first_name + space + last_name
#     return full_name


# print(my_function())

# def my_name(f_name, l_name):
#     space = ' '
#     full_name = f_name + space + l_name
#     return full_name


# print(my_name(l_name = 'patade', f_name = 'sakshi'))

# def is_number_even(num):
#     if num % 2 == 0:
#         return True
#     return False


# print(is_number_even(3))
# print(is_number_even(10))

# def return_name(name = 'medialoop user'):
#     space = ' '
#     message = name + space + 'welcome dear!'
#     return message


# print(return_name())
# # print(return_name('vaishu'))


# def func(lst=[]):
#     lst.append(1)
#     return lst

# print(func())
# print(func())
# print(func())


# def func(lst=[]):
#     lst = lst + [1]
#     return lst

# print(func())
# print(func())
# print(func())

# def add_user(user, users= None):
#     if users is None:
#         users = []
#     users.append(user)
#     return users


# print(add_user('sakshi'))
# print(add_user('vaihsu'))
# print(add_user('meira'))
# print(add_user('rita'))

# def func(a, b=5, c=10):
#     return a + b * c

# print(func(2))
# print(func(2, 3))
# print(func(2, 3, 4))
# print(func(2, c=3))

# def func(a, b=[], c=10):
#     b.append(a)
#     return b, c

# print(func(1))
# print(func(2))
# print(func(3, [100]))

# def func(lst=[]):
#     lst.append(1)
#     return lst

# print(func())
# print(func())
# print(func())



# def func(lst=None):
#     if lst is None:
#         lst = []
#     lst.append(1)
#     return lst


# print(func([10]))
# print(func())


# def my_team(team, *names_of_players):
#     print(f'team name is: {team}')

#     for i in names_of_players:
#         print(f"team player is: {i}")


# print(my_team('coco-melon','sakshi', 'vaishu', 'mira', 'jaara', 'ruoko'))


# def my_players(*players):
#     return f"team players are: {players}"


# print(my_players('sakshi', 'seuija', 'saloun', 'vcera'))

# def area(radius):
#     pi = 3.14
#     area_of_circle = pi * radius ** 2
#     return int(area_of_circle)


# print(area(20))

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


# def reverse_list(arr):
#         nums = [i for i in reversed(arr)]
#         print(nums)


# reverse_list(['a', 'b', 'c', 'd'])
# reverse_list([3, 4, 2, 1])



# food_stuff= ['Potato', 'Tomato', 'Mango', 'Milk']

# def add_item(lst,item):
#     lst.append(item)
#     return lst


# print(add_item(food_stuff, 'cherry'))


# def sum_of_numbers(num):
#     total = 0
#     for i in range(num+1):
#         total += i
#     return total
# print(sum_of_numbers(5))


# def sum_of_odds(num):
#     total = 0
#     for i in range(num+1):
#         if i % 2 == 1:
#             total += i
#     return total
    

# print(sum_of_odds(10))


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


def factorial(num):
    mul = 1
    for i in reversed(range(1, num+1)):
        mul = mul * (i)
    return mul
     
print(factorial(5))

def is_empty(param):
    if not param:
        return f'argument is empty'
    return param
    


print(is_empty())
