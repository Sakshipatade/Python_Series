list1 = [3, 4, 7, 9, 1, 5, 8, 1, 2, 4, 6]

num = int(input("Enter how many numbers you want to add from the list: "))
total = 0
for i in range(num):
    total = total + i
print(total)

# OR

all_num = list1[:num]   

total = 0
for i in all_num:
    total = total + i
print(total)


# addition of numbers as per your own list
# num = input("enter numbers with spaces")
# sum = 0
# nums = [int(i.strip()) for i in num.split()]
# for i in nums:
#     sum = sum + i
# print(sum)
