f= open('data5.txt', 'r') # 파일 열기 : 읽기모드
su = 0
for _ in range(5):
    n=int(f.readline()) #data5.txt파일의 한줄 내의 숫자를 읽어서 int형변환
    su += n             #su에 누적 합산

print(f'다섯 숫자의 합 = {su}, 평균 = {su/5}')  # 합과 평균 출력
f.close()   # 파일 닫기  

print('------------------------------------')

# read_file_lines()를 사용해서 처리

from asyncore import read
from file_util import read_file_lines

data = read_file_lines('data5.txt')
data = [int(n) for n in data]

total = sum(data)
average = total / len(data)
print(f'합계: {total}, 평균: {average}')