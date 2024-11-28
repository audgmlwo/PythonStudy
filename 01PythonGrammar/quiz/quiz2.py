'''
문제 2: 팰린드롬 문자열 확인
주어진 문자열이 팰린드롬인지 확인하는 함수를 작성하세요.
(팰린드롬: 앞뒤가 똑같은 문자열, 예: "level", "radar")
함수 이름: is_palindrome
입력: 문자열 s (예: "radar")
출력: True 또는 False
'''

def is_palindrome():
    strs = input('문자 입력:').split(' ')

    for str in strs :
        if str == str[::-1]:
    
            print("True")
        else:

            print("False")

is_palindrome()

def is_palindrome1(str):
    isPalin = False
    print(f"원본:{str}")
    reversed_str = ''.join(reversed(str))
    print(f"사본:{reversed_str}")
    if str == reversed_str:
        isPalin = True    
    return isPalin


def is_palindrome2(str):
    isPalin = True


    start = 0
    end = len(str)-1
    while start < end:
        if str[start] != str[end]:            
            isPalin = False
            break
        start += 1
        end -= 1    
    return isPalin


istr = input("문자열을 입력하세요:")
print(f"함수1 : {is_palindrome1(istr)}")
print(f"함수2 : {is_palindrome2(istr)}")
