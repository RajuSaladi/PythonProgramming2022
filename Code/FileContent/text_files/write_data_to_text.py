data_list = ['OpenKnowledgeShare', 'Python', 'Programming 2022']

file_path = 'Code\FileContent\data\output.txt'
f = open(file_path, 'w')
# f.writelines([this_line+'\n' for this_line in data_list])
f.write('This is awesome!!!')
f.close()

