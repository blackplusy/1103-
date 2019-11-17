#coding=utf-8
dic={'admin':'123','sal':'456'}
while 1:
    #输入用户名
    username=input('请输入您的用户名： ')
    #检查是否输入或者是否存在于字典的键中
    if len(username)==0 or username not in dic.keys():
        print('您的输入有误，请重新输入')
    else:
        print('用户名存在')
        #密码验证循环
        while 1:
            #输入密码
            passwd=input('请输入您的密码：')
            #验证密码是否是和用户名对应密码
            if dic[username]==passwd:
                print('登录成功')
                #跳出密码验证循环
                break
            else:
                print('您的密码有误，重新输入密码')
        #跳出用户名验证循环
        break