def fbi(n):
    if n==2 or n==1:
        return(1)

    else:
        return fbi(n-1)+fbi(n-2)

n = eval(input())
print(fbi(n))