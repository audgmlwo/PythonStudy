'''
시나리오] 원의 넓이와 둘레를 계산할 수 있는 클래스를 작성한 후 
주어진 코드가 실행될 수 있도록 구현하시오.
circle1 = Circle(5)
print("원의넓이:", circle1.calArea())
print("원의둘레:", circle1.calRound())
'''

#수학 관련 기능을 제공하는 math 모듈을 임포트
import math

#클래스 정의
class Circle:
    #생성자 
    def __init__(self, radius):
        #맴버변수 : 반지름 표현
        self.radius = radius
    #넓이
    def calArea(self):
        return math.pi * (self.radius **2)
    #둘레
    def calRound(self):
        return 2 * math.pi * self.radius
    def __str__(self) :
        return f'원의 발지름은 {self.radius} 입니다.'

#인스턴스 생성
circle1 = Circle(5)
#인스턴스의 정보를 __str__()을 통해 출력
print(circle1)
print("원의 넓이 :", circle1.calArea())
print("원의 둘레 :", circle1.calRound())