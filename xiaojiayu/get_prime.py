# 输出小于指定整数的的素数？
import math

def is_prime(num):
    # int i;
    if num <= 1:
        return False;
    else:
        if num == 2:
            return True;
        if num % 2 == 0:
            return False;
        for i in range(3,int(math.sqrt(num))+1,2):
            if num % i == 0:
                return False;
        return True;

'''
def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False
'''
def get_prime(n):
    for i in range(n):
        if is_prime(i):
            print(i,end = ' ')


n = int(input())
get_prime(n)
