# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

num = 10

for i in range(0, num):
    for j in range(0, i+1):
        print(j+1, end= " ")
    print()





# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 

num = 5
for i in range(0,num):
    for j in range(0, i+1):
        print(i+1, end = " ")
    print()




# 0 
# 1 2 
# 2 3 4 
# 3 4 5 6 
# 4 5 6 7 8

num = 5
for i in range(0,num):
    for j in range(0, i+1):
        print(j+i, end = " ")
    print()






# 1
# 2 3
# 4 5 6
# 7 8 9 10

num = 5
n = 1
for i in range(0, num):
    for j in range(0, i+1):
        print(n, end = " ")
        n = n+1
    print()