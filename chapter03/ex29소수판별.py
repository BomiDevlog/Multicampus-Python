# 소수 (prime number) 판별. 단일 for문

n = int(input('수를 입력하세요 : '))

is_prime = True
for num in range(2, n):     # 2부터 (n-1) 사이의 수 num에 대하여
    if n % num == 0:        # 이 수 중에서 n의 약수가 있으면
        is_prime = False    # 소수가 아님
        break
print(n, 'is prime : ', is_prime)

# 중간에 소수가 아니라고 판단했음에도 계속 loop를 돈다. ->break로 반복문 벗어남