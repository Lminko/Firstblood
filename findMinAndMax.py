# -*- coding: utf-8 -*-
def findMinAndMax(L):
    if len(L)==0:
        return (None,None)
    else:
        y=x=int(L[0])
        for i in L:
            i=int(i)
            if i<x:
                x=i
            if i>y:
                y=i
        return (x,y)
L = input('输入数列：').strip(' ').split(' ')
print(L)
print(findMinAndMax(L)) 