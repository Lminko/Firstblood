# -*- coding: utf-8 -*-
def trim(s):
    if (s[:1] == ' '):
        return trim(s[1:])
    elif (s[-1:] == ' '):
        return trim(s[:-1])
    else:
        return s
s = input('输入字符串：')
s1 = trim(s)
print(s,'|')
print(s1,'|')