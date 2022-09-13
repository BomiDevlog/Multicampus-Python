# csv
# 파일 처리할 때 

from datetime import datetime
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

try:
    with open('sensors.csv', 'rt', encoding='utf-8') as f:
        data = f.readlines() # 파일 관련 작업은 여기까지이기에, for문은 with밖에서 작업해도 됨.

    result = [] #새로운 리스트 생성
    for row in data[1:]: # 데이터를 다듬는 후속작업. # slicing : 두번째부터 끝까지
        row = row.strip().split(',') #개행문자 제거, 콤마단위 분할 #row의 참조가 변경됨. ->원본도 조작하려면 작업 필요함
        row[0] = int(row[0])    # ID -> int 변환
        row[3] = float(row[3])  # VALUE -> float 변환
        row[4] = datetime.strptime(row[4], DATE_FORMAT)  #CREATED_AT : 날짜문자열 -> datetime
        result.append(row)
        print(row)

        # 데이터분석할 때 
        # csv 표준모듈 : 개행문자제거해서 콤마단위 분할하는 부분까지 처리해줌 9~13번라인
        # pandas : 알맞은 데이터타입으로 형변환까지 처리해줌. 엑셀기능을 대부분 가지고있음. 9~16번라인. 통계, 정렬, 피벗 등
        # 데이터분석 시 pandas가 가장 유용한 써드파티모듈

    # header, data = data[0], data[1:]
    header, data = data[0].strip().split(',') , result
    # header에 대한 전처리작업. result라는 새로운 리스트를 생성해서 row를 배정.

    print(header) #리스트로 나와야하는데 문자열
    print("="*80)
    # 가독성을 높이기 위해 for루프
    for row in data:
        print(row)
        # 18번라인과 같은 결과. 원본도 같은 형태로 조작한 것.
        # 분석가능. 평균기온. 온도변화 그래프. 습도 변화 그래프. 최저온도 최고 온도 등을 찾아 줄 수 있다.

    # print(data) 
    # 문자열=> 작업내용이 원본에는 처리가 안되어있다. 
    # (17번라인  print(row) 과 결과가 다름
    # -> row = row.strip().split(',') 12번라인 때문에 일어나는 일)
    '''
    row = row.strip().split(',') 12번라인으로 인해 row에 대한 참조가 바뀌었기 때문이다.
    row는 문자열str. 파이썬의 문자열은 불변객체
    strip에 의해 str복사본
    split에 의해 리스트 생성
    즉 12번라인 이후 원본이 아닌 새로운 리스트를 조작한 것이며 원본에는 아무 변화가 없음
    => result라는 새로운 리스트를 생성해서 row를 배정.
    '''

except Exception as e:
    print(e)

'''
ex30.py의 출력상태

19,livingroom,temp,28,"2022-08-31 12:23:38"

개행문자 제거가 안되었기때문에 엔터 빈줄이 들어감
데이터로써 날짜에 따옴표까지 들어감 -> 제거해야함
콤마단위로 끊음 -> 리스트로 변경
데이터는 전부 문자열이라 변환 필요
'''

'''
다시실행하니 에러

Microsoft Windows [Version 10.0.19044.1889]
(c) Microsoft Corporation. All rights reserved.

C:\python>python -u "c:\python\chapter08\ex30_3.py"
[Errno 2] No such file or directory: 'sensors.csv'

C:\python>C:/ProgramData/Anaconda3/Scripts/activate

(base) C:\python>conda activate base

(base) C:\python>


워킹디렉토리문제. 상대경로로 'sensors.csv'를 써주어서

(base) C:\python>cd chapter08 해주고 실행하니 정상실행
'''

'''
자료에 맞게 형변환해야한다.

아이디는 인테저
플래이스랑 타입은 그대로 문자열
밸류는 플로트
크레이티드 앳은 데이트타임해야함 원본에서 ""쌍따옴표 제거하는 전처리작업해야함.
sensors.csv에서 문자열교체작업 : 컨트롤+에이치해서 리플레이스로 "를 빈문자로 교체함
'''

'''
invalid literal for int() with base 10: 'ID'
10 진수기반의 수가 아니라서 형변환이 안된다.
1번째 라인은 무시하고 2번째 라인부터 형변환 -> slicing
'''
# 첫번째부분은 여전히 헤더임. 그러니 실제데이터 리스트와 헤더 리스트를 분리해주는 작업