'''
예외처리
    : 에러를 핸들링하기 위해 사용된다.
      파이썬에서는 try ~ except를 사용한다.
      그리고 else 절을 사용할 수 있다.
'''

def calc(val):
    sum = None
    #예외발생이 예상되는 지점을 try로 묶어준다.
    try:
        sum = val[0] + val[1]+ val[2]
        if val[0]==100:
            #정의되지 않은 변수를 출력하므로 에러 
            print(no_var)
        elif val[0]==55:
            #0을 0으로 나누면 인피니티 => 에러 
            result = val[0] / 0
            print("rusult", result)
    #예외명을 명시하여 특정 예외만 처리
    except IndexError:
        print('리스트의 인덱스에 에러가 있습니다.')
    #예외발생시 에러메시지를 변수로 받아 출력    
    except NameError as err:
        print('선언되지 않은 변수를 사용하였습니다.', str(err))
    #예외명을 명시하지 않으면 모든 예외를 처리할 수 있는 블럭이 됨
    except:
        print('예외가 발생함')
    #예외가 발생하지 않으면 실행되는 블럭    
    else:
        print('에러없음')
    #예외발생과 상관없이 무조건 실행되는 블럭   
    finally:
        print('sum',sum)

#정상실행
print('실행1')
calc([1,2,3])
#val[2] 없으므로 => IndexError 발생됨.
print('실행2')
calc([10,20])
#선언되지 않은 변수를 출력하므로 => NameError 발생됨.
print('실행3')
calc([100,101,102,103])
#ZeroDivisionError가 발생되고, 특정 예외로 코드를 작성안했기때문에 => 그냥 예외발생으로 처리됨
print('실행4')
calc([55,56,57])
#중첩된 예외처리

'''
실행1: 최초 실행시에는 파일이 없는 상태이므로 IOError 발생됨.
실행2: 애국가.txt 파일을 생성후 실행하면 파일의 끝까지 내용을 읽은후
       예외가 발생됨
'''
print('실행5')
try:
    fp = open("./saveFiles/애국가.txt", mode = 'rt', encoding='utf-8')
    try:
        while True:
            lines = fp.readlines()
            if not lines:break
            print(lines)
    finally:
        print("예외]가 더 이상 읽을 내용이 없습니다.")
        fp.close
except IOError:
    print("예외]파일이 없습니다.")