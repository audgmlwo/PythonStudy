'''
퀴즈] 다음과 같은 메트릭스를 출력하는 프로그램을 for문으로 작성하시오.

1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1
'''


for i in range(0,4,1):
    for j in range(0,4,1):
        if i == j :
            print("1",end=" ")
        else :
            print("0",end=" ")    
    print()

'''
퀴즈] 다음과 같은 피라미드를 출력하는 프로그램을 for문으로 작성하시오.

*
**
***
****
*****
'''
print()
print("="*30)

for i in range(0,5,1):
    for j in range(0,5,1):
        if i >= j :
            print("*",end=" ")
        else :
            print(" ",end=" ")    
    print()

'''
    *
   ***
  *****
 *******
*********
  

'''    
       
print()
print("="*30)   

j_max = 7
for i in range(1,j_max,):
    for j in range(1,j_max,1):
        if i+j < j_max :
            print("",end=" ")
        else :
            print("*",end=" ")    
    print()

print()
print("="*30)

j_max = 7
for i in range(1, j_max + 1):  # 1부터 j_max까지
    for j in range(1, j_max * 2):  # 1부터 j_max*2-1까지 (가로 폭)
        if j <= j_max - i or j >= j_max + i:  # 공백 조건
            print(" ", end="")
        else:  # 별 출력
            print("*", end="")
    print()  # 한 행 끝난 후 줄바꿈

print()
print("=" * 30)

NUM = 7

for i in range(0,NUM,1):
    # @를 출력하는 부분
    for j in range(0,NUM - i + 1,1):
        print(" ", end="")
    
    # *를 출력하는 부분(1,3,5 형태로 출력)
    for k in range(0,i * 2 + 1,1):
        print("*", end="")
    
    # 줄바꿈 처리
    print(" ")
print(" ")    
print("=" * 30)

j_max = 3
for i in range(1, j_max * 2):  # 1부터 j_max까지
    for j in range(1, j_max * 2):  # 1부터 j_max*2-1까지 (가로 폭)
        if j <= j_max - i or j_max + i <= j:  # 공백 조건     
            print(" ", end="")
        else:  # 별 출력
            print("*", end="")
    print()  # 한 행 끝난 후 줄바꿈

print()
print("=" * 30)

''' 5*5 1,6 // 0,5
12345 
 234
  3
 234
12345  

##### 
1###5
12#45         j(1,2) < j_max(3) < j(4,5)  i=3  12 3 45
                
1###5
#####

'''


