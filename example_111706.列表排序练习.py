#coding=utf-8
#索引  0  1  2  3  4  5
#索引  -6 -5 -4 -3 -2 -1
#索引从左到右实现方法
a='abcdef'
for i in range(6):
    print(a[6-i-1],end="")
a=input('请输入一个字符串')
for i in range(len(a)):
    print(a[len(a)-1-i],end="")
#索引从右到左实现方法
a='abcd'
for i in range(1,5):
    print(a[-i],end="")
a=input('请输入一个字符串')
for i in  range(1,len(a)+1):
    print(a[-i],end="")

