#coding=utf-8
#字典的访问
dic={'name':'8jie','age':18}
print(dic)
print(dic['name'])
print(dic['age'])
#字典修改
dic={'name':'8jie','age':18}
print(dic)
dic['age']=100
print(dic)
dic['name']='simida'
print(dic)
#删除字典
#del
dic1={'name':'heygor','QQ':110}
print(dic1)
del dic1['QQ']
print(dic1)
del dic1
# print(dic1)
#clear
#清空字典(可以访问)
dic1={'name':'gaga','QQ':119}
print(dic1)
dic1.clear()
print(dic1)
#1.keys
dic1={'name':'gaga','QQ':119}
print(dic1.keys())
print(type(dic1.keys()))
for i in dic1.keys():
    print(i)
    print(type(i))
#2.values
dic1={'name':'gaga','QQ':119}
print(dic1.values())
print(type(dic1.values()))
for i in dic1.values():
    print(i)
#3.items
dic1={'name':'gaga','QQ':119}
for i,j in dic1.items():
    print(i,j)