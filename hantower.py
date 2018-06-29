# -*- coding: utf-8 -*-
def move(x,y):
    print(x,'-->',y)
def hantower(n,a,b,c):
    if n == 1:
        move(a,c)
    else:
        hantower(n-1,a,c,b)
        move(a,c)
        hantower(n-1,b,a,c)
n = int(input('输入盘子的数量：'))
print('移动顺序：')
hantower(n,'A','B','C')
