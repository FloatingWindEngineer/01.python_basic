#08_type.py
# 자료형(Datatype)

## 자료형 확인           출력값   의미
print(type(123))        #int    정수형
print(type(45.67))      #float  실수형
print(type('2021'))     #str    문자열형
print(type(True))       #bool   논리형
print(type([1,2,3]))    #list   리스트
print(type((1,2,3)))    #tuple  튜플

## 형변환 Datatype Conversion
## -> 형식 (자료형)값
a=3
b=4.5
c=(float)(a)       # a값을 실수형으로 바꿔라
d=int(b)           # b값을 정수형으로 바꿔라    tip.자료형 수식에 () 안씌워도 됨

print(a)
print(b)
print(c)
print(d)

print(type(a))
print(type(b))
print(type(c))
print(type(d))

