#coding=utf-8
#菱形
for i in range(-3,4):
    i=abs(i)
    print(i*' '+(7-2*i)*'*')

#圣杯
e=3
# for i in range(-e,n-e):
for i in range(-3,4):
    i=abs(i)
    print(' '*(e-i)+'*'*(2*i+1))
#99乘法表
for i in  range(1,10):
    for j in range(1,i+1):
        print(str(i)+"*"+str(j)+'='+str(i*j),end=" ")
    print()
