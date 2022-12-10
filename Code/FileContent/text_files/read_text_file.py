file_path = 'Code\FileContent\data\sample.txt'

# Read file all at once
'''
f = open(file_path, 'r')
data_list = f.readlines()
f.close()

print(data_list)
print(len(data_list))
'''

# Read file line by line
f = open(file_path, 'r')
for line in f:
    print(line)
