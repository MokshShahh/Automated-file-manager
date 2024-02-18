import os
from shutil import move #becauses the os.rename function does not work with "\" and windows folders are full of them

def organize_files(root):
    """
    function accepts folder path as input and organizes everything within that folder
    it ignores any sub folder within main folder and only organizes files
    """
    root=(r"C:\Users\moksh\OneDrive\Desktop\Test")
    files_dict={}
    for path,dir,files in os.walk(root):
        #print(files)
        for file in files:      #makes a dict where key is file extension and value is a list full of files within folder with same extensions
            name,ext=os.path.splitext(file)
            if ext in files_dict.keys():
                files_dict[ext].append(name)
            else:
                files_dict[ext]=[]
                files_dict[ext].append(name)
            #print(files_dict.keys())
        break
    
    
    #actual sorting part
    for ext in files_dict.keys():
        key=ext.replace("."," ")
        path=os.path.join(root,key)
        os.mkdir(path)      #makes the folder into which all files with same extension go
        for file in files_dict[ext]:
            full=file+ext
            move(os.path.join(root,full),path)  #moves file from main folder into sub folder which was created above
        


if __name__=="__main__":
    folder=input(r"please enter path of folder you would like to organize")
    organize_files(folder)
    




        

