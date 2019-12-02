import math

def fac(n):
    if n < 2:
        return 1
    return n*fac(n-1)

def sequence(f, a, n, x):
    if x > n:
        return
    print(x, a)
    sequence(f, f(a), n, x+1)

f = lambda x : (1+(4/x))**x
a1 = 3
# print(sequence(f, a1, 5, 1))

for i in range(100000,1000000, 100):
    print(f(i))

print(math.e**4)