#coding=utf-8
#1.find和index
#find
a='c'
str1='aabbcc'
print(str1.find(a))
a='d'
print(str1.find(a))
a='b'
print(str1.find(a))
#index
a='b'
print(str1.index(a))
a='d'
# print(str1.index(a))
#2.isalphpa和isdigt
#isalpha
a='simida'
print(a.isalpha())
a='1simida'
print(a.isalpha())
#isdigit
a='123'
print(a.isdigit())
a='123a'
print(a.isdigit())
#3.join
s1='+'
s2='a','b','c' #元组类型
print(s2)
s=s1.join(s2)
print(type(s))
print(s)
#4.upper和lower
name='Apple'
print(name.upper())
print(name.lower())
#5.startswith和endswith
a='aabbcc'
print(a.startswith('a'))
print(a.startswith('d'))
print(a.endswith('c'))
print(a.endswith('d'))
#6.count replace split
#count
name='HeygorGaGa'
print(name.count('a'))
print(name.count('h'))
#replace
print(name.replace('g','memeda'))
#split
name='1,2,3,4'
b=name.split(',')
print(b)
#7.引号
print('heygor is handsome!!')
print("shit!!!")
print('''你瞎了么？''')
# print('i'm your baba! ')
print('i\'m your mom!!!')
print("i'm your papa!!")
print('您是"郭德纲"么？')
print('heygor')
print('18')
print('---')
print('''
heygor
18
''')
'''
这段文字没有执行
'''

