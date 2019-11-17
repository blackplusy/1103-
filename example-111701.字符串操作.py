#coding=utf-8
#1.字符串的索引
name='im your baba!!!'
print(name[0])
print(name[3])
print(name[-2])
# print(name[30])
#2.字符串的切片
name='im your baba!!!'
print(name[0:4])
print(name[:4])
print(name[4:])
print(name[3:-1])
tel='0452-8869504'
print(tel[:5])
print(tel[5:])
print(tel[:5]+'6'+tel[5:])
#3.其他操作
#3.1 字符串的拼接
a='lady'
b='gaga'
print(a+b)
print(a+b[-1])
#3.2 字符串的遍历
name='im your papa!!'
for i in name:
    print(i)
#3.3 字符串的去空格
'''
string.strip()  去掉两边的空格
string.lstrip() 去掉左边空格
string.rstrip() 去掉右边空格
'''
str1='    python no.1    '
print(str1)
print(str1.lstrip())
print(str1.rstrip())
#3.4 计算元素个数
str1='    python no.1    '
print(len(str1))
name=input('请输入用户名: ')
if  len(name)==0:
    print('您的输入有误')
else:
    print('您输入的是'+name)
