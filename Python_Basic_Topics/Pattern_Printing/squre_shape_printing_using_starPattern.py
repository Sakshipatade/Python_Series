#   * * * * * * 
#   * * * * * * 
#   * * * * * * 
#   * * * * * * 
#   * * * * * * 


# num = 5
# for i in range(0,num):
#     for j in range(0, i+1):
#         print("*", end =" ")
    
#     for k in range(0, num-i):
#         print("*", end = " ")
#     print()

#   * * * * * * 
#   *         * 
#   *         * 
#   *         * 
#   *         * 
#   * * * * * *
num= 6
for i in range(0,num):
    for j in range(0, num):
        # if j == 0 or j == num-1 or i == 0 or i == num-1:
        #     print("*", end = " ")
        # else:
        #     print(" ", end = " ")
        print(f"{i}{j} ", end = "")
    print()


