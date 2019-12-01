#coding=utf-8
#1.查看普通txt文档
file=open('D:\\test5.txt','r')
# print(file)
for i in file:
	print(i)
file.close()
#2.写入内容到文件
#如果存在该文件，删除原有内容，写入新内容(覆盖)
#如果不存在该文件，自动创建
s='access denyed!!'
file=open('D:\\access.txt','w')
file.write(s)
file.close()
print('已经创建好文件')
#3.追加内容到文件
#如果存在该文件，追加新内容
#如果不存在该文件，自动创建
s='192.168.0.1 8:00 [error] ! \n'
file=open('D:\\access-log.txt','a')
file.write(s)
file.write(s)
file.close()