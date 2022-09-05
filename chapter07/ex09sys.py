# sys모듈 : sys는 파이썬 자체를 의미. 직접 사용하진 않음.
'''
>>> import sys
>>> sys.prefix
'C:\\ProgramData\\Anaconda3'
파이썬의 버전 확인
>>> sys.version
'3.9.12 (main, Apr  4 2022, 05:22:27) [MSC v.1916 64 bit (AMD64)]' 
저작권확인
'''

# os:PATH : 명령어를 찾는 곳 지정. 
# a.exe를 찾을 때 어디서 찾아야하는가.

# sys.path 모듈을 찾는 곳 지정
'''
>>> import sys
>>> for p in sys.path:
... print(p)
  File "<stdin>", line 2
    print(p)
    ^
IndentationError: expected an indented block
>>> for p in sys.path:
...  print(p)
...

C:\ProgramData\Anaconda3\python39.zip
C:\ProgramData\Anaconda3\DLLs
C:\ProgramData\Anaconda3\lib
C:\ProgramData\Anaconda3
C:\ProgramData\Anaconda3\lib\site-packages
C:\ProgramData\Anaconda3\lib\site-packages\win32
C:\ProgramData\Anaconda3\lib\site-packages\win32\lib
C:\ProgramData\Anaconda3\lib\site-packages\Pythonwin
>>>

'''