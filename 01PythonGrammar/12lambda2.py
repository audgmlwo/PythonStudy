# 1.map()
'''
map 함수는 주어진 함수와 컬렉션을 인자로 받아, 컬렉션의
각 요소에 함수를 적용한 결과를 반환한다.
for문과 같은 반복문을 사용하지 않아도 지정한 함수로 인자를 
자동으로 전달하여 그 결과를 List 형태로 반환한다.
'''
# 함수 정의 : 매개변수에 2를 곱한 결과를 반환
def multiply_by_two(n):
    return n*2
# 리스트 정의
numbers = [1,2,3,4,5]
#map (함수,리스트) 와 같이 호출
result = map(multiply_by_two, numbers)
#결과 1 : map Object로 출력됨
print('결과1-1', result)
#결과 2 : Object를 List로 변환 후 출력
print('결과1-2', list(result))
'''
각 요소에 2를 곱한 결과를 반환. 리스트의 크기는 기존과 동일하다.
결과 : [2,4,6,8,10]
'''

# 2.fiter 함수
'''
filter 함수는 주어진 요소 중 조건에 맞는 것만 필터링하여 반환한다.
즉, 지정된 함수(혹은 람다식)에서 True가 되는것만 반환하여
새로운 List 함수(or 람다식) 에서 True가 되는것만 반환하여 결과를 생성한다.
'''
#인수가 짝수인 경우 True를 반환하는 함수
def is_even(x):
    return x % 2 ==0
numbers = [1,2,3,4,5]
result = filter(is_even, numbers)
print('결과2',list(result))

'''
짝수만 리스트에 남고, 홀수는 모두 제거된 상태로 반환된다.
결과 : [2,4]
'''
# 3.reduce 함수
from functools import reduce

'''
반복 가능한 객체의 각 요소를 지정된 함수로 처리한 뒤 이전 결과와
누적해서 반환하는 함수이다. 죽, 하나의 값을 반환한다.
파이썬 3.x 부터는 내장함수가 아니므로 별도의 모듈을 임포트해야한다.
'''

#두 개의 인자를 합산한 결과를 반환하는 함수
def add(x,y):
    return x+y
numbers = [1,2,3,4,5]
result = reduce(add, numbers)
print('결과3', result)

'''
리듀스 함수는 리스트의 처음 2개의 요소를 함수로 전달하여 결과를 만들고,
그 결과를 다시 다음 요소와 결함하는 방식으로 전체 리스트를 처리한다.

add(1,2) = 3
add(3,2) = 6
add(6,4) = 10
add(10,5) = 15(최종결과)

reduce 에서 사용하는 함수는 2개의 인자만 받을 수 있다.
만약 매개변수를 3개로 정의하면 에러가 발생한다.


'''