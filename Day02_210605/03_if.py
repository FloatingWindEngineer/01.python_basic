#03_if.py

###성적프로그램
name='코로나'
kor=40
eng=60
mat=50
aver=(kor+eng+mat)//3           # // : 정수값 출력       / : 실수값 출력

print("이름:%s" % name) 
print("국어:%d" % kor) 
print("영어:%d" % eng)   
print("수학:%d" % mat)  
print("평균:%d" % aver) 

#문1) 평균이 95점 이상이면 장학생 출력
if aver>=95: print("장학생")
else:                         
    print("장학생 아님")
#만약에 aver가 95보다 작은데, else 문장이 없으면 출력 아무것도 안됨



#문2) 국어점수가 70점 이상이면 국어:합격
#    아니면 국어:불합격
if kor>=70:
    print("국어:합격")
else:
    print("국어:불합격")



#문3) 수학점수 90점 이상이면 수학:A학점
#             80점 이상이면 수학:B학점
#             70점 이상이면 수학:C학점
#             60점 이상이면 수학:D학점
#             나머지는 수학:F학점
if mat>=90:
    print("수학:A학점")
elif mat>=80:
    print("수학:B학점")
elif mat>=70:
    print("수학:C학점")
elif mat>=60:
    print("수학:D학점")
else:
    print("수학:F학점")




#문4) 과락 (or 조건)
#  평균이 70점 이상이면, 결과 : 합격
#  단, 국영수 세 과목 중에서 한 과목이라도 40점 미만이면, 결과 : 재시험
#  평균이 70점 미만이면, 결과 : 불합격
if aver>=70:
    print("결과:합격")
    if kor<40 or eng<40 or mat<40:
        print("결과:재시험")
else:
    print("결과:불합격")

"""
내가 쓴 틀린 답 내용...!
if aver>=70:
    print("합격")
elif kor<40 or eng<40 or mat<40       ==> 이 줄이 틀림! elif가 아니라 if 사용해야 함.
    print("재시험")
else:
    print("불합격")
"""



#문5) 과락 (and 조건)                  -> 문4 를 and 조건 사용해서 풀이하는 방법
if aver>=70:
    if kor>=40 and eng>=40 and mat>=40:       
        print("결과:합격")
    else:
        print("결과:재시험")
else:
    print("결과:불합격")


#=========================================================================
#=========================================================================


## 간단한 계산기 프로그램
a=3
b=5
op='%'       #문자열값 설정한 것
"""
    실행결과
    3+5=8
    3-5=-2
    3*5=15
    3/5=0.6      -> 이것만 혼자 소수점이 존재
    3%5=3
"""

result=0     #나중에 result 사용하려고 지금 그냥 초기값을 0으로 설정한 것.

if op=='+':
    result=a+b
elif op=='-':
    result=a-b
elif op=='*':
    result=a*b
elif op=='/':
    result=a/b
elif op=='%':
    result=a%b           #result=15로 변경됨.

if op=='/':
    print("%d %s %d = %.1f" % (a, op, b, result))  #실수값 출력

else:
    print("%d %s %d = %d" % (a, op, b, result))    #정수값 출력


