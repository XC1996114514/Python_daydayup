f = open("latex.log")
t = f.read()
f.close()

count = 0
d = {}
countnum=0

for word in t:
    if 'a' < word < 'z':
        d[word] = d.get(word, 0) + 1
        countnum=countnum+1

print("共{0}字符，".format(countnum),end='')
print(d)