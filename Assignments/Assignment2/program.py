a = [1, 2, 3, 4, 0, -1, 10]
b = [10, 20, 3, 40, 5, 2, 20]

output_list = []
for i in range(0, len(a)):
    c = b[i]/a[i] 
    if c > 0:
        output_list.append(c)
    else:
        break
print("output_list", output_list)
