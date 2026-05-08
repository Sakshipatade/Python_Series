import os 
import shutil
# import time 

file_categories = {
    'Images' : {
        'extentions':['.png', '.jpg', '.webp', '.jpeg', '.docx'],
        'destination_path':'/Images'
        },
    'Text_files' : {
        'extentions': ['.doc', '.txt', '.pdf', '.PDF', '.odt', '.exe', '.dmg'],
        'destination_path':'/Text_files'
        },
    'Videos' : {
        'extentions':['.mp4'],
        'destination_path':'/Videos'
        },
    'Zipped_Files' : {
        'extentions':['.gz'],
        'destination_path':'/Zipped_Files'
        },
    'Debian_Files' : {
        'extentions':['.deb'],
        'destination_path':'/Debian_Files'
        },
    'Presentation' : {
        'extentions':['.ppt', '.pptx'],
        'destination_path':'/Presentation'
        },
    'Sheets' : {
        'extentions':['.xlsx'],
        'destination_path':'/Sheets'
        }
}


def moveFiles(path:str):

    for i in os.listdir(path):
        file_path = path+"/"+i
        destintion_dir = path + '/Others'

        if os.path.isdir(file_path):
            continue
        
        if os.path.isfile(file_path):
            # print('it is file')
            # ext = pathlib.Path(i).suffix
            _, ext = os.path.splitext(i)
            # print(ext)

            
            if ext in file_categories['Images']['extentions']:
                destintion_dir = path + file_categories['Images']['destination_path']

            elif ext in file_categories['Text_files']['extentions']:
                destintion_dir = path + file_categories['Text_files']['destination_path']
                
            elif ext in file_categories['Videos']['extentions']:
                destintion_dir = path + file_categories['Videos']['destination_path']

            elif ext in file_categories['Zipped_Files']['extentions']:
                destintion_dir = path + file_categories['Zipped_Files']['destination_path']

            elif ext in file_categories['Debian_Files']['extentions']:
                destintion_dir = path + file_categories['Debian_Files']['destination_path']

            elif ext in file_categories['Presentation']['extentions']:
                destintion_dir = path + file_categories['Presentation']['destination_path']
            
            elif ext in file_categories['Sheets']['extentions']:
                destintion_dir = path + file_categories['Sheets']['destination_path']

  
            if not os.path.exists(destintion_dir):
                os.mkdir(destintion_dir)
            shutil.move(file_path, destintion_dir)

    print('done successfully')



if __name__ == "__main__":
    moveFiles('/home/sakshi/Downloads')