#06_dic.python
#딕셔너리 Dictionary
#이름(key)과 값(value)의 쌍으로 데이터를 정의하는 구조
#{'key':value, 'key':value, 'key':vlaue ~~} 구조로 이루어짐

"""
dic={'name':'무궁화', 'phone':'123-4567','age':25}
print(dic)
print(type(dic))
print(dic['name'])
print(dic['phone'])
print(dic['age'])
print(dic['height'])   -> 이건 에러

# key가 중복될 경우 마지막 하나를 제외한 나머지는 무시됨
data = {'msg':'hello', 'msg':'world', 'msg':'python'}
print(data)   #{'msg':'python'} 출력

# key는 정수형으로도 지정 가능(리스트와 혼동될 수 있으므로 권장하지 않음)
rank = {0:'Python', 30:'R', 10:'Java'}
print(rank[0])
"""
#==========================================================================
"""
# 리스트의 요소가 딕셔너리가 되는 경우 (=JSON 문법이라는 것과 유사한 형태?)
sungjuk = [
             {'name':'무궁화', 'kor':80, 'eng':75}
            ,{'name':'오필승', 'kor':60, 'eng':100}
            ,{'name':'코리아', 'kor':65, 'eng':95}
          ]

style = "{0}의 국어점수:{1}, 영어점수:{2}"
print(style.format(sungjuk[0]['name'],sungjuk[0]['kor'],sungjuk[0]['eng']))
print(style.format(sungjuk[1]['name'],sungjuk[1]['kor'],sungjuk[1]['eng']))
print(style.format(sungjuk[2]['name'],sungjuk[2]['kor'],sungjuk[2]['eng']))
"""
#===========================================================================
"""
#딕셔너리는 리스트나 다른 딕셔너리를 포함할 수 있다.
addr   = ['서울', '서초구', '강남대로']
score  = {'kor':10, 'mat':20, 'eng':30}
member = {
             'userid' :'python'
            ,'age'   : 25
            ,'addr'  : addr
            ,'score' : score
        }

print(member)

## 계층화된 값에 접근하기
print(member['addr'][0])         #서울
print(member['score']['kor'])    #10
"""
#===========================================================================

# 딕셔너리의 계층화 직접 표현
mydic = { 'total'      :1962
         ,'city'       :['서울', '제주', '부산']
         ,'population' :[100, 200, 300]
         ,'date'       :{'yy':2019, 'mm':3, 'dd':5}
        }

print(mydic)
print(mydic['city'][0])         #서울
print(mydic['population'][0])   #100
print(mydic['date']['yy'])      #2019
#===========================================================================
print('-'*30)

#딕셔너리 관련 함수
dic = {'name':'무궁화', 'phone':'123-4567', 'age':25}

print(dic['name'])
print(dic.get('name'))

keys = dic.keys()           #key만 모아서 객체로 변환
print(keys)                 #dic.keys(['name', 'phone', 'age']) 출력됨



