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
    "level1": {
        "level2": {
            "level3": {
                "level4": [
                    {"value": 10},
                    {"value": 20},
                    {"value": [1, 2, {"deep": "yes"}]}
                ]
            }
        }
    }
}

# def check_data(data):
#     if type(data) == dict:
#         return {key:check_data(vlaue) for key,vlaue in data.items()}
#     elif type(data) == list:
#         return [check_data(item) for item in data]
#     else:
#         return type(data).__name__.upper()
# print(check_data(data3))

def get_keys(data):
    if type(data) == dict:
        result = []
        return {get_keys(key):vlaues for key,vlaues in data.items()}
    else:
        return data3.keys()
    
    
print(get_keys(data3))        