# 소수 구하기. 중첩 for문

for n in range(2,101):  
    # n은 2~100까지의 정수. 임의로 n을 소수로 가정
    is_prime = True
    for num in range(2,n):     # 2~ (n-1)사이의 수 num에 대해
        if n % num == 0 :      # 이 수 중에서 n 의 약수가 있으면
            is_prime = False   # 소수가 아님
    if is_prime:               #조건식으로 is_prime이 True일 경우. 즉 소수라면 출력
        print(n, end=', ')