

import csv
# l=[]
with open('E:\\a.csv', 'r') as f:
    reader = csv.reader(f)
    for i in reader:
        if i[0]=='月度汇总表 统计日期：2019-10-01 至 2019-10-31' or i[0]=='姓名' or i[0]=='' or i[0]=='报表生成时间：2019-11-05 11:40':
            continue
        else:
            l1=[]
            l1.append(i[0])
            # print(i[0])
            l=[]
            l2=[]
            for a in i:
                if '小时' in a:
                    # print(a[-5:-2],end=" ")
                    b=a.split()
                    l.append(b[-1][:-2])
                    # print(b[-1][:-2])
                    # l.append(a[-4:-2])
                    l2.append(a)
                else:
                    continue
            # print(l)
            # print()
            with open('D:\\999.csv', 'a', newline="") as f:
                file = csv.writer(f, dialect='excel')
                file.writerow(l1)
                #测试用
                file.writerow(l2)
                file.writerow(l)
            # for a in i:
            #     print(a)
                # if a[0]=='':
                #     continue
                # else:
                #     print(a)
            # print()
            # file=open('D:\\test5.txt','a')
            # file.write(i[0]+'\n')
            # file.write(str(l)+'\n')
            # file.close()
            # print(list(i[0]))
            # b=i[0]
            # with open('D:\\999.csv', 'a', newline="") as f:
            #     file = csv.writer(f, dialect='excel')
            #     file.writerow(b)
            #     file.writerow(l)
        # print()
print("finished")