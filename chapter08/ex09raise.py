# raise : java의 throw 
# 예외 이유 서술해야함

from msilib.schema import Directory


def get_ans(ans):
    if ans in [ '예', '아니오'] :
        # []리스트 ()튜플로 해도됨
        # {}사전은 부적합. 현재는 값 2개를 비교하는 상황이다. 사전은 키-밸류를 확인하기때문에 이 문제에는 안맞음.
        print('정상적인 입력입니다.')
    else:
        raise ValueError('입력을 확인하세요.')
    
while True:
    try:
        ans = input('예/아니오 중 하나를 입력하세요 :')
        get_ans(ans)
        break
    except Exception as e:
        print('error :', e)

# ------------------------------------- 
# I/O 입출력
# cpu - 메모리를 제외한 외부장치와 데이터를 주고받는 것을 입출력(input/output) 이라고한다
# input/output의 기준은 CPU를 기준으로 방향을 본다
# 외부장치에서 cpu-메모리 쪽으로 데이터가 들어가는 것을 입력
# 반대로 나가는 것을 출력
# 외부장치 : 키보드, 마우스, 하드디스크 등. 하드디스크의 파일을 핸들링하는 것도 I/O

# 파일 입출력
# 파일명 a.jpg 만으로는 파일을 찾을 수 없고,
# 어디에 있는 파일인지 파일 경로(path)도 알아야함.
# # (path : 파일이 어디에 있는지 프로그램언어에서 문자열로 서술하는 방법)
# 어디를 거쳐가느냐 폴더(디렉토리) 
# # ( 커맨드(cmd)기반의 텍스트가 cd -> 디렉토리 이동. 폴더는 그래픽적 개념. 폴더와 디렉토리는 유사개념.)
# "/Temp/a.jpg" /(슬래시)가 경로에서 제일 앞에 있으면 루트 디렉토리, 경로의 중간에 있으면 디렉토리 구분자
# cf: os별로 다름  windows '\'역슬래시 Mac, Linux '/' 슬래시 
# 역슬래시는 '\' escape문자이기에 \t는 tab으로 인식. "\\Temp\\a.jpg"
# 파이썬이 "/Temp/a.jpg"로 입력해도 운영체제에 맞게 윈도우즈는 자동으로  "\\Temp\\a.jpg"로 인식해줌 
# 그래서 슬래시로 표기하겠음.
# "/temp/a/b/c.jpg" path
# C: 드라이브는 생략가능.

# 경로(path)-절대경로 : 루트부터 기술 /temp/a.jpg
#           -상대경로 : 루트부터 기술하지 않는다 temp/a.jpg, a.jpg

# working directory 작업 디렉토리
# 커맨드창에서 어디서 작업하는지 중요하기때문에 보여줌
# 홈 디렉토리가 디폴트 워킹디렉토리가 된다.
# 최초의 터미널을 띄울때 프로젝트 디렉토리가 열림 =>PYTHON

'''
C:\python>dir
 C 드라이브의 볼륨에는 이름이 없습니다.
 볼륨 일련 번호: 9EF2-0B7F

 C:\python 디렉터리

2022-09-06  오전 11:12    <DIR>          . 현재 디렉터리
2022-09-06  오전 11:12    <DIR>          .. 상위 디렉터리
2022-08-31  오후 03:19    <DIR>          chapter01
2022-08-31  오후 04:32    <DIR>          chapter02
2022-09-01  오후 02:26    <DIR>          chapter03
2022-09-01  오후 03:01    <DIR>          chapter04
2022-09-05  오전 11:46    <DIR>          chapter04_2
2022-09-02  오후 02:05    <DIR>          chapter05
2022-09-05  오전 10:05    <DIR>          chapter06
2022-09-05  오후 03:21    <DIR>          chapter07
2022-09-06  오전 11:12    <DIR>          chapter07_2
2022-09-06  오후 12:16    <DIR>          chapter08
2022-09-06  오전 10:13                 0 conda
               1개 파일                   0 바이트
              12개 디렉터리  77,089,546,240 바이트 남음

# 이름을 조금 치고 탭키 누르면 자동완성. 절대경로입력.
C:\python>dir \python\chapter01\ex01helloworld.py
 C 드라이브의 볼륨에는 이름이 없습니다.
 볼륨 일련 번호: 9EF2-0B7F

# 상대경로. 워킹디렉토리까지는 서술안해도 됨.
 C:\python\chapter01 디렉터리

2022-08-31  오후 03:24               775 ex01helloworld.py
               1개 파일                 775 바이트
               0개 디렉터리  77,089,218,560 바이트 남음

C:\python>dir chapter02\ex02-2variable.py
 C 드라이브의 볼륨에는 이름이 없습니다.
 볼륨 일련 번호: 9EF2-0B7F

 C:\python\chapter02 디렉터리

2022-08-31  오후 03:38               922 ex02-2variable.py
               1개 파일                 922 바이트
               0개 디렉터리  77,092,290,560 바이트 남음

C:\python>

상대경로로 입력하는게 사람이 작업하기에 편한데
기계가 작업할 대는 절대경로가 더 정확함.

C:\python>cd .

C:\python>cd ..

C:\>cd python

C:\python>cd chapter02

C:\python\chapter02>cd ..\chapter03

C:\python\chapter03>cd ..\..

C:\>

'''
