#第四行可能会少打个空格
str=input()
for i in range(0,len(str)):
    if str[i]==' ':
        print(' ',end="")
    elif str[i] in ['x','y','z','X','Y','Z']:
        print(chr(ord(str[i])-23),end='')
    elif str[i] in['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w'\
                   'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W']:
        print(chr(ord(str[i])+3),end='')
    elif str[i] in['w']:
        print("z", end='')
    elif str[i] in["W"]:
        print("Z",end='')
    else:
        print(str[i],end='')

