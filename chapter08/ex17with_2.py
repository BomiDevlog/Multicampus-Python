# with 문법 : with ~ as문
try:
    # open 성공하면 변수 f에 배정됨 : 파일 열기
    with open('hello3.txt', 'r', encoding='utf-8') as f:
    # open 실패해서 예외 발생 -> 예외처리
        data = f.read()
        print(data)
        # with 코드블럭을 벗어날 때 close() 자동 호출 : 파일 닫기
        # finally에서 할 일이 없음. with에서 대신해주기 때문.
except Exception as e:
    print(e)


print("=====================")

'''
(base) C:\python\chapter08>python -u "c:\python\chapter08\ex17with_2.py"
Traceback (most recent call last):
  File "c:\python\chapter08\ex17with_2.py", line 4, in <module>
    with open('hello3.txt', 'r', encoding='utf-8') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'hello3.txt'

파일이 없는 경우 예외 발생
'''

# 파일 열고 닫기 할 때 기본 메커니즘. with 내의 실행문을 상황에 맞게 변경

# -> fileutil 업그레이드

'''
# 파일 핸들링할 때 가장 안전한 코드니까 통째로 외우기

try:
    with open('hello.txt', 'r', encoding='utf-8') as f:
        pass
except Exception as e:
    print(e)

'''

'''
.csv
엑셀에서 관리할 수 있는 파일
콤마 세퍼레이티드 . 값이 콤마로 구분

text파일

#아두이노 수업 때 mysql에 데이터 수집한걸 사용할 것

첫줄은 엑셀헤드에 해당. mysql 컬럼

'''