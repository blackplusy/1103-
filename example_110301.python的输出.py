#coding=utf-8
#coding设置文件的字符集
#常见的字符集  utf-8   通用    GBK2312  中文

#1.直接输出
#输出数字类型数据
#输出字符串类型数据
#输出列表类型数据
#输出使用print函数进行输出，括号中放入需要输出的内容
print(123)
print("黑哥真帅！！！")
print([1,2,3])

#2.变量输出
#常量： 值不会改变的量
#变量:  值会变化的量
a=100
#a是变量的名字，100是变量的值
print(a)
a=30
print(a)
#变量可以进行相应操作
a=100
b=20
print(a+b)
a="100"
b="20"
print(a+b)

#3.函数输出
#abs()    绝对值
#len()    计算元素个数
#输出-30的绝对值
print(abs(-30))
#输出字符串hello world 元素个数
print(len("hello world!!!"))

#4.格式化输出
#  %s  格式化输出字符串信息
#  %d  格式化输出数字信息
print('小红是NO.1')
print('小明是NO.2')
print('小军是NO.3')
name='小明'
no=1
print('%s是NO.%d'%(name,no))
#注意:如果是一个参数，不需要加括号，如果是多个参数，需要加括号

age=18
print('您的年龄是%d'%age)


















