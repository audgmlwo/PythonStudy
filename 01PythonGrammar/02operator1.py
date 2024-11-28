#산술연산자

# 3개의 정수형 변수 선언
x = 2
y = 4
z = 8

print("x+y", x+y)
print("x-y", x-y)
print("x*y", x*y)
#나누기 연산. 결과는 실수(float)형으로 반환.
print("x/y", x/y)
#몫을 구히기 위한 나누기 연산. 결과는 정수(int)형으로 변환
print("x//y", x//y)
#거듭제곱. 즉 x의 y승의 결과 반환
print("x**y", x**y)
#pow = 거듭제곱 , 파이썬이 제공하는 기본함수 
print("pow(x,y)", pow(x,y))
#pow (인자가 3개 이면), x의 y승을 먼저 연산 그 결과를 z로 나눈 나머지가 반환됨.
print("pow(x,y,z)", pow(x,y,z))
#x를 y로 나눈 몫과 나머지를 Tuple(튜풀)로 반환함.
print("divmod(x,y)", divmod(x,y))

'''
수학 관련 여러가지 함수를 가지고 이는 math 모듈을 현재 문서에
import 한 후 팩토리얼 함수를 호출
'''


import math
print("math.factorial(5)", math.factorial(5))