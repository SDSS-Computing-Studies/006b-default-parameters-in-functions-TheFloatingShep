#! python3

import math

def tempConversion(x,unit):
    if unit == "F":
        return float(round(((x - 32) * (5/9)), 1))
    else:
        return float(round(((x * (9/5)) + 32), 1))

def factorPair(x,y):
    lis = [y]
    lis.append((x/y))
    lis.sort()
    return lis

def cosineLaw(a,b,C,oppositeSide):
    if oppositeSide == True:
        c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(toRadians(C)))
        return c
    elif oppositeSide == False:
        n = quadratic((b**2) , (2 * a * math.cos(toRadians(C))) , (a**2)-(C**2))
        return solution(n)
def toRadians(x):
    return (x * math.pi) / 180
def solution(n):
    if n[0] < 0:
        return n[1]
    else:
        return n
def quadratic(a,b,c):
    sols = [((-b + (math.sqrt((b**2) - 4 * a * c))) / (2 * a)),((-b - (math.sqrt((b**2) - 4 * a * c))) / (2 * a))]
    sols.sort()
    return sols
print(cosineLaw(3,2,25,False))