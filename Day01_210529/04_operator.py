#논리연산자
#-> 조건이 2개 이상일때 전체적으로 판단
#-> 결과값은 논리형(boolean)으로 반환된다
#-> and, or, not


##and 연산자
##-> 모든 조건을 만족하면 True
##-> 그리고, ~이면서
print(True and True)
print(True and False)    # 이건 왜 출력값이 False야?
print(False and True)    # 이건 또 왜 출력값이 False야?
print(False and False)   # 이건 왜? 출력값이 False야?? and연산자는 True/False만 나오는게 아닌거???

print()

#or 연산자
#-> 조건들 중에서 하나만이라도 True 이면 True
#-> 또는, ~이거나
print(True or True)
print(True or False)
print(False or True)
print(False or False)

"""
@@@@@@@@@@@@@@@@@@@@@@@
!!!!!!!!!!!!!!!!!
연산자 and / or 모르겠다!!!!!!!!!!!
!!!!!!!!!!!!!!!!!
not 연산자도 모르겠네.... 출력값이 뭐로 나오는건지 ... true 아니면 flase 만 출력되는건가?????
@@@@@@@@@@@@@@@@@@@@@@@
"""

print()

##not 연산자
##-> 부정연산자, ~아니라면
flag=not(3<5)
print(flag)
#----------------------------------------------------------------

print()

#문1) 임의의 정수가 2의 배수이면서 5의 배수인지 확인하시오
num=11
print(num%2==0 and num%5==0)
print(num%10==0)   #윗줄 수식이랑 같은 의미(2의배수&5의배수 이면, 10의 배수) -> 동일한거지만 어떤걸로 함수 만들지 개발자가 고민하는 부분이 이런거래


#문2) 임의의 정수가 1이거나 3인지 확인하시오
code=3
print(code==1 or code==3)
print(code%2==1)   #의미 : 홀수인지?


#문3) 해당년도가 윤년인지 확인하시오
        #윤년 문제는 항상 4년마다 한번은 아니라서 원래 다른 방식으로 풀어야함 
year=not(2021%4!=0)
print(year)
#위에 공식 : 내가 작성 해본 공식 / 아래 공식 : 쌤이 작성한 답 (쌤 답 내용 이해 다시해보기)
year=2021
print(year%4==0 and year%100!=0 or year%400==0)


#문4) 국어점수 80~89점 사이인지 확인하시오
kor=75
print(kor>=80 and kor<=89)
    # 75 >=80     75 <=89
    # False   and True
    # 따라서 False 출력됨
#-----------------------------------------------------------------

print('-' * 30)

#할당 연산자
a=3
a=a+10
a+=10    # 해당 수식은 위에 줄이랑 같은 수식임. 너무 많이 사용해서 이렇게 씀.
print(a)


a-=5     #a=a-5 수식을 줄어여 쓴 수식임
print(a)


a*=2     #a=a*2 수식과 동일한 수식
print(a)


a//=10    #a=a//10  수식과 동일한 수식
print(a)


a%=2     #a=a%2 수식과 동일한 수식
print(a)

