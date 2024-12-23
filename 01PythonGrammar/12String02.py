'''
서식문자로 문자열, 정수, 실수 표현
형식]
    '%s' % '문자열 혹은 변수'
    '%d' : 정수
    '%f' : 실수
    자리수 지정시 %10d, %5.3f 같이 표현한다.
'''

#문자열 사용
str = '내 이름은 %s 입니다.' % '칸'
print("str1=",str)

#리스트 사용
names = ['유비','관우','장비']
for n in names:
    print('이름 : %s % n')

# 정수 사용
money = 100000
str = '마우스 가격은 %d원 입니다.' %money  
print(str)

# 실수 사용
pi = 3.141592
print('원주율은 %f' %pi)
print('원주율은 %5.3f' %pi)


# 변수가 2개 이상일때
str = '이름 : %s. 나이 : %d'%('홍길동', 99)
print(str)

# 변수를 여러개 초기화

phone, age , height = "010-1234-5678", 28, 181.5
# 여러개를 출력할때는 콤마로 구분하고, 괄호로 묶어준다.
str2 = '전화번호:%s, 나이: %d, 키 :%.1f'% (phone, age, height)
print("str2=",str2)