'''
문제 1: 숫자의 합 구하기
사용자로부터 양의 정수를 입력받아 각 자릿수의 합을 계산하는 함수를 작성하세요.
함수 이름: sum_of_digits
입력: 정수 n (예: 1234)
'''

def sum_of_digits():
    nums = map(int, input('정수 입력: ').split(' '))
    sum = 0

    for num in nums :
        sum += num
    print('입력한 정수의 합',sum)

sum_of_digits()

def sum_of_digits1():
    nums =  input('정수 입력: ')
    sum = 0

    for num in nums :
        sum += int(num)
    print('입력한 정수의 합',{sum})

sum_of_digits1()