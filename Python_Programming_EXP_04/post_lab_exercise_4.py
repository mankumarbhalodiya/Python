my_list = [10, 20, 20, 30, 40, 40, 50]
freq = {}
for item in my_list:
    freq[item] = freq.get(item, 0) + 1
print(freq)