f = open("data.csv")
ls=f.readlines()

ls=[]

for line in f:
    line=line.replace("\n","")
    line=line.replace(" ",'')
    ls.append(line.split(","))

#以， 隔开

f.close()

for i in ls[::-1]:
    for j in i[::-1]:
        if j==i[0]:
            print("{}".format(j),end="")
        else:
            print("{}".format(j),end=";")
print()