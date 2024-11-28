'''
퀴즈] 국,영,수 점수를 입력받아 평균값을 구하고 이를 통해 학점을 출력하는 
    프로그램을 작성하시오. 
    90점 이상은 A학점 
    80점 이상은 B학점
    70점 이상은 C학점
    60점 이상은 D학점    
    60점 미만은 F학점으로 판단하여 출력합니다. 
'''

n1 = int(input('국:'))
n2 = int(input('영:'))
n3 = int(input('수:'))

sum = (n1+n2+n3)/3

if 90 <= sum <= 100 :
    print("A학점",format(sum,".2f"))
elif 80 <= sum < 90:
    print("B학점",format(sum,".2f"))
elif 70 <= sum < 80:
    print("C학점",format(sum,".2f"))
elif 60 <= sum < 70:
    print("D학점",format(sum,".2f"))    
else :
    print("F학점",format(sum,".2f"))


'''
퀴즈2] 아이디를 먼저 입력받은 후 user_info 리스트에 등록되었다면 패스워드를 
입력받아 일치하는지 확인하는 프로그램을 작성하시오. 여기서 패스워드는 1234로 가정합니다. 
'''

user_id_list= ["1번","2번","3번","4번","5번","6번"]
user_id = input("ID를 입력하세요:")

if user_id in user_id_list :
        print("아이디가 확인되었습니다.")
        pwd = int(input('비밀번호를 입력하세요:'))
        if pwd == 1234:
             print("인증에 성공하셨습니다.")
        else:
             print("비밀번호가 틀립니다. 인증에 실패하였습니다.")     
else :
    print("아이디가 없습니다.")  
