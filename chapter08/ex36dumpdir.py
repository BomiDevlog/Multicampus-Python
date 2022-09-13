'''
dir의 경우, 한개 레벨에 대해 목록 출력

디렉토리를 제시하면 서브디렉토리의 내용까지 포함하여 파일의 목록을 보여주는 함수 생성
'''

import os

def dumpdir(path): # path : 디렉토리경로 
    files = os.listdir(path)
    for f in files: # f가 파일인지 디렉토리인지에 따라 다른 결과
        fullpath = os.path.join(path, f)
        if os.path.isdir(fullpath): # 디렉토리일 경우 다시 dumpdir 호출
            print("[%s]"%fullpath)
            dumpdir(fullpath) 
            #디렉토리라면 다시 실행하여 서브디렉토리를 열어서 검사함 => 재귀호출(자기자신을 호출한다)
        else:
            print("\t"+f) # 파일일 경우 파일명만 나열
        
dumpdir(".") # 현재 디렉토리

'''
images디렉토리에 a가 존재한다면
f가 a에 해당하고
join을 통해 fullpath = 'images/a'
조건문에서 a가 파일인지 디렉토리인지 검사

'''