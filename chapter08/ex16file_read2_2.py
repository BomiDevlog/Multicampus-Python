'''
사용자로부터 파일 이름을 받아들인 후  (input)
파일의 내용을 라인 번호와 함께
출력하는 기능을 파일 입출력을 통해서 구현하기
'''

fname = input('입력할 파일의 이름 : ') # 파일 열기

f = open(fname, 'r')
n = 1                   # 줄 번호를 출력하기 위한 변수
l = f.readline()
while l:                # 읽을 줄이 있으면 반복 수행
    print('{:3d}: {}'.format(n,l), end = '') # 줄번호와 내용 출력 # 개행문자가 있어서 개행문자 제거하려고  end = ''
    n += 1              # 줄 번호 증가
    l = f.readline()    # 다음 줄 읽어온다

f.close()

print('\n----------------------------') # 줄바꿈하고 --- 출력


# read_file_lines()를 사용해서 처리

from file_util import read_file_lines

data = read_file_lines(fname)

for n, l in enumerate(data, 1): # enumerate. 시작번호 1부터 (디폴트 0)
    print(f'{n:3d}: {l}') # 이미 개행문자 제거됨

