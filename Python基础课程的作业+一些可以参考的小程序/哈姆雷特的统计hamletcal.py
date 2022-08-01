def gettext():
    txt=open("hamlet.txt","r").read()
    txt=txt.lower()
    for ch in '!#%&*+(),-./:;<=>?@[\\]^_{|}~':
        txt=txt.replace(ch,"")
    return txt

hamlettxt=gettext()
words=hamlettxt.split()
counts={} #新建字典类型
for word in words:
    counts[word]=counts.get(word,0)+1
items =list(counts.items())

items.sort(key=lambda x:x[1],reverse=True)
#按照元素键值对的第二个列表进行排序，方式是从大到小
for i in range(10):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))