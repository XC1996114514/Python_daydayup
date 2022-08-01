def prime(m):
    Prime = True
    if m < 2:
        Prime = False
    elif m > 2:
        for i in range(2, m):
            if m % i == 0:
                Prime = False
                break
    return Prime



n=eval(input())
if isinstance(n,float):
    n=int(n)+1
count=0
primes=[]
while count <5:
    if prime(n):
        primes.append(str(n))
        count+=1
    n+=1

print(",".join(primes))  #输出中间有逗号
