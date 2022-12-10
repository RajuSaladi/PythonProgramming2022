file_path = 'Code\FileContent\data\output_append.txt'

data_list = ['first', 'second', 'third', 'hgha;h;oiahoia']

# f = open(file_path, 'a')
# f.writelines([this_line+'\n' for this_line in data_list])
# f.close()

f = open(file_path, 'a')
f.write('This is new line being appended')
f.close()
