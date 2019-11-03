#coding=utf-8

num=int(input('请输入一个3位数'))
bai=num//100
# print(bai)
shi=num//10%10
# print(shi)
ge=num%10

if bai**3+shi**3+ge**3==num:
    print('水仙花数字')
else:
    print('不是水仙花数子')



