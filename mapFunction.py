# increase the each value by 5 in the below list

nums = [1, 2, 3, 4, 5]

def increaseValue(x):
    return x+5

result = list(map(increaseValue, nums))
print(result)
