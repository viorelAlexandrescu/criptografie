import numpy as np
from math import sqrt
p = 
q = 
seed = 
m = p * q


def calc_x(k):
    return np.power(k, 2) % m


def bbs():
    x = np.power(seed, 2) % m
    print('0: ', x)
    for i in range(40):
        x = calc_x(x)
        print(i+1, ':', x)


def is_prim(k):
    for i in range(2, int(sqrt(k))+1, 1):
        if k % i == 0:
            return False
    return True


def congruent(k):
    if k % 4 == 3:
        return True
    else:
        return False


# print(is_prim())
# print(congruent())
bbs()