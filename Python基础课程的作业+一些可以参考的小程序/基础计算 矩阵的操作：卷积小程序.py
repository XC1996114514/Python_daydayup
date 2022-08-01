from fractions import Fraction

def core_convolution(a, b):
    lena = len(a)
    lenb = len(b)
    length = lena + lenb-1
    c = []

    for num in range(length):
        d=0
        for num1 in range(lena):
            if (num - num1 < 0) or (num - num1 > lenb-1):
                continue
            else:
                temp = b[num-num1]
                d=d+ Fraction(a[num1] * temp)

        c.append(d)

    return c


if __name__ == '__main__':
    a = [1/3,1/3,1/3]
    b = [1/3,1/3,1/3]

c = core_convolution(a, b)
print(c)

d= core_convolution(c,a)
print(d)
