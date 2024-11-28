print(f"{'중첩된 if문':-^30}")   

num1 = int(input('숫자 하나를 입력하세요:'))

# 중첩된 구조의 if문 작성

if num1%2==0:
    if num1%3==0:
        print("2와 3으로 나누어짐")
    else:
        print("2는 가능, 3은불가")
else:
    if num1%3==0:
        print("2는 불가, 3은가능")
    else:
        print("2와 3 모두 불가")

print(f"{'삼항연산자':-^30}")  

'''
삼항연산자
        형식] 변수 = True조건의 문장 if 조건식 else False조건의 문장
            할당할 필요가 없다면 좌측항은 생략할 수 있다.
'''

#삼항연산자
number = 99
# 조건에 맞는 값을 좌측항으로 할당한다.
result = "100보다 크다" if number > 100 else "100보다 작다"
print(result)

#할당없이 즉시 조건에 맞는 print()문을 실행한다.
print("3의배수") if number%3==0 else print("3의배수아님")

print(f"{'if~in문':-^30}") 
cList = ["세부","보라카이","파타야","나트랑","코타키나발루","푸켓"]
journey =input("여행할 나라를 입력하세요:")
# 리스트에 입력한 나라가 포함되었다면 True를 반환
if journey in cList :
    print("{}는(은) 여행지 목록에 있습니다.".format(journey))    
else :
    print("{}는(은) 여행지 목록에 없습니다.".format(journey))  

