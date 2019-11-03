#coding=utf-8

#输入
#通过input函数来接受键盘传入的内容,括号中可以输入提示信息
name=input()
print(type(name))
print('your name is %s'% name)

#查看数据类型
#type

# age=input("请输入您的芳龄：")
# print('名字是%s的年龄是%d'%(name,age))

#数据类型转换
#str  转换数据为字符串类型
#int  转换数据为数字类型

age=int(input("请输入你的年龄："))
print(type(age))
print('名字是%s的年龄是%d'%(name,age))

