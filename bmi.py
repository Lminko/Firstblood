# -*- coding: utf-8 -*-

height = float(input('please input your height(/m): ')) 
weight = float(input('please input your weight(/kg): ')) 
bmi = weight/(height*height)*1.0
b = round(bmi,1)
print('your BMI index :%.1f' % b)
if b < 18.5:
    print('过轻')
elif b < 25:
    print('正常')
elif b < 28:
    print('过重')
elif b < 32:
    print('肥胖')
else:
    print('严重肥胖')
