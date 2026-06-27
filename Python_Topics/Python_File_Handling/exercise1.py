fileLocation = '/home/sakshi/Documents/python-concepts/Python_Topics/Python_File_Handling/obama_speech.txt'

with open(fileLocation) as f:
    content = f.readlines()
    
    for row in content:
        total = content.count(row)
        print(total)

