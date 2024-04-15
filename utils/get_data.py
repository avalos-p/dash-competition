import json

'''
Importing data
'''

def models_dict(path:str = "./data/modelos_dic.json"):
    with open(path, 'r') as json_file:
        models_dictionary = json.load(json_file)
    return models_dictionary
