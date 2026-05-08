# def recur(num):
#     if num == 0:
#         return
#     else:
#         num -= 1
#         print(num)
#         recur(num)


# recur(5)


num = input("enter numbers with spaces")
sum = 0
nums = [int(i.strip()) for i in num.split()]
for i in nums:
    sum = sum + i
print(sum)