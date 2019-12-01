#coding=utf-8
#栈的方式访问列表
#list.append() 列表最后追加内容
#list.pop()    弹出最后一个元素
l=[1,2,3,4]
print(l)
l.append(5)
print(l)
l.append(6)
print(l)
l.pop()
print(l)
l.pop()
print(l)
l.pop()
print(l)
#获取列表的索引
#index()
l=['a','b','c','d','e']
print(l.index('c'))
#枚举
l=['a','b','c','d','e']
for index,value in enumerate(l):
    print('索引是:'+str(index)+'值是:'+str(value))
#列表的排序
l=[1,2,3,4]
print(l)
l.reverse()
print(l)
l=[1,3,2,4]
print(l)
l.reverse()
print(l)

l=[1,3,5,2,4,6]
l.sort()
print(l)
l.reverse()
print(l)

l=[1,3,5,2,4,6]
print(l)
l.sort(reverse=True)
print(l)

#补充
#insert()
l=['a','b','c']
l.insert(1,'d')
print(l)
l.insert(-1,'aaa')
print(l)
#extend()
l=['a','b','c']
l.extend('a')
print(l)
l.extend([1,2,3])
print(l)

#列表推导式
#给定列表
a=[1,2,3,4]
print([5*x for x in a])
#没有给定列表可以使用range方法
print([3*x for x in range(10)])
#加入if条件进行推导
a=[1,2,3,4]
print([x for x in a if x%2==0])
#多个for语句进行列表推导
print([[x,y] for x in range(2) for y in range(2)])





