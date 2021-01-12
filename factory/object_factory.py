from faker import Faker
import factory.control_excel as xl

class Ipman:
    def __init__(self, name, address, ip):
        self.name = name
        self.address = address
        self.ip = ip

    def show_data(self):
        print('name :', self.name)
        print('address :', self.address)
        print('ip :', self.ip)


def serialization(data):
    IPmans = []
    
    for i in range(len(data)):
        ipman = Ipman(data[i]['name'], data[i]['address'], data[i]['ip'])
        IPmans.append(ipman)
    
    return IPmans


def show_whole(Ipmans):
    for i in Ipmans:
        i.show_data()

        
def faker_generator(cnt = 0):
    f = Faker('ko_KR')
    
    if cnt == 0:
        input()
        # 가상환경 쓸 경우, 버퍼에 가상환경 주소가 남아 있는 것을 해결하기 위해
        cnt = input('몇개 생성할래? > ')
    
    IPmans = []

    for i in range(int(cnt)):
        IPmans.append(Ipman(f.name(), f.address(), f.ipv4_private()))
        
    return IPmans
