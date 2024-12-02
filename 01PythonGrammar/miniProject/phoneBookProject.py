pList = []

def menu():
    print('1.입력 2.출력 3. 검색 4.수정 5.삭제')
    print('6.종료')
    return input('번호선택:')


def insert(name, phone, addr):
   
    global pList
    pId = len(pList) +1
    pList.append([pId, name, phone, addr])
    print("입력 완료.")
    return pList

def show(pList):
    if pList:
        print(" 번호    이름       전화번호              주소"),
        print(f"{'':-^54}")  
        for data in pList:
            print(f"  {data[0]}     {data[1]}   {data[2]}    {data[3]}")
            print(f"{'':-^54}")
    else:
        print("데이터가 없습니다.")

def search(word):   
     word = (input("검색할 이름 : "))
     print(f"{'':-^54}")
     for data in pList:
          if word in data[1]:
             print(" 번호    이름       전화번호              주소"),
             print(f"{'':-^54}")    
             print(f"  {data[0]}     {data[1]}   {data[2]}    {data[3]}") 
             print(f"{'':-^54}")   
     else:
          print("검색 결과가 없습니다.")     
      
      

choice = 0
#사용자가 종료할떄까지 무한 반복해서 함수 호출
while True:
        #반환값을 정수로 변환 후 변수에 저장
        choice  = int(menu())
        # 5가 입력되면 break 를 통해 whule문을 탈출
        if choice == 1: 
              print('1.입력 2.출력 3. 검색 4.수정 5.삭제 6.종료'),
              print(f"{'입력기능':-^50}"),
              insert((input(" 이름 : ")),(input(" 전화번호 : ")),(input(" 주소 : ")))
        if choice == 2:
             print('1.입력 2.출력 3. 검색 4.수정 5.삭제 6.종료'),
             print(f"{'출력기능':-^50}"),show(pList)
        if choice == 3:
             print('1.입력 2.출력 3. 검색 4.수정 5.삭제 6.종료'),
             
             print(f"{'검색기능':-^50}"),search(pList)
             
        if choice == 4:
               print(f"{'수정기능':-^30}")
               target_id = int(input("수정할 데이터 번호: "))
               for data in pList:
                    if data[0] == target_id:
                         data[1] = input("새 이름: ")
                         data[2] = input("새 전화번호: ")
                         data[3] = input("새 주소: ")
                         print("수정 완료.")
                         break
               else:
                    print("해당 번호의 데이터가 없습니다.")
        if choice == 5:
               print(f"{'삭제기능':-^30}")
               target_id = int(input("삭제할 데이터 번호: "))
               for i, data in enumerate(pList):
                    if data[0] == target_id:
                         del pList[i]
                         print("삭제 완료.")
                         break
        else:
                    print("해당 번호의 데이터가 없습니다.")
        if choice == 6:
           break

print("종료!")