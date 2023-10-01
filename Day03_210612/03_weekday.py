#03_weekday.py
#요일 구하는 프로그램
"""
    서기 1년 1월 1일 ~ 서기 2021년 6월 12일 까지의 총 날수
    총 날수%7 -> 0(일), 1(월), 2(화), 3(수), 4(목), 5(금), 6(토) 각 숫자에 해당하는 요일임.

    1단계) 서기 1년 ~ 서기 2020년 총 일수
        윤년 += 366
        평년 += 365

    2단계) 1월 ~ 5월 총 일수
        +=31 -> 1 3 5 7 8 10 12
        +=30 -> 4 6 9 11
        +=29 -> 2 (윤년)
        +=28 -> 2 (평년)

    3단계) total += 12

"""

cYear=2021  #해당 년도
cMonth=6    #해당 월
cDate=12    #해당 일

total=0     #총 날수

##1단계) 
for y in range(1, cYear):   #1~2020
    if y%4==0 and y%100!=0 or y%400==0:  #윤년?
        total=total+366
    else:
        total=total+365

##2단계)
dal=[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]   #-> 0 & 1월~12월 각 일수 list up
if cYear%4==0 and cYear%100!=0 or cYear%400==0: dal[2]=29

for m in range(1, cMonth):
    total = total + dal[m]

##3단계)
total = total + cDate

print("총날수: %d" % total)

if total%7==0:
    print("일요일")
elif total%7==1:
    print("월요일")
elif total%7==2:
    print("화요일")
elif total%7==3:
    print("수요일")
elif total%7==4:
    print("목요일")
elif total%7==5:
    print("금요일")
elif total%7==6:
    print("토요일")


    