num = 10


for i in range(0, num):

    for j in range(0, i+1):
        print(j ,end= " ")
    
    for k in range(0, 2*(num-(i+1))):
        print(" ", end = " ")

    for l in range(0, i+1):
        print(l, end = " ")
    print()


for i in range(0, num):

    for j in range(0, num-i):
        print(j, end = " ")
    
    for k in range(0, 2*(i)):
        print(" ", end = " ")
    
    for l in range(0, num-i):
        print(l, end = " ")
    print()
