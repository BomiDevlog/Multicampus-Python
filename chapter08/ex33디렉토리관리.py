# 파일 관리
'''
디렉토리 관리함수 

os 모듈 
os.chdir(d)  워킹디렉토리 변경. ch change의 약자. dir 디렉터리의 약자
os.mkdir(d)  디렉토리 생성. make.
os.rmdir(d)  디렉토리 삭제. remove
os.getcwd()  작업디렉토리를 리턴. 겟 커런트 워킹 디렉토리
os.listdir(d) 

glob 모듈
glob.glob(pattern)

'''

import os
import shutil

# os.chdir('..')
# wd = os.getcwd()
# print(wd) 
'''
C:\python\chapter08 현재 워킹디렉터리
cd .. 상위디렉터리 이동했음 -> C:\python 현재 워킹디렉터리
프로그램 자체는 워킹디렉터리를 변경한게 아니라
터미널에서 명령으로 워킹디렉토리를 변경했더니 워킹디렉터리가 달라지고 있다.

프로그램에서 워킹디렉토리를 변경할때 os.chdir(d)을 사용
(base) C:\python>cd chapter08 
(base) C:\python\chapter08>python -u "c:\python\chapter08\ex33디렉토리관리.py"
C:\python
프로그램의 워킹디렉토리를 변경함
(base) C:\python\chapter08>
터미널의 워킹디렉토리는 그대로임.
'''

# ------------------------------

# os.mkdir('images') #상대경로. 터미널의 워킹디렉토리대로 chapter08에 파일 
# os.rmdir('images')   #삭제
'''
(base) C:\python\chapter08>python -u "c:\python\chapter08\ex33디렉토리관리.py"
C:\python
Traceback (most recent call last):
  File "c:\python\chapter08\ex33디렉토리관리.py", line 36, in <module>
    os.mkdir('images') #상대경로. 터미널의 워킹디렉토리대로 chapter08에 파일 생성
FileExistsError: [WinError 183] 파일이 이미 있으므로 만들 수 없습니다: 'images'
한 번 더 실행하니 기존에 있어서 에러

디렉토리에 대해서는, 존재한다면 다시 만들지 않음 ->에러 발생.

(base) C:\python\chapter08>python -u "c:\python\chapter08\ex33디렉토리관리.py"
C:\python
Traceback (most recent call last):
  File "c:\python\chapter08\ex33디렉토리관리.py", line 39, in <module>
    os.rmdir('images')   #삭제
FileNotFoundError: [WinError 2] 지정된 파일을 찾을 수 없습니다: 'images'

이미 삭제해서 없는데, 한번 더 실행하니 없어서 에러. 
'''

# ------------------------------
# os.mkdir('images/dog')
'''
dog를 생성해야하는데 경로인  images가 없어서 에러.
(base) C:\python\chapter08>python -u "c:\python\chapter08\ex33디렉토리관리.py"
C:\python
Traceback (most recent call last):
  File "c:\python\chapter08\ex33디렉토리관리.py", line 63, in <module>
    os.mkdir('images/dog')
FileNotFoundError: [WinError 3] 지정된 경로를 찾을 수 없습니다: 'images/dog'

'''
# ------------------------------
# 먼저 상위디렉토리 images를 만들고 하위인 서브디렉토리를 생성 : top-down방식으로 하나씩 만들어야함

os.mkdir('images')
os.mkdir('images/dog')
os.mkdir('images/cat')
'''
Traceback (most recent call last):
  File "c:\python\chapter08\ex33디렉토리관리.py", line 77, in <module>
    os.mkdir('images')
FileExistsError: [WinError 183] 파일이 이미 있으므로 만들 수 없습니다: 'images'
'''
# os.rmdir('images') # 디렉토리가 비어있지 않다면 지울 수 없다. rmdir은 바텀업방식으로 디렉토리를 전부 비우고 삭제해야함. -> 번거로움
'''
(base) C:\python\chapter08>python -u "c:\python\chapter08\ex33디렉토리관리.py"
C:\python
Traceback (most recent call last):
  File "c:\python\chapter08\ex33디렉토리관리.py", line 86, in <module>
    os.rmdir('images')
OSError: [WinError 145] 디렉터리가 비어 있지 않습니다: 'images'
'''

# 내용물까지 포함해서 디렉터리를 삭제하고 싶다면 shutil.rmtree(path) 이용.
shutil.rmtree('images')
# 전부 삭제시키기때문에 조심해서 사용해야한다!!