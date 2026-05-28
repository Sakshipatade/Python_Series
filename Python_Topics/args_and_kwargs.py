# Create a function that accepts any number of integers and returns their sum.

# def addFunction(*nums):
#     return sum(nums)

# print(addFunction(3,4,6,9,1,7,5))





# Find Maximum from passed arguments

# def findMax(*nums):
#     for i in nums:

# findMax(3,4,5,6,7)





nums:list[int] = [4,5,6,7,8,9]
# nums.sort(reverse=True)
# print(nums[0])  <-Either this will be the logic i used to find out the largest number from the list

for i in nums:
    for j in nums:
        if j>i:
            temp = j
            j = i
            i = temp
        
    

