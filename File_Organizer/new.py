import os 
import shutil
PATH = '/home/sakshi/Documents/python-concepts/File_Organizer'
print(os.getcwd())

file1 = 'file1.txt'
file2 = 'file2.txt'
file3 = 'file3.doc'
file4 = 'file4.pdf'
file5 = 'file5.pdf'


with open(os.path.join(PATH, file1), 'w+')as f1:
    pass
with open(os.path.join(PATH, file2), 'w+')as f2:
    pass
with open(os.path.join(PATH, file3), 'w+')as f3:
    pass
with open(os.path.join(PATH, file4), 'w+')as f4:
    pass
with open(os.path.join(PATH, file5), 'w+')as f5:
    pass

