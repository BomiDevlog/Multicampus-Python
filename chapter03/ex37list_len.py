# 누적합계, 평균
numbers = [10, 20, 30, 40, 50]

s=0
for n in numbers:
    s=s+n
print('리스트 항목 값의 합 :',s)

# 리스트의 길이 구하기 : len()
size = len(numbers)
print('리스트 항목 값의 평균 :', s/size)
# 파이썬에서 길이 관련해선 len()함수로 구한다

# len 다른 활용. 문자열 길이 구하기
name = 'Hong'
print(len(name))