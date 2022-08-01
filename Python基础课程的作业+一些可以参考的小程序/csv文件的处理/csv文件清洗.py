f = open("data.csv")
ls = f.readlines()
ls = ls[::-1]
lt=[]
for line in ls:
    line=line.replace("\n","")
    line.replace(" ","")
    lt=line.split(",")
    lt.reverse()
    print(";".join(lt))
f.close
