
def rvs(s):
    if s=="":
        return  s
    else:
        return rvs(s[1:])+s[0]

string=input()
string=rvs(string)

print(string)