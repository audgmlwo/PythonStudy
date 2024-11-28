'''
딕셔너리(dictionary)
: 고유키(Key)와 값(Value)로 구성된 집합자료형. key를 통해 저장되므로
자료의 순서는 보장되지 않는다.    
'''

#생성 1 - dict() 함수를 이용해서 딕셔너리 생성.
dic1 = dict(birth = 1970, name = "홍길동", size = "100cm")
print(dic1)

#생성2 - 중괄호를 이용한 생성. (항목 사이를 ':' 구분함)
dic2 = {'원':1, '투':2,'쓰리': 3}
print(dic2)

#반복문을 이용한 딕셔너리 출력
fruits ={'사과':100, '포도':200, '오렌지':300, '복숭아':400 }
print('for문을 이용한 출력')
#먼저 Key를 반복해서 얻어온다.

for key in fruits: #key를 통해 값을 출력
    val = fruits[key]
    print("%s : %d " % (key,val))

#딕셔너리의 크기 반환
print("길이",len(fruits))
print("복숭아",fruits['복숭아'])

#key가 존재하는 경우 기존 값이 변경됨.
fruits['오렌지'] = 3500
print("오렌지", fruits['오렌지'])

#삭제
del fruits['복숭아']
print("복숭아삭제",)

#keys() : 딕셔너리의 key로 구성된 dict_keys 객체를 반환하여
#         사용할 수 있다.
get_keys = fruits.keys()
for k in get_keys:
    print(k)

#values() : 딕셔너리의 value로 구성된 dict_values 객체를 반환
get_values = fruits.values()
for v in get_values:    
    print(v)
