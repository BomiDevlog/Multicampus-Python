# random 모듈 테스트

import random

print(random.random())
print(random.randrange(1,10))

# 파일명이 random.py라고 하면 에러남. 
# path를 잡을 때 현재 디렉토리를 가장 먼저 찾는데, 
# 그 때 해당 파일이 그대로 import되어 파이썬 내장함수가 작동하지 않아서.
