# -*- coding: utf-8 -*-
import math

def quadratic(a,b,c):
    if not (isinstance(a,(int,float))and isinstance(b,(int,float))and isinstance(c,(int,float))):
        raise TypeError('你输入的是错误的计算对象类型')
    if (b*b-4*a*c)>0:
        x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
        x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
        return x1,x2
    elif (b*b-4*a*c)==0:
        x1 = -b/2*a
        x2 = x1
        return x1,x2
    else:
        print('方程无实根')

print('quadratic(2, 3, 1) =', quadratic(1, 2, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 2, 3))
