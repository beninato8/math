import sys

sys.setrecursionlimit(1000000000)

def get_dy(x, y, dx, dydx, n):
    dy = dydx(x, y) * dx
    return [] if n == 0 else [(x, y)] + get_dy(x+dx, y+dy, dx, dydx, n-1)

def get_dy_to_val(x, y, dx, dydx, val):
    x = float(f'{x:.10f}')
    y = float(f'{y:.10f}')
    dy = dydx(x, y) * dx
    print(x, y)
    if x == val:
        return y
    if x > val:
        return []
    return get_dy_to_val(x+dx, y+dy, dx, dydx, val)

x = 0
dx = .0001
y = 0
dydx = lambda x,y : 2 - (3*y)/(400+2*x)
xIn = 20
print(get_dy_to_val(x, y, dx, dydx, xIn))
