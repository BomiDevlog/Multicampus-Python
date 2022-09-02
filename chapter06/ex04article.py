# cnn에서 임의의 뉴스기사를 copy&paste해서,
# article의 문자열에 나오는 글자(spelling)의 출현 횟수를 계산

article = '''
A cargo vessel carrying 3,000 metric tons of corn from Ukraine that was stranded in the Bosporus Strait has been anchored and traffic has resumed, Turkey's General Directorate of Coastal Safety said Friday. 

The ship, Lady Zehma, was traveling from the Black Sea to Ravena, Italy when it ran aground due to rudder failure and became stranded on Thursday. 

The ship has been towed and is now anchored in Istanbul's Bebek Bay, the General Directorate tweeted Friday. 

Traffic had been suspended, but has since resumed, it added. 
'''

# 전처리작업으로 인용부호 제거하고 , 대소문자 통합시키면 -> 알파벳 빈도수 측정을 할 수 있다

# remove, del 등은 작업량이 많아짐. 
# comprehension으로 filter작업해서 부호 제거 -> 글자만 분석할 수 잇음.
article = [ ch for ch in article if ch not in [' ', '\n', '.', ',','\'','\"'] ]

spel_count = {} # 빈 딕셔너리 생성

# 문자열은 문자열 콜렉션. 
# 문자열 자체를 주어서 글자한글자한글자를 loop에서 계산


# 문자열일 때는 ch는 문자 하나하나가 됨.
for ch in article :
    spel_count[ch] = spel_count.get(ch, 0) +1

# -------------------
# 콜렉션이 무엇이냐에 따라 x가 결정됨 
# for i in range(10) :
#     i는 index번호
# for x in spel_count :
#     print(X) x는 key값
#  ---------------------

# print(spel_count.items())
#() 리터럴을 보니 tuple임을 알수있다
# for x in spel_count.items() : # 튜플을 언팩함
#     print(x) // x[0], x[1]

for ch, count in spel_count.items() :
    print(f'{ch} : {count}')


# 딕셔너리는 정렬할 수 없다 -> 리스트로 형변환해서 정렬 

ch_list = list(spel_count) # ch_list = list(spel_count.keys()) 와 같은 결과.
# print(ch_list)  # key값만 list에 담긴다.

ch_list.sort()  # key값의 오름차순 정렬

for key in ch_list :
    print(f'{key} : {spel_count[key]}')
# key는 리스트에 바로 있고, value값은 딕셔너리에서 key에 대응하는 값으로 매칭함!
# key값이 딕셔너리에 있다는 것이 보장되기때문에 get을 사용하지 않아도 됨.
# 정렬결과는 아스키코드의 배치상, 숫자, 대문자,소문자가 오름차순으로 나온다. 

# ------------------

# value로 빈도 수 정렬의 경우

# list(spel_count.values()) 
# value값을 뽑아내서 정렬하더라도, 밸류에 대응하는 키값을 찾을 수 없다.
# 즉 정렬하더라도 출력할 수 없다.


# 키워드 pass : 코드블럭 정의안하면 빨간줄에러. 아직 함수내용을 정하지못했을 때 pass하면 내부정의는 안했지만 함수로서 형태는 갖춤


items = list(spel_count.items())
print(items) # key와 value가 튜플로 들어있다

def what_key(x) :
    # pass
    # print(x) #매개변수x가 무엇인지 알아보는 확인용
    # sort에서 오는 element를 매개변수로 받는다.
    return x[1] #리턴하는 값을 기준으로 element를 받는다. -> 정렬하기를 원하는 두번째 엘리먼트(value값)를 지정함.

items.sort(key=what_key, reverse=True) #(매개변수명 = 함수명) . 마치 콜백처럼 동작.
# 마치 JS의 forEach(f),each(f) 매개변수에 함수를 지정하면 element가 하나씩 전달됨.
# value값 내림차순 정렬 -> 빈도 수

# items.sort() # 튜플에서 첫번째 element (key값)으로 정렬됨
# 컨트롤키를 누르고 sort에 마우스를 가져다 보라

# 특수한 형태의 리스트를 정렬하려면? (리스트안에 콜렉션(튜플 등)이 있으니 특수 형태)

# items가 count값으로 정렬된다면
# for ch, count in items : 
#      print(f'{ch} : {count}')


# --------데이터 분석 과정
# 분석할 데이터 준비
# 전처리해서 다듬고
# 통계내고
# 통계결과를 이해하기 쉽게 출력 (도표 등 이용)

# 빈도수가 가장 많은 데이터 5개만 가져오려면?
# 앞의 5개만 가져오면됨 -> slicing
for ch, count in items[:5] :  # Top-N문제 (상위 n개만 골라내는 문제)
     print(f'{ch} : {count}')