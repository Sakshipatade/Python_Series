lst = [3, 4, 2, 6, 2, 8, 1, 6, 4, 0, 2, 4, 3, 7, 8]
seen = []

for i in lst:
    if i not in seen:
        seen.append(i)
print(seen)

