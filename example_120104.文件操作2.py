#coding=utf-8

file=open('D:\\t.txt','r')
for i in file.readlines():
    i=i.split()
    if i[-1]=='110':
        print('110 is here!')
file.close()
