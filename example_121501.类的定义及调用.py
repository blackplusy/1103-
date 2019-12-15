#coding=utf-8

class student:
	def study(self):
		print('im study!!!')
	def play(self):
		print('im playing ball')

boy=student()
#产生一个student的对象，通过boy实例对象来访问属性和方法
boy.age=20
#给对象添加属性，注意:后面如果再次出现，表示对属性进行修改
boy.faver='baseball'

boy.study()
#通过实例对象去访问类的方法

print(boy.age)
print(boy.faver)
