print(f"{'if문 첫번째 형식':-^30}")
a, b, c, str = 10, 20, 30, '파이썬'

if a !=b:
    print("a는b와다르다.")
if a<= c:
    print("a는c보다 작거나 같다.")
if str:
    print("문자열은 True를 반환 한다.")
#if a> str : # 에러발생
#      print("문자열과 정수는 비교 대상이 될 수 없다.")

print(f"{'if문 두번째 형식':-^30}")
if not a>b:
    print("a는b보다 크지 않다.")
else :
    print('a는 b보다 큽니다.')    

if a == b and b != c:
    print("a는b와 같고, b는 c와 다르다.")
else :
    print('위에 조건중에 False가 있다.')   

if a > b or b < c:
    print("a는b보다 크거나 b는 c보다 작다")    
else :
   print('위에 조건중에 False가 있다.')      

'''
2개 이상의 조건식이 있는 경우 elif를 사용한다.
자바와 같이 else if 가 아니므로 사용에 주의해야한다.
'''

print(f"{'if문 세번째 형식':-^30}")   
age = 33
print(age, "살은", end ="")
if age >= 35:
    print("중년")
elif age >= 30:
    print("중년의 시작")
else:
    print("청년입니다.")





