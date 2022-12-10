import json

json_file_path = 'Code\FileContent\data\cars.json'

f = open(json_file_path, 'r')
json_data = json.load(f)
f.close()

print(len(json_data))
print(json_data[10])