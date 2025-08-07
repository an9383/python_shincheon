


class Customer:
    def __init__(self,name,address,phone):      #스키마를 구성할때 사용함.
        self.name = name
        self.address = address
        self.phone = phone
    def change_phone(self,new):
        self.phone = new
    def __call__(self,position):                #__가 붙으면 클래스 내장함수라는 의미임. call 함수 호출시에는 변수이름('')형식으로 호출해야 함.
        print(f'{self.name}은 {position}')       # __call__텐서플로에서 많이 씀.
    def __repr__(self):                         #repr은 print(변수)형식으로 호출해야 함. 화면에 보기 좋게 표시할때 처리함.
        return (f"{self.name}은 {self.address}에 살고"
                f" 전화번호는 {self.phone}입니다.")

if __name__ =="__main__":
    john = Customer('john','seoul','010-1111-2222')     #john변수자체가 self임. self는 데이터를 집어넣는 변수를 의미함.
    peter = Customer('peter','pusan','010-2222-3333')
    peter.change_phone('010-3333-4444')
    # print(john.__dict__)
    # print(peter.__dict__)
    # john('cook')
    # peter('server')

    print(john)                                 # repr함수를 호출.
