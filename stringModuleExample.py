# import math
# import string
# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)



# import statistics
# score = [40, 50, 100, 60, 32, 74, 93, 54, 98, 75, 49, 73, 104]
# # print(math.floor(statistics.mean(score)))
# print(statistics.mean(score))
# print(statistics.median(score))
# print(statistics.mode(score))
# print(statistics.stdev(score))



# from math import *
# from math import pi as PI
# print(PI)




# for i in dir(math):
#     print(i)




# import random
# print(random.randint(1,5))





# write a function which generated a random 6 digits characters for user unique id 
# import random
# import string
# user_id = string.ascii_letters + string.digits
# def generateId():
#     userId = ''.join(random.choices(user_id, k = 10))
#     print(userId)

# generateId()




# it choooses random number from the list
# age = [22, 31, 10, 7, 32, 21, 18, 15, 19]
# print(random.choice(age))


# Modify the previous task. Declare a function named user_id_gen_by_user.
#  It doesn’t take any parameters but it takes two inputs using input().
#  One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

# import random
# import string

# user_id = string.ascii_letters + string.digits

# length_of_id = int(input('enter the length of the id: '))
# no_of_id = int(input("how many id's you want to generate: "))

# def user_id_gen_by_user():
#     for i in range(no_of_id):
#         print(''.join(random.choices(user_id, k = length_of_id)))


# user_id_gen_by_user()


# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
# import random
# def rgb_color_gen():
#     red_value = random.randint(0,255)
#     green_value = random.randint(0,255)
#     blue_value = random.randint(0,255)
#     return f'rgb({red_value}, {green_value}, {blue_value})'


# print(rgb_color_gen())


# there are other ways too
# import random
# values = map(str, [random.randint() for _ in range(3)])


# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
import random

# arr = [(234, 65, 34), (83, 123, 243), (243, 87, 34), (120, 62, 110), (120, 28, 73)]
# def list_of_rgb_colors():
#     print(random.choices(arr))


# list_of_rgb_colors()


import random
arr = [231, 22, 23, 83, 120, 111, 243, 23, 93, 110, 83, 93, 98, 105]
def list_of_rgb_colors():
    red_value = random.choices(arr)
    green_value = random.choices(arr)
    blue_value = random.choices(arr)
    print(f'{red_value}, {green_value}, {blue_value}')

    


list_of_rgb_colors()
