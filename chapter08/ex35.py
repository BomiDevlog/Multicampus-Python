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
'''

import os

file_path = 'temp'
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

'''
존재 여부:  False
파일 여부:  False
디렉토리 여부:  False
'''