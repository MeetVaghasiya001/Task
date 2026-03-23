# all_data = {
#     "NAME": "BHARGAV",
#     "AGE": 25, 
#     "INTERESTS": [
#             "GAMING", "EATING OUT", "MOVIE"
#                 ], 
#     "ADDRESS":{
#             "CITY": "AHMEDABAD", "STATE": "GUJARAT"
#               }
#     }


# def data_type(data):
#     if type(data) == dict:
#         return {key: data_type(value) for key, value in data.items()}
#     elif type(data) == list:
#         return [data_type(item) for item in data]
#     else:
#         return type(data).__name__.upper()
    
# print(data_type(all_data))

data3 = {
    'one':1,
    'two':{
        'two_1':1,
        'two_2':{
            'two_2_1':1
        }
    },
    'three':3,
    'four':4
}

# def check_data(data):
#     if type(data) == dict:
#         return {key:check_data(vlaue) for key,vlaue in data.items()}
#     elif type(data) == list:
#         return [check_data(item) for item in data]
#     else:
#         return type(data).__name__.upper()
# print(check_data(data3))

def get_keys(data,all_keys=None):
    if all_keys == None:
        all_keys =[]

    if type(data) == dict:
        for k,v in data.items():
            all_keys.append(k)
            get_keys(v,all_keys)
    
    elif type(data) == list:
        for item in data:
            get_keys(item,all_keys)
    
    return all_keys,len(all_keys)

# print(get_keys(data3)) 

print('----------------------------------')

def all_valaues(data,all_val=None):
    if all_val == None:
        all_val = []
    
    if type(data) == dict:
        for v in data.values():
            all_valaues(v,all_val)
    
    elif type(data) == list:
        for item in data:
            all_valaues(item,all_val)
    else:
        all_val.append(data)

    return all_val

# print(all_valaues(data3))

def get_int(data,int_val=None,depth=0,max_depth =2):
    if int_val == None:
        int_val = []
    if depth > max_depth:
        return 0
    print(depth)
    if type(data) == dict:
        for v in data.values():
            get_int(v,int_val,depth + 1)

    elif type(data) == list:
        for item in data:
            get_int(item,int_val,depth + 1)

    elif type(data) == int:
        int_val.append(data)

    return int_val
print(get_int(data3))