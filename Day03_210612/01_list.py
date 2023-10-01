#01_list.py
"""
    [컬렉션]
    - 연속성 자료형
    - 하나의 변수에 여러개의 값을 저장
    - List, Tuple, Dictionary  => 기본
    - Element, 요소, 원소
    - Index, 색인, 순서 (대부분 0부터 시작해서 1씩 증가한다)
    - DataFrame, Series는 pandas모듈 추가 설치해야 함 (anaconda는 별도 설치하지 않아도 됨)
"""

#List
##1) 1차원 리스트
kor=[90, 85, 73, 64, 100]    #[대괄호] : list  / (괄호) : Tuple
print(type(kor))      #kor변수의 타입 확인 방법 -> <class 'list'>로 출력됨
print(kor[0])         #0번째 요소 출력
print(kor[2])
print(kor[4])
print(len(kor))       #kor리스트 요소의 갯수 : len()

#반복변수 i로 요소 접근
#for i in range(5):          #0~4까지 돌려라
for i in range(len(kor)):    #len(kor)은 5 이므로, 이 문장의미는 0~4까지 돌려라임
    print(kor[i])  

print('-' *30)
#================================================================================

names=['개나리','진달래','무궁화','라일락','홍길동']

for i in range(len(names)):
    print(names[i])

#요소 전체
print(names)

#================================================================================
##2) 2차원 리스트
###-> 행과 열로 구성   *Tip : 행/열은 0부터 시작
students=[
          ['무궁화', 30]
         ,['홍길동', 50]
         ,['오필승', 45]
        ]  #3행 2열  -> 행/열은 0부터 카운트!

print(students[0][0])   #[0행][0열] 출력 -> 무궁화 출력
print(students[0][1])   #[0행][1열] 출력 -> 30

print(students[1][0])
print(students[1][1])

print(students[2][0])
print(students[2][1])

print(len(students))      #3출력  -> stuents의 행의 갯수
print(len(students[0]))   #2출력  -> 0행의 열의 갯수

print('-'*30)

print(students)            #리스트 전체 요소
print(students[0])         #[0]행의 요소
print(students[1])         #[1]행의 요소
print(students[2])         #[2]행의 요소  

#print(students[3][3])  -> 에러 : 3행 3열 요소는 존재하지 않음. List index out of range 출력
#========================================================================================

#1차원 리스트를 묶어서 2차원 리스트를 만들 수 있다.
s1=['무궁화', 30]
s2=['홍길동', 50]
s3=['오필승', 45]

s4=[s1, s2, s3]         #2차원 리스트

print(s4)
#========================================================================================

nums=['ONE','TWO','THREE','FOUR','FIVE']

#1) 리스트 요소 개별 접근
for i in range(len(nums)):
    print(nums[i])

#2) 리스트 요소 개별 접근
for num in nums:          #for 요소 in 전체요소
    print(num)
    





