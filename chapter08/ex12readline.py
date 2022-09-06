#  readline() : line 단위로 읽고싶을 때. 개행문자가 나올때까지 읽음.

# AAA\n
# BBB\n
# CCC 

f=open('foo.txt', 'r')  # 1. 파일 열기

s=f.readline()          # 2. 파일의 첫번째 줄을 읽는다
print(s, end='')        #    출력

s=f.readline()          #    파일의 두번째 줄을 읽는다
print(s, end='')        #    출력

s=f.readline()          #    파일의 세번째 줄을 읽는다
print(s, end='')        #    출력

s=f.readline()          #    파일의 네번째 줄을 읽는다
# print(s, end='')        #    출력 -> 없는 줄. 출력되지 않음
print(type(s), end='') 
# 더이상 읽을 수 없는 상태에서 비어있는 문자열이 반환된다.
# 텍스트는 비어있는 문자열, 바이너리는 None이 반환됨


f.close()               # 3. 파일 닫기
