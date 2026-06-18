file_location = '/home/sakshi/Documents/python-concepts/Python_Topics/Python_File_Handling/example.txt'

f = open(file_location)
# output = f.readline()            # type => <class 'str'>
# output = f. read(10)             # type => <class 'str'>
output = f. readlines(10)          # type => <class 'list'>
print(output)
# print(type(output))


# same technique but it closes the file automatically 
with open(file_location) as f:
    output = f.read()
    print(output)



with open(file_location, 'a') as file:
    # file.write('this is the first paragraph')
    file.write('this is the second paragraph')

