num = 6

for i in range(0,num):
    for j in range(0,num-i):
        print(" ", end = "")
    
    for k in range(0,i+1):
        print("*", end = "")
    
    for l in range(0, i+1):
        print("*", end = "")

    for l in range(0,num-i):
        print(" ", end = "")
    print()




for i in range(0, num):
    for j in range(0,i+1):
        print(" ", end = "")

    for k in range(0, num-i):
        print("*", end="")
    

    for l in range(0,num-i):
        print("*", end = "")
    

    for n in range(0, i+1):
        print(" ", end = "")
    print()

# n = int(input("Enter number of rows: "))

# # Upper half (pyramid)
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")   # spaces
#     print("* " * i)                # stars

# # Lower half (inverted pyramid)
# for i in range(n - 1, 0, -1):
#     print(" " * (n - i), end="")   # spaces
#     print("* " * i)                # stars