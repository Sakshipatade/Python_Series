list1 = [3, 4, 7, 2, 8, 1, 9]
num = int(input("Enter the number for returning the index of it: "))

# for i in list1:
#     if i ==  num:
#         print(f"index of your entered number is {list1.index(i)}")
#         break

# else:
#     print("number is not present in the list")



if num in list1:
    print(f"index of number is {list1.index(num)}")
else:
    print(-1)