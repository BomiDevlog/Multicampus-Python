# 경로 작업

'''
#디렉토리 관리함수

* os.path 모듈
os.path.isabs(f) 절대경로인지 판단
os.path.abspath(f) 절대경로로 변경
os.path.realpath(f) 링크 관련(윈도우즈에 없는 개념)
os.path.exists(f) 존재하는지 여부.
os.path.isfile(f) 파일인지 디렉토리인지 알고싶을 경우. 파일이면 True
os.path.isdir(f) 파일인지 디렉토리인지 알고싶을 경우. 디렉토리이면 True -- isfile과 isdir은 배타적개념, 둘 다 전제조건으로 파일이 존재해야함
os.path.getsize(f)

os.path.join(경로1, 경로2, ...)
⁃ 인자로 전달된 경로들을 운영체제별 디렉토리 구분자로 결합

join('a','b','c') 가변매개변수이기에 개수 제한 없음
=>'a\b\c' 
윈도우즈 : '\' 역슬래시
Mac, Linux : '/' 슬래시
'''

import os

file_path = 'ex30.py' #'data5.txt'  '__pycache__' 도 해봄
# '.' #상대경로 -> False
# 'temp' # 없는 파일명으로 상대경로 -> False
print(os.path.isabs(file_path)) #절대경로라면 True, 상대경로라면 False

# 문자열로만 판단하여 절대경로,상대경로를 찾음
# 실제 존재하는지는 판단하지않음.

# 상대경로를 절대경로로 변경
file_path = os.path.abspath(file_path)
print(file_path)
# 마찬가지로 실제 존재하는 지는 판단하지 않음
# 문자열로만 판단하여 절대경로로 변경시킴. 
# C:\python\chapter08\temp

print('존재 여부: ', os.path.exists(file_path))
# 존재한다면 True, 존재하지않는다면 False.
# 종종 사용하니 기억하기!! 존재하지 않는다면 에러이니 존재유무를 확인하고 작업함

print('파일 여부: ', os.path.isfile(file_path))
print('디렉토리 여부: ', os.path.isdir(file_path))

print('파일 크기: ', os.path.getsize(file_path))

file_path = os.path.join('a','b','c', 'test.jpg')
print(file_path)

'''
존재 여부:  True
파일 여부:  True
디렉토리 여부:  False

존재 여부:  True
파일 여부:  False
디렉토리 여부:  True
'''

'''
(base) C:\python\chapter08>python -u "c:\python\chapter08\ex35_2.py"
False
C:\python\chapter08\ex30.py
존재 여부:  True
파일 여부:  True
디렉토리 여부:  False
파일 크기:  305

(base) C:\python\chapter08>dir
 C 드라이브의 볼륨에는 이름이 없습니다.
 볼륨 일련 번호: 9EF2-0B7F

 C:\python\chapter08 디렉터리

2022-09-08  오후 12:38    <DIR>          .
2022-09-08  오후 12:38    <DIR>          ..
2022-09-06  오후 04:24                20 data5.txt
2022-09-06  오전 11:20             1,698 ex01try_except.py
2022-09-06  오전 11:24             1,278 ex01try_except_2.py
2022-09-06  오전 11:35               463 ex04try_except.py
2022-09-06  오전 11:35               470 ex06try_else.py
2022-09-06  오전 11:43               742 ex07for_else.py
2022-09-06  오후 12:13               894 ex08finally.py
2022-09-06  오후 02:08             4,742 ex09raise.py
2022-09-06  오후 02:39               663 ex10io-2.py
2022-09-06  오후 02:26             1,348 ex10io.py
2022-09-06  오후 02:47               768 ex11io.py
2022-09-06  오후 03:03               737 ex11io_2.py
2022-09-06  오후 03:04               753 ex11io_3.py
2022-09-06  오후 03:14               728 ex11io_4.py
2022-09-06  오후 03:26               856 ex12readline.py
2022-09-06  오후 03:43               766 ex12readlines.py
2022-09-06  오후 04:05             1,076 ex12readlines_2.py
2022-09-06  오후 03:36             1,282 ex12readline_2.py
2022-09-06  오후 04:09               139 ex12_3module.py
2022-09-06  오후 04:24               480 ex14file_write.py
2022-09-06  오후 04:33               664 ex15file_read.py
2022-09-08  오후 12:44             1,425 ex16file_read2.py
2022-09-06  오후 05:06             1,015 ex16file_read2_2.py
2022-09-06  오후 05:14               357 ex17with.py
2022-09-06  오후 05:40             1,447 ex17with_2.py
2022-09-06  오후 05:45               305 ex30.py
2022-09-06  오후 05:43               165 ex30_2.py
2022-09-08  오전 11:22             4,118 ex30_3.py
2022-09-08  오전 11:22               697 ex31datetime_str.py
2022-09-08  오후 12:16             2,715 ex32파일관리.py
2022-09-08  오후 12:22             3,901 ex33디렉토리관리.py
2022-09-08  오후 12:29               292 ex34listdir.py
2022-09-08  오후 12:38             1,706 ex35.py
2022-09-08  오후 12:45             1,877 ex35_2.py
2022-09-06  오후 05:24               562 file_util.py
2022-09-06  오후 05:22               961 file_util_prior.py
2022-09-06  오후 03:16                13 foo.txt
2022-09-06  오후 05:17                38 hello.txt
2022-09-06  오후 02:28               257 hello2.txt
2022-09-08  오전 11:26                45 live.txt
2022-09-08  오전 10:14             4,405 sensors.csv
2022-09-06  오후 04:45               236 we_will_rock.txt
2022-09-06  오후 04:33    <DIR>          __pycache__
              42개 파일              47,104 바이트
               3개 디렉터리  77,494,022,144 바이트 남음
'''
'''
(base) C:\python\chapter08>python -u "c:\python\chapter08\ex35_2.py"
False
C:\python\chapter08\ex30.py
존재 여부:  True
파일 여부:  True
디렉토리 여부:  False
파일 크기:  305
a\b\c\test.jpg
'''