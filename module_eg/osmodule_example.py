import os 
# print(os.getcwd())

# to print the number of items in the current directory
count_of_dir = [i for i in os.listdir()]
# print(len(count_of_dir))

PATH = '/home/sakshi/Documents/python-concepts/module_eg/'


if not os.path.exists('test_folder'):
    os.mkdir('/home/sakshi/Documents/python-concepts/module_eg/test_folder')
    if os.path.isdir('test_folder'):
        print('folder exists')
    else:
        print('folder not found')


FOLDER_PATH = '/home/sakshi/Documents/python-concepts/module_eg/test_folder'
file_name = 'sakshi.txt'


with open(os.path.join(FOLDER_PATH, file_name), 'w+')as fl:
    pass

FILE_PATH = '/home/sakshi/Documents/python-concepts/module_eg/test_folder/sakshi.txt'
if os.path.isfile(FILE_PATH):
    print('file found')
else:
    print('file not found')

    