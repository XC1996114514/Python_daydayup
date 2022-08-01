
for i in range(100,1000):

    a=int((i)/100)
    b=int((i%100)/10)
    c=int(i%10)
    if pow(a,3)+pow(b,3)+pow(c,3)==i:

        print("{0},".format(i),end='')



##f=[]

##or i in range(100,1000):

    ## a=int((i)/100)
    ## b=int((i%100)/10)
    ## c=int(i%10)
        ## if pow(a,3)+pow(b,3)+pow(c,3)==i:
        ##f.append(i)

##print(', '.join(str(i) for i in f))