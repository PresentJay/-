from openpyxl import Workbook
import os

def write_excel():
    wb = Workbook()
    ws1 = wb.create_sheet("data")

    os.mkdir('result')
    wb.save('./result/data.xlsx')
    print('생성완료~~~')