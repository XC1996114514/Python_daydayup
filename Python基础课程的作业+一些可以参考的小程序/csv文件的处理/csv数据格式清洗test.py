f=open("data.csv")
line=f.readlines()

line.reverse()
print(line)
for l in line:
    l = l.replace('\n', '')
    l = l.replace(' ', '')
    ls=l.split(",")
    ls=ls[::-1]
    print(";".join(ls))