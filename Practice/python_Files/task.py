import os

#! 1. List all files
'''
data_list = os.listdir()
for dirs in data_list:
    print(dirs)
'''

#! 2. create a folder practice
'''
os.mkdir('Practice')
'''

#! 3. check file
'''
if os.path.exists('practice1.py'):
    print("true!")
else:
    print('No')
'''

#! 4.create a nested folders
'''
os.makedirs('project/data/images')
'''

#! 5.Cretae files in Data folder
'''
with open('project/data/text1.txt','w') as f:
    f.write('Hello')

with open('project/data/text2.txt' ,'w') as e:
    e.write('hii')
'''

#! 6.Rename files
'''
folder = 'project/data'
for filename in os.listdir(folder):
    if filename.endswith(".txt"):
        old_path = os.path.join(folder, filename)
        new_name = "new_" + filename
        new_path = os.path.join(folder, new_name)

        os.rename(old_path, new_path)

print("Renaming done")
'''

#! 7. Delete all txt files from folder
'''
folder = 'project/data'
print(os.listdir(folder))
for file in os.listdir(folder):
    if file.endswith('.txt'):
        os.remove(os.path.join(folder,file))
'''

#8.print file size
'''
info = os.stat('task.py')

print(info.st_size)
'''

#! 9.print all files folders and dirs
'''
folder = 'C:/Users/meet.vaghasiya/PycharmProjects/pythonProject/.venv/project'
print(folder)
for root,dirs,files in os.walk(folder):
    print(f'Root:{root}')
    print(f'dirs:{dirs}')
    print(f'files:{files}')
'''



#! 10.find largest file in directory
'''
folder = 'C:/Users/meet.vaghasiya/PycharmProjects/pythonProject/.venv'
file_size = 0
max_file = ''
for root,dirs,files in os.walk(folder):
    for file in files:
        full_path = os.path.join(root,file)
        size = os.path.getsize(full_path)

        if size > file_size:
            file_size = size
            max_file = full_path

print(f'largest file :{max_file}')
print(f'file size:{round(file_size / (1024 * 1024),2)} MB')
'''

#! 11.File organizor
'''
folder = "C:/Users/meet.vaghasiya/meet"
add_folder = 'Practice/python_Files'
os.makedirs('Practice/python_Files',exist_ok=True)

print(os.listdir(folder))
for root,dirs,files in os.walk(folder):
    print(files)
    for file in files:
        if file.endswith('.py'):
            source_path = os.path.join(root,file)
            chang_path = os.path.join(add_folder,file)

            os.rename(source_path,chang_path)
    print('Done!')
'''

#! Count files in each directory
'''
folder = "C:/Users/meet.vaghasiya/Meet"

if not os.path.exists(folder):
    print("Wrong directory!")
else:
    files_name=[]
    for item in os.listdir(folder):
        item_path = os.path.join(folder,item)

        file_count = 0 
        if os.path.isdir(item_path):
            for root,dirs,files in os.walk(item_path):
                file_count += len(files)
            print(f'{files}-->{file_count}')
        else:
            if os.path.isfile(item):
                file_count += 1
                files_name.append(item)
    print(f'{files_name}-->{file_count}')
'''











