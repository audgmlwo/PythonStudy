'''
문제 3: 소수 판별하기
입력받은 정수가 소수(Prime Number)인지 확인하는 함수를 작성하세요.
(소수: 1과 자기 자신만으로 나누어지는 1보다 큰 정수)
함수 이름: is_prime
입력: 정수 n (예: 7)
출력: True 또는 False
'''

def is_prime():

    num = int(input('숫자를 입력하세요: '))

    if num > 1:  
        for i in range(2, num): 
            if num % i == 0:
                print(f"{num}은(는) 소수가 아닙니다.")
                break
            else:
                print(f"{num}은(는) 소수입니다.")
    else:
     print(f"{num}은(는) 소수가 아닙니다.")  

is_prime()

def is_prime1(num):
    isPrime = True


    for i in range(2,num):
        if num % i == 0:
            isPrime = False
            break


    return isPrime


iNum = int(input("정수를 입력하세요:"))
print(f"결과 : {is_prime1(iNum)}")