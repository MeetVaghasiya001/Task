from datetime import datetime
import json
import os

def create_month(base_dir,start_date,end_date):
    month_folder = f'01-{start_date.month}-{start_date.year}'
    folder_path = os.path.join(base_dir,month_folder)
        
    os.makedirs(folder_path,exist_ok=True)
    return folder_path


def text_file(folder_path,filename,info):
    txt_path = os.path.join(folder_path,'01.txt')
    with open(txt_path,'w') as f:
        f.write(f'File Size:{info.st_size}'+'\n')
        f.write(f'File Type:{info.st_mode}'+'\n')
        f.write(f'File Create:{datetime.fromtimestamp(info.st_ctime)}'+'\n')
        f.write(f'File Updated:{datetime.fromtimestamp(info.st_mtime)}'+'\n')
    return txt_path

def json_file(folder_path,filename,info):
    json_path = os.path.join(folder_path,'02.json')
    data = {
            'File Size':info.st_size,
            'File Type':info.st_mode,
            'File Meta Data':{
                'File Created At':datetime.fromtimestamp(info.st_ctime),
                'File Updated At':datetime.fromtimestamp(info.st_mtime)
            }
        }
    with open(json_path,'w') as f:
        json.dump(data,f,indent=4,default=str)
    return json_path

def html_file(folder_path,filename,info):
    html_path = os.path.join(folder_path,'03.html')
    with open(html_path,'w') as f:
        f.write(f'''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
            </head>
            <body>
                <p>File Size:{info.st_size}</p>
                <p>File Type:{info.st_mode}</p>
                <p>File Created At:{datetime.fromtimestamp(info.st_ctime)}</p>
                <p>File Updated At:{datetime.fromtimestamp(info.st_mtime)}</p>
            </body>
            </html>
            ''')
    return html_path


def remove_files(base_dir):
    for month_folder in os.listdir(base_dir):
        month_path =os.path.join(base_dir,month_folder)
        
        if os.path.exists(month_path):
            for day_folder in os.listdir(month_path):
                day_folder_path = os.path.join(month_path,day_folder)

                if os.path.exists(day_folder_path):

                    for files in os.listdir(day_folder_path):
                        file_path = os.path.join(day_folder_path,files)
                        
                        if os.path.exists(file_path):
                            os.remove(file_path)
    print('All Done👍👍👍')



       




