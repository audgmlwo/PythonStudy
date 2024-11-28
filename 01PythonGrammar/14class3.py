'''
멤버변수의 외부 접근을 차단하고, 클래스 내부에서만 접근하도록 처리하는
*정보은닉을 위해 (자바 private) 파이썬에서는 __ (언더바2개)를 사용한다.
'''

class Computer:
    #생성자
    def __init__(self, name, passwd):
        
        self.name = name # public(외부접근허용)
        self.__passwd = passwd #private(외부접근차단)
    # 멤버 메서드    
    def hitKeyboard(self):
        return f'{self.name}로 키보드 작업을 합니다.'
    def clickMouse(self):
        print(f'{self.name}에서 마우스로 클릭합니다.')
    #정보은닉 처리된 멤버변수의 접근을 위한 getter/setter메서드 정의    
    def getPasswd(self):
        return self.__passwd
    def setPasswd(self, passwd):
        self.__passwd = passwd

#인스턴스 생성
myCom = Computer('엘지',"qwer1234")

#멤버메서드 호출
print(myCom.hitKeyboard())
myCom.clickMouse()

#외부접근이 허용되므로 정상적으로 출력됨
print("컴퓨터이름", myCom.name)

#private 이므로 접근할 수 없어서 에러발생 => getter를 통해 접근 후 출력해야 한다.
#print("패스워드", myCom.__passwd)
'''
Traceback (most recent call last):
  File "c:\workspace\PythonStudy\01PythonGrammar\14class3.py", line 22, 
in <module>
    print("패스워드", myCom.__passwd)
                      ^^^^^^^^^^^^^^
AttributeError: 'Computer' object has no attribute '__passwd'

'''

print("패스워드", myCom.getPasswd())

#변경을 위해 setter 호출
myCom.setPasswd('abcd9876')
print('패스워드 변경후1', myCom.getPasswd())

'''
맹글링 규칙에 의해 정보은닉 처리된 멤버변수는 
이름이 변경되므로 아래와 같이 작성했을떄 값을 변경할 수 없다.
또한 에러도 발생하지 않는다.
'''
myCom.__passwd = 'xxxxXXXX'
print('패스워드 변경후2', myCom.getPasswd())

#권장되지 않음
print("맹글링규칙", myCom._Computer__passwd)