#  readline() : line 단위로 읽고싶을 때. 개행문자가 나올때까지 읽음. 
# text모드에서만 가능 binary모드에서는 불가.

# 더이상 읽을 수 없는 상태에서 비어있는 문자열이 반환된다.
# '' 비어있는 문자열 --> bool ? False
#  while을 이용해 반복문 구성.

f=open('foo.txt', 'r')  # 1. 파일 열기

data = [] # 빈 리스트 준비 

s = f.readline()          # 2. 파일의 첫번째 줄을 읽는다

while s:                # 3. while문을 통해 
    data.append(s.strip())   #    파일을 라인단위로 리스트에 추가 # strip : 공백문자 제거 (스페이스, 탭, 엔터). 영어로 화이트 캐릭터. 눈에 안보이는 문자.
    # print(s, end='')  #    (출력)
    s = f.readline()    #    파일의 다음 줄을 읽는다
f.close()               # 4. 파일 닫기

print(data)             # 5. 출력

# 다른 언어라면 do~while문을 쓰는데
# 파이썬의 경우 do~while이 없기에 앞에서 첫 문장을 읽고 while문을 시작함.

'''
(base) C:\python\chapter08>python -u "c:\python\chapter08\ex12readline_2.py"
['AAAA\n', 'BB\n', 'CCC']

(base) C:\python\chapter08>python -u "c:\python\chapter08\ex12readline_2.py"
['AAAA', 'BB', 'CCC']
'''