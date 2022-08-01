import  jieba
txt=open("沉默的羔羊.txt","r",encoding="utf-8").read()
words=jieba.lcut(txt)
counts={}
for word in words:
    if len(word)==1:
        continue
    else:
        counts[word]=counts.get(word,0)+1
maxnumber=0
maxcharater=""

for key in counts:
    if counts[key]> maxnumber:
        maxcharater=key
        maxnumber=counts[key]
    if counts[key]==maxnumber and  key>maxcharater:
        maxcharater=key   ##按照unicode字符 排序
print(maxcharater)
