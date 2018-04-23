from numpy import *
import string

key = [0, 1, 0, 1, 0, 0, 0, 0,
       0, 1, 0, 0, 0, 0, 0, 1,
       0, 1, 0, 1, 0, 0, 1, 1,
       0, 1, 0, 1, 0, 0, 1, 1,
       0, 1, 0, 1, 0, 1, 1, 1,
       0, 1, 0, 0, 1, 1, 1, 1,
       0, 1, 0, 1, 0, 0, 1, 0,
       0, 1, 0, 0, 0, 1, 0, 0]

key2 = [0, 0, 0, 1, 0, 0, 1, 1,
        0, 0, 1, 1, 0, 1, 0, 0,
        0, 1, 0, 1, 0, 1, 1, 1,
        0, 1, 1, 1, 1, 0, 0, 1,
        1, 0, 0, 1, 1, 0, 1, 1,
        1, 0, 1, 1, 1, 1, 0, 0,
        1, 1, 0, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 0, 0, 0, 1]


PC1 = [57, 49, 41, 33, 25, 17, 9,
       1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27,
       19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15,
       7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29,
       21, 13, 5, 28, 20, 12, 4]

PC2 = [14, 17, 11, 24, 1, 5,
       3, 28, 15, 6, 21, 10,
       23, 19, 12, 4, 26, 8,
       16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55,
       30, 40, 51, 45, 33, 48,
       44, 49, 39, 56, 34, 53,
       46, 42, 50, 36, 29, 32]


perm = []

for i in range(len(PC1)):
    perm.append(key[PC1[i]-1])

C0 = perm[:28]
D0 = perm[28:]


def shift1(arr):
    hold = zeros(28, dtype=int16)
    for k in range(28-1):
        hold[k] = arr[k+1]
    hold[27] = arr[0]
    return hold


def shift2(arr):
    hold = zeros(28, dtype=int16)
    for k in range(28-2):
        hold[k] = arr[k+2]
    hold[26] = arr[0]
    hold[27] = arr[1]
    return hold


C = zeros((17, 28), dtype=int)
D = zeros((17, 28), dtype=int)
K = zeros((17, 48), dtype=int)
C[0] = array(C0)
D[0] = array(D0)
extra = zeros(56, dtype=int)

for i in range(1, 17, 1):
    if i == 1 or i == 2 or i == 9 or i == 16:
        C[i] = shift1(C[i-1])
        D[i] = shift1(D[i-1])
        extra[:28] = C[i]
        extra[28:] = D[i]
        for j in range(48):
            K[i][j] = extra[PC2[j]-1]
    else:
        C[i] = shift2(C[i-1])
        D[i] = shift2(D[i-1])
        extra[:28] = C[i]
        extra[28:] = D[i]
        for j in range(48):
            K[i][j] = extra[PC2[j]-1]

L = K.reshape((17, 6, 8))

for i in range(1, 17, 1):
    cfg = ''
    print("%d:" % i)
    for j in range(6):
        L2 = L[i][j].tolist()
        b = "".join(str(g) for g in L2)
        cfg = cfg+" "+str(hex(int(b, 2)))
    print(cfg)