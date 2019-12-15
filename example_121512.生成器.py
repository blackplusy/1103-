#coding=utf-8
# arr=(x for x in range(1,5))
# print(arr)
# for i in  arr:
#     print(i)
# print('next 1 is ----')
# print(next(arr))
#
# print('next 1 is ----')
# print(next(arr))
#
# print('next 1 is ----')
# print(next(arr))
#

# print('next 1 is ----')
# print(next(arr))
#

#例子2
def test():
    n=1
    print('first')
    yield n
    n+=1
    print('second')
    yield  n
    n+=1
    print('second')
    yield  n
a=test()
print('next 1')
print(next(a))

print('next 1')
print(next(a))



