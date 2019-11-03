#coding=utf-8
str1="kang sang simida!"

for i in str1:
    print(i)

tup=('heygor','kobe','ladeng')
for a in tup:
    print(a)

#函数range（）  范围
#range(10)    0-9
#range(1,10)  1-9
for i in range(10):
    print(i)
print('*'*10)
for i in range(1,10):
    print(i)
print('*'*10)
#循环嵌套
tup=('heygor','kobe','ladeng')
for a in tup:
    for b in a:
        print(b)
