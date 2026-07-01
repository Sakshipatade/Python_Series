

# arr = [1, 2, 3, 4, 5]

# for i in arr:
#     print(i)

num = 6
for i in range(0, num):
    for j in range(0, num-i):
        print(" ", end = "")

    for j in range(0, i+1):
        print("* ", end= "")
    print()





# for i in range(0, num):
#     for j in range(0, num-i):
#         print(" ", end = " ")
#     print()


# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# for i in range(0, 5):
#     for j in range(0, i+1):
#         print(j+1, end = " " )
#     print()

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# for i in range(0, 5):
#     for j in range(0, i+1):
#         print(i+1, end= " ")
#     print()

#=======================================================

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# def add_numbers(a, b):
#     return a + b

# def sub_numbers(a, b):
#     return a - b

# print("Addition:",add_numbers(num1, num2))
# print("Substraction:",sub_numbers(num1, num2))
#=======================================================

