#coding=utf-8
#功能：计算一个函数的运行时间
import time
# def jisuan(func):
#     def zsq():
#         starttime=time.time()
#         func()
#         endtime=time.time()
#         sec=endtime-starttime
#         print('消耗的时间是:%d'%sec)
#     return zsq
#
# @jisuan
# def func():
#     print('hello')
#     time.sleep(1)
#     print('world')
# f=func
# f()

#2.带有参数的装饰器

def dec(func):
    def jisuan(a,b):
        starttime = time.time()
        func(a,b)
        endtime=time.time()
        sec=endtime-starttime
        print('消耗的时间是:%d'%sec)
    return jisuan

@dec
def func(a,b):
    print('a+b=?')
    time.sleep(2)
    print('its',a+b)

f=func
f(4,5)



# if __name__=='__main__':
#     func()
    #如果文件作为普通的python文件的话，if.....下面的语句正常执行
    #如果文件作为模块导入到其他文件中的话，if.....下面的语句不执行