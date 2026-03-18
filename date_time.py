import task_modules
from datetime import datetime,timedelta
import os

def date_task():
    dir_path ='C:/Users/meet.vaghasiya/meet/data_time'

    today_date = datetime.now()
    end_date = datetime(2026,12,31,23,59,59)

    current_date = today_date
    while current_date <= end_date:
        folder_path = task_modules.create_month(dir_path,current_date,end_date)

        date_folder = current_date.strftime('%d-%m-%y')
        date_path = os.path.join(folder_path,date_folder)
        os.makedirs(date_path,exist_ok=True)
        info = os.stat(date_path)

        #for txt file 
        task_modules.text_file(date_path,'01.txt',info)

        #for json file
        task_modules.json_file(date_path,'02.json',info)

        #for html file 
        task_modules.html_file(date_path,'03.html',info)

        current_date += timedelta(days=1)

    print('Task Completed 👍')

# date_task()

# task_modules.remove_files('C:/Users/meet.vaghasiya/meet/data_time')
# task_modules.html_file_move()

def move_html():
    base_dir = 'C:/Users/meet.vaghasiya/meet/data_time'
    html_dir ='C:/Users/meet.vaghasiya/meet/HTML'
    json_dir ='C:/Users/meet.vaghasiya/meet/JSON'
    os.makedirs(html_dir,exist_ok=True)
    
    for all_dirs in os.listdir(base_dir):
        html_month_path = os.path.join(html_dir,all_dirs)
        json_month_path = os.path.join(json_dir,all_dirs)
        date_urls = os.path.join(base_dir,all_dirs)
        os.makedirs(html_month_path,exist_ok=True)
        os.makedirs(json_month_path,exist_ok=True)
        
        for date_dir in os.listdir(date_urls):
            html_date_path = os.path.join(html_month_path,date_dir)
            json_date_path = os.path.join(json_month_path,date_dir)
            os.makedirs(html_date_path,exist_ok=True)
            os.makedirs(json_date_path,exist_ok=True)
            file_paths = os.path.join(date_urls,date_dir)
            

            for files in os.listdir(file_paths):
                
                file_url = os.path.join(file_paths,files)
                html_replace_url = os.path.join(html_date_path,files)
                json_replace_url = os.path.join(json_date_path,files)
                if file_url.endswith('.html'):
                    os.rename(file_url,html_replace_url)
                elif file_url.endswith('.json'):
                    os.rename(file_url,json_replace_url)
            
move_html()


