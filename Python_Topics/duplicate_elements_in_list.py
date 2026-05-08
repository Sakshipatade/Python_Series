# how to find duplicate number in list 

list1 = [3, 4, 7, 9, 1, 5, 8, 1, 2, 4, 6]
for i in list1:
    if list1.count(i) > 1 :
        list1.remove(i)
print(list1)
