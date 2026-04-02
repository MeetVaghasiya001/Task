import json 


with open('htm files\8a58ce72f2fd04fa4199cc9743737e10_targated.html','r',encoding='utf-8') as f:
    data = f.read()

data = json.loads(data)

clean_data = json.loads(data)

with open('clean html/clean1.json','w') as f:
    json.dump(clean_data,f,indent=4,default=str)


with open('htm files\8a64fc4de53198e74a1be5fb90bf4dd1_compatitor.html','r',encoding='utf-8') as f:
    data = f.read()

data = json.loads(data)

clean_data = json.loads(data)

with open('clean html/clean2.json','w') as f:
    json.dump(clean_data,f,indent=4,default=str)