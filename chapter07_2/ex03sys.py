# sys모듈 테스트 
import sys

for path in sys.path:
    print(path)

'''
PS C:\python> python -u "c:\python\chapter07_2\ex03sys.py"
c:\python\chapter07_2   # 현재디렉토리를 가장 먼저 찾아본다.
C:\ProgramData\Anaconda3\python39.zip
C:\ProgramData\Anaconda3\DLLs
C:\ProgramData\Anaconda3\lib
C:\ProgramData\Anaconda3
C:\ProgramData\Anaconda3\lib\site-packages
C:\ProgramData\Anaconda3\lib\site-packages\win32
C:\ProgramData\Anaconda3\lib\site-packages\win32\lib
C:\ProgramData\Anaconda3\lib\site-packages\Pythonwin

'''

# sys는 특수한 내장모듈.
# 파일명이 sys.py라도 상관없이 import되어 작동.
# sys외에는 이름충돌 주의