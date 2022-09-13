# 디렉토리 관리함수
# os.listdir(d) 자주 사용!!

import os

files =os.listdir('/temp') # 읽고싶은 디렉토리 경로입력. # '.'현재디렉토리 # '../chapter02'
# 목록에 디렉토리도 존재함. #알파벳순으로 정렬


for f in files:
    print(f)

