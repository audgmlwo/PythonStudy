'''
문제 4: 문자열 단어 개수 세기
주어진 문자열에서 공백으로 구분된 단어의 개수를 세는 함수를 작성하세요.

함수 이름: count_words
입력: 문자열 s (예: "hello world python")
출력: 정수 (단어 개수)
'''

def count_words():
    dir=0
    strs = input('문자 입력:').split(' ')
    
    for str in strs : 
        dir += len(str) 

    print(dir)
     
count_words()


