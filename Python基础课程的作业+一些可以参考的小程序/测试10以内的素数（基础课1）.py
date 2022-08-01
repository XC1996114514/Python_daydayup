import math


def whether_prime(number):
    sqrt = int(math.sqrt(number))
    for j in range(2, sqrt + 1):
        if number % j == 0:
            print(number,'equals',j,'*',number//j)
            return False
    return True


def give_all_num(number):
    for i in range(2, number):
        if whether_prime(i) is True:
            print(i,'is a prime number')


if __name__ == "__main__":
    give_all_num(10)
