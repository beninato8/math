import numpy as np
import math

class Vector():
    def __init__(self, *args):
        self.pts = list(args)
        self.dim = len(args)
    def __repr__(self):
        return str(self.pts)

class Plane():
    """ax + bx + cz + d = 0"""
    def __init__(self, a, b, c, d):
        self.pts = [a,b,c,d]
    def __repr__(self):
        a,b,c,d = self.pts
        return f'{a}x + {b}y + {c}z + {d} = 0'

def distVecPlane(vec, plane):
    if vec.dim == 3:
        x, y, z = vec.pts
        a,b,c,d = plane.pts
        top = abs(a*x + b*y + c*z + d)
        if int(top) == top:
            top = int(top)
        bottom = math.sqrt(a**2 + b**2 + c**2)
        if int(bottom) != bottom:
            print(f'\\frac{{{top}}}{{\\sqrt{{{a**2 + b**2 + c**2}}}}}')
            bottom = f'sqrt({a**2 + b**2 + c**2})'
        else:
            print(f'\\frac{{{top}}}{{{bottom}}}')
        return f'{top}/{bottom}'

def distPlanePlane(plane1, plane2):
    p1 = plane1.pts
    p2 = plane2.pts
    if any(p1[0]/p2[0] != x for x in [p1[1]/p2[1], p1[2]/p2[2]]):
        print(f'{plane1} is not parallel to\n{plane2}')
        return
    a = p1[0]
    x = -p1[3]/a
    vec = Vector(x,0,0)
    return distVecPlane(vec, plane2)

def dist(a, b):
    if isinstance(a, Vector) and isinstance(b, Plane):
        return distVecPlane(a, b)
    if isinstance(b, Vector) and isinstance(a, Plane):
        return distVecPlane(b, a)
    if isinstance(a, Plane) and isinstance(b, Plane):
        return distPlanePlane(a, b)


a = Vector(1,-8,6)
b = Plane(3, 2, 6, -5)

c = Plane(4, -3, 1, -8)
d = Plane(8, -6, 2, -3)

# print(dist(a,b))
print(dist(c,d))