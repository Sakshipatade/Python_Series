lst = [2, 3, 4, 6, 2, 5, 7, 3, 4, 5, 5, 9, 0, 1, 4]

# # for i in set(lst):
# #     lst.count(i)
# #     print(f"count of {i} is {lst.count(i)}")


# lst2 = []

# for i in lst:
#     if i not in lst2:
#         print(f"count of {i} is {lst.count(i)}")
#         lst2.append(i)


# for i in set(lst):
#     print(f"count of {i} is {lst.count(i)}")


seen = []

for i in lst:
    if i not in seen:
        print(f"count of {i} is {lst.count(i)}")
        seen.append(i)