try:
    f=open('foo.txt', 'r')  # 1. 파일 열기
    data = f.readlines()    # 2. 한 줄 단위로 리스트를 얻음
    data = [line.strip() for line in data] # 3. comprehension으로 filter : 공백 제거
    f.close()               # 4. 파일 닫기

    print(data)             # 5. 출력
except Exception as e:      # 6. 예외 처리
    print('error:', e)

'''
(base) C:\python\chapter08>python -u "c:\python\chapter08\ex12readlines.py"
['AAAA\n', 'BB\n', 'CCC']
strip처리가 안되어있음 -> comprehension으로 filter

(base) C:\python\chapter08>python -u "c:\python\chapter08\ex12readlines.py"
['AAAA', 'BB', 'CCC']

'''

# 자주 쓸 예정! -> 함수화
# 매개변수는 파일 경로(파일명). 리턴값은 data.

