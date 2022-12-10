import pickle

pickle_file_path = 'Code\FileContent\data\output.pickle'

f = open(pickle_file_path, 'rb')
output_data = pickle.load(f)
f.close()

print(output_data)
