#coding=utf-8
#1.多态的实现:加法
# a=20
# b=30
# print(a+b)
# a="20"
# b="30"
# print(a+b)
#2.实例
class animal:
    def jiao(self):
        print('ao~~~~~~~')
class dog(animal):
    def jiao(self):
        print('wang！！！')
class cat(animal):
    def jiao(self):
        print('miao!!!!')
def test(s):
    s.jiao()

a=animal()
a.jiao()
b=dog()
c=cat()
test(b)
test(c)
