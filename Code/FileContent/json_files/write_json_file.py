import json

file_path = 'Code\FileContent\data\output.json'

data_dict1 = {
    'name': 'Python',
    'type': 'Programming',
    'year': 2022
}

data_dict2 = {
    'name': 'OpenKnowledgeShare',
    'type': 'Youtube Channel',
    'year': 2020
}

data_list = []
data_list.append(data_dict1)
data_list.append(data_dict2)

f = open(file_path, 'w')
json.dump(data_list, f)
f.close()
