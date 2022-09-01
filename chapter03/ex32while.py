from re import I


n = int(input('합계를 구할 수를 입력하세요 : '))
total=0
i=1
while i<=n: # i는 1~n까지 
    total += i 
    i += 1
print(f'1부터 {n}까지의 합은 {total}')

# 해당 코드는 for문에 더 적합.

# while 언제 끝날지 모를때 주로 쓰임
# while True : 
#    if( ):
#       break
# 무한루프의 기본 골격.