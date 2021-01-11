from faker import Faker
import control_excel as xl

class Ipman:
    def __init__(self, name, address, ip):
        self.name = name
        self.address = address
        self.ip = ip

    def show_data(self):
        print('name :', self.name)
        print('address :', self.address)
        print('ip :', self.ip)
        
# 끝남
def faker_test():
    f = Faker('ko_KR')
    
    # 가상환경 쓸 경우, 버퍼에 가상환경 주소가 남아 있는 것을 해결하기 위해
    input()
    
    number = input('몇개 생성할래? > ')
    IPmans = []

    for i in range(int(number)):
        IPmans.append(Ipman(f.name(), f.address(), f.ipv4_private()))
        
    for j in IPmans:
        j.show_data()
        
    print(len(IPmans))


if __name__ == "__main__":
    # faker_test()
    xl.write_excel()