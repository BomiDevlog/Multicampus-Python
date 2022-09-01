n = 5
for i in range(n) :
    for j in range(n - (i+1)):
        print(' ', end='')  # 공백 출력
    for j in range(2*i +1):
        print('+', end='')  # +출력
    print()                 #줄 바꿈