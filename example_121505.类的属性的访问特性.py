#coding=utf-8

class test:
    a=100                    #类的属性
    def __init__(self,b):
        self.b=b             #实例的属性

t=test(998)    #实例化对象
#1.通过实例化对象来访问类的属性
print('t.a=%d'% t.a)
#2.通过类名访问类的属性
print('test.a=%d'% test.a)
#3.通过实例化对象访问实例属性
print('t.b=%d'% t.b)
#4.通过类名访问实例属性
print('test.b='% test.b)
#无法通过类名.属性来访问实例属性




