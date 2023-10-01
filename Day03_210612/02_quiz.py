#02_quiz.py
#리스트 관련 문제

num=[5, 8, -1, 9, 6]

size=len(num)  #요소의 갯수 5
print(num)


##문1) 음수의 갯수를 구하시오
"""
생각 1단계
    if 5<0   -> if num[0]<0
    if 8<0   -> if num[1]<0
    if -1<0  -> if num[2]<0      -> 이 줄만 count=0+1 하면 됨
    if 9<0   -> if num[3]<0
    if 6<0   -> if num[4]<0
인가요? 를 의미함. 이걸 이제 코딩하면 됨.
"""
##풀이1)
count=0
for i in range(len(num)):         #0~4까지 반복
    if num[i]<0 : count=count+1   #num[i]값이 0보다 작으면 count+1 하라.

print("음수의 갯수 : %d" % count)  #%d에 count 대입하라.

##풀이2)
count2=0
for n in num:
    if n<0 : count2+=1

print("음수의 갯수 : %d" % count2)

#==========================================================================

##문2) 양수 중에서 홀수의 합을 구하시오
"""
생각단계
    if 5>0 and 5%2==1(홀수) -> if num[0]>0 and num[0]%2==1   -> hap=hap+5
    if 8>0 and 8%2==1       -> if num[0]>0 and num[0]%2==1
    ....
"""
hap=0
for i in range(size):
    if num[i]>0 and num[i]%2==1: hap=hap+num[i]

print("양수 중에서 홀수의 합 : %d" % hap)

#==========================================================================

##문3) num[4]의 등수를 구하시오
"""
생각단계 : 각 요소와 num[4] 요소의 값 비교하며 등수 카운트하면 됨
    if 6<5      if num[4]<num[0]
    if 6<8      if num[4]<num[1]  -> 맞음 : rank=1+1    
    if 6<-1     if num[4]<num[2]
    if 6<9      if num[4]<num[3]  -> 맞음 : rank=2+1
    if 6<6      if num[4]<num[4]
"""
rank=1
for i in range(size):
    if num[4]<num[i]: rank=rank+1

print("num[4]요소의 등수 : %d" % rank)

#==========================================================================

##문4) num리스트 요소의 각각의 등수를 구하시오
grade=[1, 1, 1, 1, 1]
"""
    if num[0]<num[0]
    if num[0]<num[1]
    if num[0]<num[2]
    if num[0]<num[3]
    if num[0]<num[4]

    if num[1]<num[0]
    if num[1]<num[1]
    if num[1]<num[2]
    if num[1]<num[3]
    if num[1]<num[4]

    ...반복 되는 형식
    -> 앞에 num[i] 이고, 뒤에 num[j] 로 생각하고 밑에처럼 풀이된거임.
    !과제! 문제 4번 분석 다시 한 번 더 생각해보기.

"""
for i in range(size):    #0~4
    for j in range(size):     #0~4
        if num[i] < num[j]: grade[i]=grade[i]+1

print(grade)




