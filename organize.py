import os
import shutil

from_dir = "C:/Users/gilce/Dropbox/My PC (LAPTOP-E1F3QFJ5)/Downloads"
to_dir = "C:/Users/gilce/Dropbox/My PC (LAPTOP-E1F3QFJ5)/Downloads"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    if extension == '':
        continue
    if extension in ['.xlsx']:
        path1 = from_dir + '/' + file_name                  
        path2 = to_dir + '/' + "Arquivos_Exel"                
        path3 = to_dir + '/' + "Arquivos_Exel" + '/' + file_name
        print("path1 " , path1)
        print("path3 ", path3)

        if os.path.exists(path2):
          print("Movendo " + file_name + ".....")
          shutil.move(path1, path3)
        else:
          os.makedirs(path2)
          print("Movendo " + file_name + ".....")
          shutil.move(path1, path3)