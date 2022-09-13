# file 관리 함수

'''
# 파이썬의 표준모듈

shell : utility의 일종. cmi명령창을 shell이라고 부름. 
        커맨드 기반의 유저인터페이스.(sh util 줄여서 shell)

a,b 파일경로 문자열임

*shutil모듈 : import shutil해서 사용
shutil.copy(a, b) 복사 
shutil.move(a, b) 이동
shutil.rmtree(path) 디렉토리를 제거(즉 서브디렉토리까지 전부 제거)
shutil.chown(f, u, g) 바꾸어라

*os 모듈 : import os해서 사용
os.rename(a, b) 이름바꾸기
os.remove(f) 파일 하나를 삭제
아래 세개는 리눅스에서 사용. 윈도우즈에서 사용x
os.chmod(f, m)  권한바꾸기
os.link(a, b) 
os.symlink(a, b)
'''

# shutil.rmtree(path)는 shell util 프로그램의 remove tree 명령어로 경로 상의 파일을 제거하는 것이고, 
# os.remove(f)는 os 즉 운영체제에서 윈도우즈의 cmd 명령어 remove로 (f)상의 file 즉 해당 파일을 삭제하게 하는 것입니다.
# 참고로 shutil.rmtree(path)는 지정한 디렉터리와 하위 디렉터리 및 파일 등을 모두 지정해서 함께 삭제할 수 있습니다.


import shutil
import os

# 파일 복사
shutil.copy("live.txt", "live2.txt")

# 파일 삭제
answer = input("live2.txt를 삭제할까요? [y]/n").lower() #소문자변환을 통해 Y, N도 인식가능. #대문자변환은 upper()
# lower()

# [y]는 디폴트값이라 엔터쳐도 해당된다는 명명 관례.
# y누르고 엔터, n누르고 엔터해서 이동 y/n, n/n-> input이 자동으로 개행무자를제거함
# 엔터만 치면 비여있는 문자열이 전달됨!!
'''
answer.lower() #적용이 안됨.
print(answer.lower()) # 동작확인 
print(answer) # 그러나 lower()호출해도 answer변화 없음.
#파이썬의 str은 불변객체이기에 내용을 못바꿈 -> 원본을 바꾸는게 아니라 복사본을 바꿔서. 
answer = answer.lower() # 다시 대입해주어야 원본이 변화됨

중요! 파이썬 문자열은 불변객체(내용 수정 불가)
자바, 자바스크립트, 파이썬 등 대부분 언어에서 문자열은 불변객체라서 원본조작이 불가하고 새로운 복사본을 생성함
새로운 대입으로 원본 변화됨

c++은 예외적으로 문자열이 불변객체가 아니다.
'''

if answer == 'y' or answer == ''  : # y입력 또는 엔터입력
        os.remove('live2.txt')

'''
틀렸던거...
if answer == 'y' | answer == '/n' :


Traceback (most recent call last):
  File "c:\python\chapter08\ex32shutil.py", line 34, in <module>
    if answer == 'y' | answer == '/n' :
TypeError: unsupported operand type(s) for |: 'str' and 'str'

'''