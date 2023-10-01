#07_for.py
#for 반복문
"""
    for 변수 in range(시작값, 종료값-1, 증감값):
        반복할 명령어
"""

for a in range(1,5,2):   # 1~4 중에서 2씩 증가
    print(a)

for b in range(1,5):     # 1~4 중에서 1씩 증가 (셋째 칸 공란이면 1이 숨어져 있는 의미)
    print(b)

for c in range(5):       # 0~4 중에서 1씩 증가 
    print(c)             # 0 1 2 3 4

#================================================================

# for 반복문을 이용한 (구구단) 4단 출력
"""
우선 내가 푼거...
for d in range(4,37,4):
    print(d)
"""
dan=4
for n in range(1, 10):
    print("%d * %d = %d" % (dan, n, (dan*n)))

# 2단~9단 출력하시오
for dan in range(2,10):
    print("%d단" % dan)
    for n in range(1, 10):
        print("%d * %d = %d" % (dan, n, (dan*n)))
        




