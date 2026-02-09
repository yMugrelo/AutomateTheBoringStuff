import os


for folderName, subfolders, filenames in os.walk('PartI'):
    print("The current folder is " + folderName)

    for subfolder in subfolders: 
        print('Subfolder of  ' + folderName + ': ' + subfolder)