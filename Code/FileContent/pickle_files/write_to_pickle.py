import pickle

pickle_file_path = 'Code\FileContent\data\output.pickle'
data_list = [1, 2, 3, 4, 5,6]
data_dict = {
    'name': 'OpenKnowledgeShare',
    'type': 'Youtube Channel',
    'year': 2020
}

input_data = [data_list, data_dict, 100, 200, 'sample_string']
f = open(pickle_file_path, 'wb')
pickle.dump(input_data, f)
f.close()
