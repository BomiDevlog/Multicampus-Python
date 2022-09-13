'''
사용자로부터 파일 이름을 받아들인 후  (input)
파일의 내용을 라인 번호와 함께
출력하는 기능을 파일 입출력을 통해서 구현하기
'''
# 존재여부를 확인하는 작업 추가
import os
import sys

fname = input('입력할 파일의 이름 : ') # 파일 열기
if not os.path.exists(fname):
  print(fname, '이 존재하지 않습니다.')
  sys.exit(0)
  # 파일이 존재하지 않는다면 더이상 진행하지 않고, 프로그램종료

f = open(fname, 'r')

n = 1                   # 줄 번호를 출력하기 위한 변수
l = f.readline()
while l:                # 읽을 줄이 있으면 반복 수행
    print('{:3d}: {}'.format(n,l), end = '') # 줄번호와 내용 출력
    n += 1              # 줄 번호 증가
    l = f.readline()    # 다음 줄 읽어온다

f.close()

'''
(base) C:\python\chapter08>python -u "c:\python\chapter08\ex16file_read2.py"
입력할 파일의 이름 : we_will_rock.txt
  1: Buddy, you're a boy, make a big noise
  2: Playing in the street, gonna be a big man someday
  3: You got mud on your face, you big disgrace
  4: Kicking your can all over the place, singin'
  5: We will, we will rock you
  6: We will, we will rock you
(base) C:\python\chapter08>
'''

'''
[    ]
     ^ 파일의 끝에서 readline하면 ''(비어있는 문자열) => False이니 while문 반복종료. 
'''