lst = [2, 4, 2, 6, 7, 4, 8, 3, 1, 1, 4, 5, 8, 9, 7, 5, 1, 1, 2]

seen = []
# this will print unique items in list
for i in lst:
    if i not in seen:
        seen.append(i)
print(seen)

for i in seen:
    print(f'Count of {i}: {seen.count(i)}')