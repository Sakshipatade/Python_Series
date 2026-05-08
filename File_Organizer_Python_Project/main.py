import os 
import shutil
# import pathlib

PATH = '/home/sakshi/Documents/python-concepts/File_Organizer'

file1 = 'file1.txt'
file2 = 'file2.txt'
file3 = 'file3.doc'
file4 = 'file4.pdf'
file5 = 'file5.pdf'

# below files are created after moving above files into sub-folders successfully and 
# Ignore the code or files below if you newly open this file

file6 = 'file6.txt'
file7 = 'file7.pdf'
file8 = 'file8.pdf'
file9 = 'file9.doc'
file10 = 'file10.doc' 

file11 = 'file11.doc'
file12 = 'file12.txt'

# with open(os.path.join(PATH, file1), 'w+')as f1:
#     pass
# with open(os.path.join(PATH, file2), 'w+')as f2:
#     pass
# with open(os.path.join(PATH, file3), 'w+')as f3:
#     pass
# with open(os.path.join(PATH, file4), 'w+')as f4:
#     pass
# with open(os.path.join(PATH, file5), 'w+')as f5:
#     pass



# with open(os.path.join(PATH, file6), 'w+')as f6:
#     pass
# with open(os.path.join(PATH, file7), 'w+')as f7:
#     pass
# with open(os.path.join(PATH, file8), 'w+')as f8:
#     pass
# with open(os.path.join(PATH, file9), 'w+')as f9:
#     pass
# with open(os.path.join(PATH, file10), 'w+')as f10:
#     pass


# with open(os.path.join(PATH, file11), 'w+')as f11:
#     pass
# with open(os.path.join(PATH, file12), 'w+')as f12:
#     pass


file_categories = {
    'Images' : ['.png', '.jpg', '.webp'],
    'Text_files' : ['.doc', '.txt', '.pdf'],
    'Videos' : ['.mp4']
}

for i in os.listdir(PATH):
    if os.path.isdir(i):
        continue

    if os.path.isfile(i):
        # ext = pathlib.Path(i).suffix
        _, ext = os.path.splitext(i)
        # print(ext)

        
        if ext in file_categories['Images']:

            Image_Directory_path = '/home/sakshi/Documents/python-concepts/File_Organizer/Images'

            if not os.path.exists('/home/sakshi/Documents/python-concepts/File_Organizer/Images'):
                os.mkdir('/home/sakshi/Documents/python-concepts/File_Organizer/Images')
            elif os.path.exists('/home/sakshi/Documents/python-concepts/File_Organizer/Images'):
                shutil.move(i, Image_Directory_path)
            else:
                continue
            
        elif ext in file_categories['Text_files']:

            Text_Files_Directory_Path = '/home/sakshi/Documents/python-concepts/File_Organizer/Text_files'

            if not os.path.exists('/home/sakshi/Documents/python-concepts/File_Organizer/Text_files'):
                os.mkdir('/home/sakshi/Documents/python-concepts/File_Organizer/Text_files')
            elif os.path.exists('/home/sakshi/Documents/python-concepts/File_Organizer/Text_files'):
                shutil.move(i,Text_Files_Directory_Path)
            else:
                continue
        
        elif ext in file_categories['Videos']:

            Videos_Directory_Path = '/home/sakshi/Documents/python-concepts/File_Organizer/Videos'

            if not os.path.exists('/home/sakshi/Documents/python-concepts/File_Organizer/Videos'):
                os.mkdir('/home/sakshi/Documents/python-concepts/File_Organizer/Videos')
            elif os.path.exists('/home/sakshi/Documents/python-concepts/File_Organizer/Videos'):
                shutil.move(i, Videos_Directory_Path)
            else:
                continue
        
        else:
            # if ext == '.md':
            #     continue

            # Other_Files_Directory = '/home/sakshi/Documents/python-concepts/File_Organizer/Others'

            # if not os.path.exists('/home/sakshi/Documents/python-concepts/File_Organizer/Other_files'):
            #     os.mkdir('/home/sakshi/Documents/python-concepts/File_Organizer/Others')
            # if os.path.exists('/home/sakshi/Documents/python-concepts/File_Organizer/Others'):
            #     shutil.move(i, Other_Files_Directory)
            # else:
            #     break
            continue

