import os
import time


def create_task():
    for i in range(ord('A'),ord('Z')+1):
        folder_name=chr(i)

        folder_path=os.path.join("C:/Users/meet.vaghasiya/meet/Task",folder_name)
        os.makedirs(folder_path,exist_ok=True)

        for j in range(0,10):
            filename=f"{folder_name}{j}.txt"
            filepath=os.path.join(folder_path,filename)

            with open(filepath,"w") as f:
                for n in range(1,11):
                    f.write(str(n) + "\n")

def remove_files(dir):
    for folder in os.listdir(dir):
        folder_path =os.path.join(dir,folder)
        
        if os.path.exists(folder_path):
            for files in os.listdir(folder_path):
                file_path= os.path.join(folder_path,files)
                os.remove(file_path)

    print('All file remove Succesfully!')
remove_files('C:/Users/meet.vaghasiya/meet/Task')