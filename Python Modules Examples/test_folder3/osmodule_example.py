import os 
import shutil
# print(os.getcwd())

CURRENT_PATH = '/home/sakshi/Documents/python-concepts/module_eg/'



# to print the number of items in the current directory
count_of_dir = [i for i in os.listdir()]
# print(len(count_of_dir))





# if not os.path.exists('test_folder'):
#     os.mkdir('/home/sakshi/Documents/python-concepts/module_eg/test_folder')
#     if os.path.isdir('test_folder'):
#         print('folder exists')
#     else:
#         print('folder not found')


FOLDER_PATH = '/home/sakshi/Documents/python-concepts/module_eg/test_folder'





# file is created with name of 'sakshi.txt'
file_name = 'sakshi.txt'
# with open(os.path.join(FOLDER_PATH, file_name), 'w+')as fl:
#     pass




FILE_PATH = '/home/sakshi/Documents/python-concepts/module_eg/test_folder/sakshi.txt'
# if os.path.isfile('/home/sakshi/Documents/python-concepts/module_eg/test_folder/sakshi.txt'):
#     print('file found')
# else:
#     print('file not found')



# change the name of the file from sakshi.txt to new.txt
# os.rename('/home/sakshi/Documents/python-concepts/module_eg/test_folder/sakshi.txt', '/home/sakshi/Documents/python-concepts/module_eg/test_folder/new.txt')




# user_input = input('Which file you want to manipulate: ')
# if os.path.exists(user_input):
#     print('Yes File Found')
# else:
#     print('Oh no... File not Found')



# new file created in module_eg folder 
# new_file = 'stringModule.txt'
# with open(os.path.join(CURRENT_PATH, new_file), 'w+') as fp:
#     pass



# To print files end with '.txt' only
# for i in os.listdir(CURRENT_PATH):
#     if i.endswith('.txt'):
#         print(i)



# show the information of the file
# print(os.stat('osmodule_example.py'))


# os.mkdir('/home/sakshi/Documents/python-concepts/module_eg/test_folder1')
# os.mkdir('/home/sakshi/Documents/python-concepts/module_eg/test_folder3')
# os.rename('/home/sakshi/Documents/python-concepts/module_eg/test_folder', '/home/sakshi/Documents/python-concepts/module_eg/test_folder2')test_folder

# os.remove('stringModule.txt')
# shutil.move('/home/sakshi/Documents/python-concepts/module_eg/module1.py', '/home/sakshi/Documents/python-concepts/module_eg/test_folder1')
# shutil.move('/home/sakshi/Documents/python-concepts/module_eg/module2.py', '/home/sakshi/Documents/python-concepts/module_eg/test_folder1')


# shutil.move('/home/sakshi/Documents/python-concepts/module_eg/osmodule_example.py','/home/sakshi/Documents/python-concepts/module_eg/test_folder3')