# coding:utf-8

"""
 @Author : Cong
 @Time : 2021/7/13 16:55
"""
import sys
import xlrd

def __loadWorkList(filepPath):
    wb = xlrd.open_workbook(filename=filepPath)
    sheet = wb.sheet_by_index(0)
    res = []
    for i in range(sheet.nrows)[2:-1]:
        # print(sheet.row_values(i))
        res.append(sheet.row_values(i))

    return res

def do_info():
    _help = '指令格式：python %s info FILEPATH' % programName
    if len(sys.argv) > 2:
        filePath = sys.argv[2]
        print(filePath)
        res = __loadWorkList(filePath)

        month = {r[3][:7] for r in res}
        print(month)

    else:
        print(_help)

programName = sys.argv[0]

if len(sys.argv) > 1:
    command = sys.argv[1]
    # print('command = %s' % command)
    if command == 'info':
        do_info()
else:
    print('命令使用：')
    print('\tpython %s COMMAND [PARAMS]' % programName)
    print('\tpython %s info' % programName)
