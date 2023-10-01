#08_quiz.py
#함수 관련 문제


#=======================================================================
def graph(ch,num):
    for n in range(num):
        print(ch, end='')  #줄바꿈 없이 출력


def fact(num):
    gop=1
    for n in range(1, num+1):
        gop=gop*n
    return gop


def diff(start, end):
    return abs(start-end)   #절대값을 반환하는 내장함수
    

def leap(y):
    if y%4==0 and y%100!=0 or y%400==0:
        return True
    else:
        return False

#=======================================================================

#문1) @기호 100번 출력하기
graph('@', 100)


#문2) 팩토리얼값 구하는 함수 4*3*2*1
print(fact(4))


#문3) 두 수 사이의 차이를 구하는 함수
print(diff(4, 7))


#문4) 윤년 확인하는 함수
if leap(2021):
    print("윤년")
else:
    print("평년")



