# coding UTF-8

from numpy.random import *

def Uniform():
    return rand()

def Func(a):
    return a**3 + 2*a**2 -5*a +6  # 関数は適当

def rand_normal():
    #print(randn())
    return randn()

x = Uniform()
t = 0

fx = Func(t)

while abs(fx) > 0.0001 and t <= 100:
    t = t + 1
    y = x + rand_normal()

    p = Uniform()

    r = Uniform()

    if r < p:
        x_next = y
    else:
        x_next = x

    fx = Func(x_next)
    print(fx)
    x=x_next
