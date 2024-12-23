'''
문자에서 사용되는 연산자
'''

srt = """ 아래와 같이
여러줄에 걸쳐 문자열을 작성하고 싶으면
이와같이 더블쿼테이션을 3개 작성한다.
"""

print(str)

#문자열 변수 생성 및 초기화
head = "나는 헤더"
bottom = "나는 바텀"
#문자열의 덧셈은 '연결'의 결과를 반환
print(head+bottom)
#곱셈의 결과는 '반복' 출력됨
print(head*3)

#문자열 슬라이싱
'''파이썬에서 문자열은 인덱스를 통해 접근할 수 있다.
인덱스는 0부터 시작하고, 콜론으로 범위를 지정할 수 있다.
범위 사용시 0:10으로 입력했다면 0~9까지를 의미한다.'''

engStr = "Hello Python Good"
print(engStr[0]) # 0번 인덱스 : H
print(engStr[:3]) # 시작인덱스가 없으면 처음부터 시작. 0~2 까지
print(engStr[1:3]) # 1~2까지만 슬라이싱
print(engStr[1:]) # 1부터 끝까지 슬라이싱(종료 인덱스가 없으므로)

#파이썬에서는 한글도 영문과 동일한 슬라이싱이 가능하다.
korSrt = "안녕하세요? 파이썬입니다."
print(korSrt[0])
print(korSrt[:2])
print(korSrt[0:6])

#정수와 문자는 아래와 같이 연결할 수 없다.
#print(engStr + 100)