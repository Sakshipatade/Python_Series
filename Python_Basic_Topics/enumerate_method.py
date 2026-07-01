# syntax: enumerate(iterable, start=0) 0 is by default index we can change it by changing the start number as per our own

colors = ['red', 'green', 'blue']
for index, color in enumerate(colors):
    print(index, color)



students = ('amit', 'priya', 'rahul', 'reena', 'lekha', 'nandini', 'jitesh', 'shamini')
for index, student in enumerate(students, start = 1):
    print(f'{index}. {student}')




try:
    fruits = ["apple", "banana", "mango", "orange"]
    for index, fruit in enumerate(fruits):
        print(fruits[5])
except IndexError:
    print('index is out of range')




numbers = [10, 20, 30, 40, 50, 60]
for index, num in enumerate(numbers):
    if index % 2 == 0:
        print(f'{index} {num}')






word = 'python'
for i, char in enumerate(word):
    print(i, char)




# create a dictionary
subjects = ["Math", "Science", "English"]


dictionary = {}
for i, sub in enumerate(subjects):
    dictionary[i] = sub
print(dictionary)


# OR dictionary comprehension
result = {i:sub for i, sub in enumerate(subjects)}
print(result)




nums = [5, 10, 15, 20, 25]
for index, num in enumerate(nums):
    if num > 12:
        print(index)

