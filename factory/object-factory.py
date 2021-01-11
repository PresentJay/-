from faker import Faker

if __name__ == "__main__":
    f = Faker('ko_KR')
    
    for i in range(10):
        print(f.name())