import os


def move_html():
    base_dir = 'C:/Users/meet.vaghasiya/meet/os-and-datetime/data_time'
    html_dir ='C:/Users/meet.vaghasiya/meet/os-and-datetime/data_time/HTML'
    json_dir ='C:/Users/meet.vaghasiya/meet/os-and-datetime/data_time/JSON'
    
    for all_dirs in os.listdir(base_dir):
        html_month_path = os.path.join(html_dir,all_dirs)
        json_month_path = os.path.join(json_dir,all_dirs)
        date_urls = os.path.join(base_dir,all_dirs)
        
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