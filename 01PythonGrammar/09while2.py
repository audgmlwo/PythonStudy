'''
1~20까지 숫자중 홀수만 출력 (단, continue 사용)
'''

a = 1
while a<= 20:
    if a % 2 ==0 :
        #짝수인 경우 단순히 1증가 시킴
        a = a+1
        continue
    #반복문 안에서 만나면 처음으로 돌아간다.
    else:
        #홀수인 경우 출력
        print(a, end=' ')
        a += 1

print()
print("="*30)

'''
구구단을 출력하시오.
'''

dan = 2
while dan <= 9 :
    su = 1
    while su<=9:
        print("%d*%d=%2d" % (dan, su, su*dan), end=' ')
        su += 1
    dan += 1
    print()

print()
print("="*30)

'''
구구단을 출력하되, 짝수단만 출력
'''
dan = 2
while dan <= 9:
    if dan%2 == 1:
        dan += 1
        continue
    else:
        su = 1
        while su <= 9:
           print("%d*%d=%2d" % (dan, su, su*dan), end=' ')
           su += 1
    dan += 1
    print()
print()