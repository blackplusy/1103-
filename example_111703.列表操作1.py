#coding=utf-8
#列表的访问
#1.直接输出
l1=['李白','李元芳','钟馗']
print(l1)
#2.遍历访问
for i in l1:
    print(i)
#3.成员访问
if '张小敬' in l1:
    print('长安十二时辰')
else:
    print('不在里面')
#列表的索引和切片
l1=['张飞','马超','云云','黄忠','二爷']
print(l1[0])
print('中国独有的佛'+l1[-1])
# print(l1[30])
print(l1[2:])
print(l1[2:3])
#列表的拼接
l=[1,2,3,4]
m=['a','b']
print(l+m)
#列表的修改
l=[1,2,3]
print(l)
l[2]='柳岩'
print(l)
l[-2]='大鹏'
print(l)
#列表的删除
l=[1,2,3]
print(l)
del l[2]
print(l)
del l
print(l)