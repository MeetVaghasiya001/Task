import os

# print(os.path.exists(('practice1.py')))
# print(os.path.getsize("practice1.py"))
# os.environ['NAME'] = 'Meet'
# print(os.getenv('NAME'))

# print(os.environ)
# print(os.stat('practice1.py'))



#! Give information about directory
'''
info = os.stat("practice1.py")

print(info.st_size)   # File size (bytes)
print(info.st_mtime)  # Last modified time
print(info.st_ctime)  # Creation time (Windows)
print(info.st_mode)   # File permissions
print(info.st_atime)  #Last Access time 1
'''


#! os.wlak

'''
print(os.path.abspath('practice1.py'))
print(os.path.getsize('practice1.py'))
for root,dirs,files in os.walk('Scripts'):
    print(f'Roots:{root}')
    print(f'Files:{files}')
    print(f'Dirs:{dirs}')
'''
# print(os.name)
# print(os.getcwd())
# print(os.cpu_count())
# print(os.system('python --version'))  # Use to run system commnds

# print(os.listdir())  # List all directory
# os.makedirs('pythonProject/hello') # For create a directory
# os.removedirs('pythonProject/hello') # For remove directory
