from openpyxl import *
import os

def init_Ipmans(sheet):    
    sheet['A1'].value = 'Name'
    sheet['B1'].value = 'Address'
    sheet['C1'].value = 'IP'
    return sheet

def set_Ipmans(sheet, IPmans, start=2):
    for i in range(start, start+len(IPmans)):
        sheet['A' + str(i)] = IPmans[i-start].name 
        sheet['B' + str(i)] = IPmans[i-start].address
        sheet['C' + str(i)] = IPmans[i-start].ip
    return sheet

def get_data(sheet, cnt):
    data = []
    for i in range(2, cnt+2):
        ipman = {
            'name' : sheet['A' + str(i)].value,
            'address' : sheet['B' + str(i)].value,
            'ip' : sheet['C' + str(i)].value
        }
        data.append(ipman)
    return data

def get_Count_Ipmans(sheet):
    count = 1
    while (sheet['A' + str(count)].value is not None) :
        count+=1
    return count-2

def create_excel():
    wb = Workbook()
    sheet = wb.active
    sheet.title = 'data'
    sheet = init_Ipmans(sheet)
    return wb

def save_excel(wb):
    if os.path.isdir('result') is False:
        os.mkdir('result')
    wb.save('./result/data.xlsx')