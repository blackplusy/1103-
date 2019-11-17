#coding=utf-8
#创建元组
a=(1)
print(a)
print(type(a))
a=(1,)
print(a)
print(type(a))
#元组的访问
tup=(1,2,3,4)
print(tup)
for i in tup:
    print(i)
if 2 in tup:
    print('yes!!!')
#元组的索引和切片
tup=(1,2,3,4,5)
print(tup[0])
print(tup[-2])
print(tup[2:4])
print(tup[3:])
print(tup[:-3])
#元组的删除
tup=(1,2,3,4)
del tup
# print(tup)
#元组的补充
t=(1,3,5,2,4,6,2,2,2,2)
print(len(t))
print(max(t))
print(min(t))
print(t.index(2))
print(t.count(2))

