# -*- coding: utf-8 -*-
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
input('按任意键继续...')
while True:
    n = int(input('输入n:'))
    print(fact(n))
    dex = input('退出请按0\n继续请按任意键...')
    if dex == '0':
        print('感谢使用，再见！')
        break
    else:
        continue