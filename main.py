from factory.object_factory import *

if __name__ == "__main__":
    
    IPmans = faker_generator()
    
    wb = xl.create_excel()
    xl.init_Ipmans(wb['data'])
    xl.set_Ipmans(wb['data'], IPmans)
    
    xl.save_excel(wb)