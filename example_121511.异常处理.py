#coding=utf-8
#1.try...except

# try:
#     p
# except NameError as e:
#     print('catch error!!!')
#     print(e)

#2.try...finally
# try:
#     f=open('test','r')
#     print(f.read())
# finally:
#     print('不要慌！！！')

#3.try...except...finally
try:
    p
except NameError as e:
    print("catch error!!!")
finally:
    print("找不到吧？")
