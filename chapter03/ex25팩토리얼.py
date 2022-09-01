# 정수의 곱 : 팩토리얼 구하기
# n!=n*...*3*2*1


n=int(input('수를 입력하세요 : '))
fact =1

for i in range(1, n+1):
    fact= fact*i
print(f'{n}!={fact}')
