''' 
Problem 1
Use a context manager to write the following city names to a file called cities.txt, one city per line:

Tokyo
Paris
New York
Sydney
Then, use a second context manager to open and read the file, and print how many cities were saved.
'''

# with open('cities.txt','w') as file:
#     file.write('Tokyo')
#     file.write('\nParis')
#     file.write('\nNew York')
#     file.write('\nSydney')

count = 0
with open('cities.txt', 'r') as file:
    # solution 1
    # content = file.readlines()
    # for i in content:
    #     count += 1
    # print(f'{count} cities saved')

    # solution 2
    # count = len(file.readlines())
    # print(f'{count} cities saved')

    # solution 3
    # print(f'{len(file.readlines())} cities saved')

    # best solution
    for i in file:
        count += 1
    print(f'{count} cities saved')
    