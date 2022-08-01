
path = "case_data_index.txt"
file = open(path, encoding='UTF-8', errors='ignore')
#print(file.read())

lines = file.readlines()
count = 0
for items in lines:
    if  items.find('卖淫') != -1 and items.find('上海') != -1:
        count += 1
        print(items)
print(count)
#print(len(lines))  有多少行代码 多少个案件