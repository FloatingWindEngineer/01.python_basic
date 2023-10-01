#04_math.py
#모듈     : 파이썬 코드를 논리적으로 묶어서 관리하고 사용할 수 있도록 하는 것
#패키지   : 모듈들을 모은 컬렉션

#수학 관련된 모듈(기능) 선언
import math             # @ 이거 선언 해줘야 밑에 줄부터 math 수식(파이/소수점 올림/내림) 사용가능 


#절대값   => 절대값 만들어주는 함수가 존재(abs) -> 함수 존재하는게 딱 엑셀과 같네
print(abs(-3))
print(abs(3))
print(abs(-2.4))
print(abs(2.4))

#최대값
print(max(1,3,5))

#최소값
print(min(-1,-3,-5))

#반올림
print(round(123.679, 2))     #출력값 : 123.68

#파이값 출력 (3.14~~~)     #### 24줄 밑에 수식들 사용하려면 위에 수학 모듈 선언 꼭 해줘야 함!
print(math.pi)            

#소수점값 올림             # (math.ceil)
print(math.ceil(2.2))     #3
print(math.ceil(3.5))     #4

#소수점값 내림             # (math.floor)
print(math.floor(2.4))    #2
print(math.floor(3.5))    #3


