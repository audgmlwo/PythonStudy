'''
클래스 변수와 정적메서드
    : class를 통해 생성되는 인스턴스에는 멤버변수와 멤버매서드가 포함된다.
      하지만 클래스변수와 정적메서드는 인스턴스 내부에 존재하지 않고 별도의
      공간에 독립적으로 생성된다. 따라서 2개 이상의 인스턴스를 생성하더라도
      딱 하나만 생성되어 모든 인스턴스가 공유하게 된다.
      자바에서 스태틱과 동일한 개념이다.
'''


class MyCalculator:
    #클래스 변수(정적변수) : 클래스 전체에서 공유됨. 딱 하나만 생성됨
    calCount = 0
    #생성자
    def __init__(self, first, second):
        #인스턴스 변수(멤버변수) : 생성된 인스턴스마다 존재함
        self.first = first
        self.second = second

    #인스턴스 메서드 (멤버 메서드)
    def calculate(self, symbol):
        # 클래스명을 통해 정적변수에 접근
        MyCalculator.calCount += 1
        #멤버변수는 self를 통해 접근하여 연산을 수행
        if symbol=='+':
            result = self.first + self.second
        elif symbol=='-':
            result = self.first - self.second
        elif symbol=='*':
            result = self.first * self.second
        elif symbol=='/':
            result = self.first / self.second
        return result
    
    #정적함수 정의. 데코레이터(자바에서 어노테이션)를 사용함. 
    @staticmethod
    def otherNumMulti(refCls,otherNum):

        '''
        해당 함수는 정적함수로 정의되었으므로 인스턴스 외부에 독립적으로
        생성된다. 따라서 특정 인스턴스의 변수에 접근하기 위해 인스턴스
        의 참조값을 매개변수로 받은 후 사용해야한다.
        '''
        result = (refCls.first + refCls.second) * otherNum
        #계산 횟수 증가
        MyCalculator.calCount += 1
        print("결과", result)
        print("연산횟수", MyCalculator.calCount)

    #참조변수 자체를 사용해서 인스턴스의 내용을 출력할떄 사용하는 함수 
    def __str__(self):
        str = f'계산기 클래스 입니다.'\
            f'first={self.first},second={self.second}'
        return str

#인스턴스 생성
cal1 = MyCalculator(5,9)
cal2 = MyCalculator(3,4)

#인스턴스 1을 통한 연산
print('덧셈(call):', cal1.calculate('+'))
print('곱셈(call):', cal1.calculate('*'))

#인스턴스 2를 통한 연산
print('뺄셈(cal2):', cal2.calculate('-'))
print('나눗셈(cal2):', cal2.calculate('/'))


#클래스변수는 딱 하나만 생성되므로 전체 계산횟수 4가 출력됨
print('계산횟수',MyCalculator.calCount)

'''
정적함수는 참조변수가 아니라 클래스명으로 직접 호출한다.
즉, 함수호출을 위해 인스턴스를 생성할 필요가 없다.
'''

MyCalculator.otherNumMulti(cal1, 10)
MyCalculator.otherNumMulti(cal2, 10)

#인스턴스메서드는 클래스명으로 호출 불가
#MyCalculator.calculate('\')