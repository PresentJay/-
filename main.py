from factory.object_factory import *

if __name__ == "__main__":    
    # IPmans = faker_generator()
    
    input()
    
    flag = input('불러올래:1, 새로만들래:2\n')
    
    if int(flag) == 2:    
        wb = xl.create_excel()
        xl.set_Ipmans(wb['data'], IPmans)
    elif int(flag) == 1:
        wb = xl.load_workbook('./result/data.xlsx')
        print(xl.get_Count_Ipmans(wb['data']))
    
    # xl.save_excel(wb)