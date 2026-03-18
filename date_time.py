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


