from datetime import datetime


class Employee:
    # 클래스 속성 정의
    raise_amount: float = 1.04

    # 인스턴스 변수할당 코드
    def __init__(self, first: str, last: str, pay: int):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # classmethod로 선언된 함수에는 첫번쨰 인자로 클래스 자체가 넘어온다.
    @classmethod
    def from_string(cls, emp_str: str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, int(pay))

    @classmethod
    def update_raise_amount(cls, raise_amount: float):
        cls.raise_amount = raise_amount

    # staticmethod는 인터프리터가 따로 넘겨주는 인자가 없다.
    # 보통 유틸성 함수를 사용할때 활용한다.
    @staticmethod
    def is_workday(day: datetime) -> bool:
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True


emp1 = Employee('Lee', 'HaSung', 1000)
emp2 = Employee.from_string('Hong-GilDong-1000')

print(emp2.fullname())  # Hong GilDong
print(emp1.fullname())  # Lee HaSung

# 인스턴스 변수는 다른 인스턴스변수에 영향을 주지 않는다.
emp1.apply_raise()
print(emp1.pay)  # 1040
print(emp2.pay)  # 1000

# 클래스 속성은 모든 인스턴스들에 영향을 끼친다.
# 파이썬이 인스턴스나 클래스의 속성을 찾을 땐 먼저 인스턴스의 __dict__를 통해 확인하고 만약 없으면 클래스의 __dict__에서 찾는다.
# 아래의 경우 emp1의 인스턴스 속성에는 ㄱaise_amout가 없으니 Employee 클래스에서 raise_amout를 찾은것임
Employee.update_raise_amount(1.05)
print(emp1.raise_amount)  # 1.05
print(emp2.raise_amount)  # 1.05
