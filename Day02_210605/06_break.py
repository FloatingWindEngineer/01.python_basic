#06_break.py

#break
#-> 반복문 안에서 루프를 빠져나오기 위해

# continue
#-> 루프 블럭의 나머지 문장들을 실행하지 않고
#-> 다음 루프로 직접 돌아가게 할 수 있다

a=1
while a<10:
    a=a+1
    if a==5: break       # 반복문을 빠져나감 중단
    print(a)             # 234

print('-'*30)

b=1
while b<10:
    b=b+1
    if b==5: continue    # 루프 블럭 나머지 문장 실행하지 않고, 반복문을 계속 실행
    print(b)             # 2346789  (-> 5없음 : 5일때, continue 때문에 건너뛰어짐)


#===========================================================================
print('='*50)
print('='*50)

# 무한 LOOP : 끝이 없는 반복
a=0
while True:
    a=a+10
    if a==50: break
    print(a)

#===========================================================================

# 문) x값이, 10으로부터 x를 여러 번 뺀후
#     결과가 음수가 되면 x를 몇 번 뺐는지 구하시오 

"""
    10-3=7
    7-3=4
    4-3=1
    1-3=-2
"""
x=3
su=10
c=0

while True:
    c=c+1
    su=su-x
    if su<0: break

print(c)

"""
# 밑에 공식 : 내가 풀이해본 공식:)  -> 답은 맞았는데... while true 랑 break 안썼네...하...

while su>0:
    c=c+1
    su=su-x

print(c)
"""

    




