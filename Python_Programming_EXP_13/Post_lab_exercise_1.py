lines_list = []
with open("ict.txt", 'r') as f:
    for line in f:
        lines_list.append(line.strip())

print(lines_list) 