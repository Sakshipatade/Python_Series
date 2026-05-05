import os 
# print(os.getcwd())

# to print the number of items in the current directory
count_of_dir = [i for i in os.listdir()]
# print(len(count_of_dir))


if not os.path.exists('test_folder'):
    os.mkdir('test_folder')
    if os.path.isdir('test_folder'):
        print('folder exists')
    else:
        print('folder not found')

