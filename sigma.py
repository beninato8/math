start = 1
stop = 10000000
import math

f = lambda x : 1/(9*x)
s = 0
for i in range(start, stop+1):
    s += f(i)

print(s)