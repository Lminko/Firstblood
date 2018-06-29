# -*- coding: utf-8 -*-
def sys_tf(f,s,num):
    dec=int(num,f)
    if s==2:
        num='{0:b}'.format(dec)
    if s==8:
        num='{0:o}'.format(dec)
    if s==10:
        num='{0:d}'.format(dec)
    if s==16:
        num='{0:x}'.format(dec)
    return num
index = input('\t欢迎使用进制转换器！按任意按键继续...')
while True:
    print('\t~~~~~~~~~~~~~~\n\t||  主菜单  ||\n\t~~~~~~~~~~~~~~')
    menu=('2  -> 二进制','8  -> 八进制','10 -> 十进制','16 -> 十六进制','0  -> 退出')
    for feature in menu:
        print('\t%s'%feature)
    number=('2','8','10','16')
    d = {'2': '二进制', '8': '八进制', '10': '十进制','16': '十六进制'}
    exit = input('\t~~~~~~~~~~~~~~\n\t按任意键继续,退出请按0...\n\t=============')
    if exit=='0':
            print('\t感谢你的使用，再见！\n')
            break
    order1=input('\t请选择你要输入数字的进制：')
    order2=input('\t请选择你要输出数字的进制：')
    if order1 in number and order2 in number:
        mod1=d[order1]
        mod2=d[order2]
        num1=int(order1)
        num2=int(order2)
    else:
        print('\t输入有误！')
        continue
    while True:
        print('\t*******************************\n\t当前模式：%s==>%s\n\t*******************************' % (mod1,mod2))
        num = input('\t请输入需要转换%s数字：' %mod1)
        n = sys_tf(num1,num2,num)
        print('\t%s数：%s\n\t%s数：%s\t\n\t*******************************' %(mod1,num,mod2,n))
        dex = input('\t按任意键继续转换,按#返回主菜单\n\t')
        if dex=='#':
            break
        else:
            continue

