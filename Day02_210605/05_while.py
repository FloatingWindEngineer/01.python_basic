#05_while.py
#반복문 : while문, for문
#break문, continue문
#무한 LOOP -> 끝 없는 반복
"""
    while 조건: 
        조건이 True이면 처리
        조건이 True이면 처리
        조건이 True이면 처리
"""
#==============================================================

##1) 증가에 따른 반복
i=1
while i<=3:
    print("JAVA")
    i=i+1         #동일 문법 : i+=1 이렇게도 쓸 수 있음 (복습내용)
"""
    상기 while 문법 의미

    while 1<=3   (옳음)   ->   JAVA (출력)   ->   i=1+1 =2 (값으로 i값 재setting)
    while 2<=3   JAVA  i=2+1=3 
    while 3<=3   JAVA  i=3+1=4 
    while 4<=3   (이제 수식 틀리므로  JAVA 출력 못함. 중단됨.
    
    따라서, JAVA 3번 출력될 때까지 반복되는 것임.
"""

##2) 감소에 따른 반복
j=3
while j>=1:
    print("%d PYTHON" % j)
    j=j-1
"""
    while 3>=1  (옳은 수식)   ->   3PYTHON (출력)   ->   j=3-1 =2 (값으로 재setting)
    while 2>=1  2PYTHON  j=2-1=1
    while 1>=1  1PYTHON  j=1-1=0
    while 0>=1  (이제 틀림- > 반복 중단)
"""
#===============================================================

## 4단 출력하기 (구구단)
"""
    4*1=4
    4*2=8
    ...
    4*9=36
"""
dan=4
i=1   #i를 1~9 반복되는 값으로 설정 (4*i)
while i<=9:
    print("%d * %d = %d" % (dan, i, dan*i))
    i=i+1

#================================================================

a=0
while a<=100:
    a=a+10
    print(a)


#================================================================

# 누적, 갯수

#문1) 1~3사이의 누적의 합을 구하시오 (1+2+3)
hap=0
a=1
while a<=3:
    hap=hap+a   #hap+=a
    a=a+1       #a+=1

print("결과:%d" % hap)

"""
    while 1<=3   hap=0+1   a=1+1
    while 2<=3   hap=1+2   a=2+1
    while 3<=3   hap=3+3   a=3+1
    while 4<=3
"""



#문2) 4팩토리얼값 구하기(누적의 곱 4*3*2*1)
gop=1           #곱하기 누적값에 0을 넣으면 안돼. 0곱하면 0이니까!
f=4
while f>=1:
    gop=gop*f
    f=f-1

print("4팩도리얼: %d" % gop)





#문3) 1~10중에서 3의 배수의 갯수를 구하시오
count=0    #결과값 = count  로 설정
a=1        #a = 변수   로 설정
while a<=10:
    if a%3==0: count=count+1
    a=a+1

print(count)

"""
    while 1<=10  if 1%3==0
                a=1+1
    while 2<=10  if 2%3==0
                a=2+1
    while 3<=10  if 3%3==0  count=0+1
                a=3+1
"""





#문4) 서기1년~서기2021년까지 윤년의 갯수를 구하시오
leap=0
year=1
while year<=2021:
    if year%4==0 and year%100!=0 or year%400==0: leap=leap+1    #year%100! : 느낌표 뭐더라??
    year+=1

print(leap)

"""
내가 작성해본 답   ===> 결과값이 다르네!? 틀렸네?!
    윤년은 4년마다 옴 -> 4의 배수

count=0
a=1
while a<=2021:
    if a%4==0: count+=1
    a+=1

print(count)
"""





#문5) 1~100중에서 짝수의 합, 홀수의 합을 각각 구하시오
odd=0   #홀수의 합
even=0  #짝수의 합


"""
# 첫 번째 풀이 방법 (선생님이 알려준 답 주석처리 함. 두 번째 풀이 보려고 공식 숨김)
a=1
while a<=100:
    if a%2==0:
        even=even+a
    # elif a%2==1:    => 이 줄은 굳이 안써도 됨 -> why? 2로 나눴을 때, 나머지는 0 아니면 1 이니까! 
    else:
        odd=odd+a
    a=a+1

print("짝수의 합 %d" % even)
print("홀수의 합 %d" % odd)
"""



# 두 번째 풀이 방법
flag=False     #논리형(boolean형)
a=1
while a<=100:
    if flag:
        even=even+a
        flag=False
    else:
        odd=odd+a
        flag=True
    a=a+1

print("짝수의 합 %d" % even)
print("홀수의 합 %d" % odd)

"""
 두 번째 풀이 방법 설명 참조! 공부해보기!

    while 1<=100   if False
                   else: flag=True
    while 2<=100   if True
                      flag=False
    while 3<=100   if False
                   else: flage=True

                   .....

 @ True/False 반복 실행 됨 @

"""





#문6) 두 수 사이의 수를 전부 더하시오
# 5+4+3+2 = 14
# 2+3+4+5 = 14
start=5
end=2
sum=0    #누적의 합 = sum 으로 설정

#-----------------tip------------------------------------------------------------------
# 만일, start가 end보다 더 크면 변수를 서로 교환(swap)한다. (밑에 if문~n=start문장 추가)
"""
1번 방식) 임시변수 설정

if start>end:
    tmp=start
    start=end
    end=tmp
"""

# 2번 방식) 파이썬에서 변수 맞교환
if start>end:
    start, end=end, start

#--------------------------------------------------------------------------------------
n=start
while n<=end:
    sum=sum+n
    n=n+1

print(sum)
    







