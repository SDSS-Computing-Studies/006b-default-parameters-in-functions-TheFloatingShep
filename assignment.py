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

def cosineLaw(a,b,c,d):
    return "jeff"
def toRadians():
    return "jeff"
def solution():
    return "jeff"
def quadratic():
    return "jeff"

a = int(input("Enter side A\n"))
b = int(input("Enter side B\n"))
c = int(input("Enter side C\n"))
if a >= b and a >= c:
    C = a
    B = b
    A = c
if b >= a and b >= c:
    C = b
    B = a
    A = c
if c >= b and c >= a:
    C = c
    B = b
    A = a
if A > B:
    B2 = A
    A2 = B
else:
    B2 = B
    A2 = A
An = str(A2)
Bn = str(B2)
Cn = str(C)
if (A2**2) + (B2**2) == (C**2):
    print(An + "," + Bn + "," + Cn + " form a Pythagorean triple")
else:
    print(An + "," + Bn + "," + Cn + " do not form a Pythagorean triple")