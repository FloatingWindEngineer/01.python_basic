#04_format.py
#출력서식

str1="나는 %d원을 갖고 있다" % 500
print(str1)

#출력 서식 코드를 재사용할 수 있다.
str2="%s날짜는 %d년 %d월 %d일 입니다."

msg1=str2 % ("정모", 2020, 12, 10)
print(msg1)

msg2=str2 % ("번개", 2020, 12, 15)
print(msg2)
#===============================================

#format()함수
msg1="I eat {0} apples"   #0번째
print(msg1.format(3))

msg2="{0}은 {1}년 {2}월 {3}일 입니다."
print(msg2.format("어버이날", 2021, 5, 8))

msg3="{name}은 {yy}년 {mm}월 {dd}일 입니다."
print(msg3.format(name="크리스마스", yy=2021, mm=12, dd=25))

msg4="{0}은 {1}년 {mm}월 {dd}일 입니다."    #-> msg4 (혼용사용)은 잘 사용하지 않음.
print(msg4.format("손흥민", 2019, mm=12, dd=25))




