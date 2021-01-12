from factory.object_factory import *

if __name__ == "__main__":
    input()
    
    flag2 = input('생성할래:1, 정보 확인할래:2\n>> ')
    
    if int(flag2) == 1:
        IPmans = faker_generator()
        flag = input('불러올래:1, 새로만들래:2\n>> ')
        
        if int(flag) == 2:    
            wb = xl.create_excel()
            xl.set_Ipmans(wb['data'], IPmans)
        elif int(flag) == 1:
            wb = xl.load_workbook('./result/data.xlsx')
            count = xl.get_Count_Ipmans(wb['data'])
            print('엑셀에 원래 있던 Ipman 수 :', count)
            xl.set_Ipmans(wb['data'], IPmans, start=count+2)        
        xl.save_excel(wb)
        
    elif int(flag2) == 2:
        wb = xl.load_workbook('./result/data.xlsx')
        count = xl.get_Count_Ipmans(wb['data'])
        IPmans = serialization_from_excel(xl.get_data(wb['data'], count))
        show_whole(IPmans)