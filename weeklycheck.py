#encoding=utf-8
import xlrd
from collections import defaultdict
#from time import sleep
#import re
wr=xlrd.open_workbook('/Users/ricelee/Desktop/人员填报明细报表.xlsx')
sheet=wr.sheet_by_name('填报明细')

dic=defaultdict(list)
name=''
week=0
status=''
days=0



def checkstatus():
    statusOK = 0
    statusFL = 0
    print('状态检查'.center(40,'-'))
    for name in dic:

        for i in dic[name]:
            if i[1] != '已填':
                print('{}：{}周没提交周报'.format(name,i[0]))
                statusFL += 1
            elif i[2]==False:
                print('{}：{}周未分配精力'.format(name, i[0]))
                statusFL += 1
            else:
                statusOK += 1
    print('共检查{}条数据，正常{}条，异常{}条'.format(statusOK+statusFL,statusOK,statusFL).center(40,'-'))

def countdays(count):
    print('工时检查'.center(40,'-'))
    countOK = 0
    countFL = 0
    for name in dic:
        total_days = 0

        for i in dic[name]:
            total_days += i[2]

        if total_days !=float(count):
            print('{}：工时：{} 未满{}天'.format(name,str(total_days).center(5,' '),count))
            countFL += 1
        else:
            countOK += 1
    print('共{}人，工时正常{}人，异常{}人'.format(countOK+countFL,countOK,countFL).center(40,'-'))

if __name__ == '__main__':

    weeklist = list(input("Week(s):(请顺序填写周数，例如10,11,12,13) \n").split(','))
    count = len(weeklist)*5

    for a in range(1, sheet.nrows):
        if len(sheet.row_values(a)[3])<3:
            name = sheet.row_values(a)[3]+'\t '
        else:
            name = sheet.row_values(a)[3]
        week = sheet.row_values(a)[1]
        status = sheet.row_values(a)[11]
        days = sheet.row_values(a)[16]
        if days=='':
            days=0
        if week in weeklist:
            dic[name].append((week, status, days))

    checkstatus()#检查是否已经提交

    countdays(count)#检查总工时是否够

    print('检查结束'.center(40,'-'))