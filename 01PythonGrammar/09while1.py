'''
반복문 : 파이썬에서의 반복문은 while 문과 for문만 있다.
    형식]
        초기값
        while 조건문:
            수행할문장
            증감식
        else:
            정상 종료되었을때 진입;

단, while 문이 완료되지 않은 상태로 탈출하게되면 else구문으로
진입할 수 없다.
'''
'''
 열번 찍어 안넘어가는 나무는 없다 라는 속담을 while 문으로 구현
'''

treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." %treeHit )
    if treeHit == 10:
        print("나무가 넘어갑니다.")

print()
print("="*30)


#파이썬에서는 문자열도 조건식으로 사용할 수 있다.
str = '파이썬'
#str이 공백이 될때까지 반복. 공백이 아니라면 True
while str:
    # 출력문 끝에 공백을 추가하여 줄바꿈 없이 출력
    print(str, end=' ')
    '''
    인덱스 1부터 마지막까지를 살라이싱한다.
    즉, 문자열에서 첫글자를 제거한 후 다시 대입한다.
    '''
    str = str[1:]

print()
print("="*30)



sum = 0
i = 1
while i<= 10:
    sum += i
    if i<10 :
        print(i, end="+")
    else:
        print(i, end="=")
    i += 1

else:
    #while 문이 종료되면 else 구문이 실행되어 합의 결과를출력
    print(sum)

print()
print("="*30)


#무한루프 조건으로 while문 실행
coffee = 10
while True:
    print("커피한잔팜")
    coffee = coffee -1
    print("남은 커피양 %d개 입니다." % coffee)
    #판매완료 조건이 되었을때 break를 통해 while문 탈출
    if coffee ==0:
        print("커피 다떨어짐. 안팜")
        break

print()
print("="*30)



import random
#새로운 Set을 생성
lotoo = set()
#무한 루프 조건으로 while문 생성
while True:
    #1~45 의 난수를 생성
    rndNum = random.randint(1,45)
    #생성된 난수는 set에 추가(중복은 자동으로 제거됨)
    lotoo.add(rndNum)
    # set의 크기 , 즉 6개의 요소가 모두 채워지면, while문 탈출
    if len(lotoo) == 6:
        break
    #오름 차순으로 출력
print("로또번호 :", sorted(lotoo)) 
