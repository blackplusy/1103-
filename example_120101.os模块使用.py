#coding=utf-8
import os
#1.运行系统中的命令
os.system('dir')    
#2.删除系统中的文件   
# os.remove('d:\\tel.txt')   
#3.显示当前目录的绝对路径
print(os.getcwd()) 
#4.显示指定目录下所有文件(列表形式存储)
print(os.listdir('D:\\'))      
#5.返回一个路径的目录和文件名(元组形式存储)
print(os.path.split('D:\\1201\\a.py'))
#6.判断是否是文件
print(os.path.isfile('D:\\1201\\a.py'))
#7.判断是否是目录
#os.path.isdir
#8.判断路径是否存在
#os.path.exists