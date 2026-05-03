list1 = [3, 4, 7, 9, 1, 5, 8, 1, 2, 4, 6]

# num = int(input("Enter how many numbers you want to add from the list: "))
# total = 0
# for i in range(num):
#     total = total + list1[i]
# print(total)



# all_num = list1[:num]

# total = 0
# for i in all_num:
#     total = total + i
# print(tota

# list1.sort(reverse= True)
# list1.sort()

# for i in list1:
#     sum = list1[0] + list1[1]
# print(sum)



# how to find duplicate number in list 
for i in list1:
    if list1.count(i) > 1 :
        list1.remove(i)
print(list1)


list1.sort(reverse = True)

sum = 0
for i in list1:
    sum = list1[0] + list1[1]
print("sum of two biggest number in list is {}".format(sum))

