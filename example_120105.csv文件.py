#coding=utf-8
#csv文件的读
import csv
with open('D:\\10-hr.csv','r') as f:
	reader=csv.reader(f)
	for i in reader:
		print(i)
#csv文件的写
with open('D:\\1201.csv','w',newline="") as f:
	file=csv.writer(f,dialect='excel')
	file.writerow([1,2,3,4])
	file.writerow([8,8,8,8])
	file.writerow([1,2,3,4])
	file.writerow([8,8,8,8])
print('ok了')