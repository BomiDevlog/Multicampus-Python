# 1에서 100까지의 합을 구하다가, 합계가 50보다 크면 계산 중단하기
total = 0;
for i in range(1, 101) :
    total+=i
    if total>50:
        print(f'계산 중단, i={i}, total={total}')
        break
    # break를 만나면 그 즉시 반복 실행을 종료하고 루프를 빠져나옴


# 1에서 100까지의 수 중 홀수의 합 구하기
total2=0
for j in range(1,101):
    if j%2 == 0: # 짝수이면 continue
        continue
    total2 += j
print(f'홀수의 합: {total2}')

# 루프를 빠져나오지 않고 continue 아래의 문장만을 건너뛰는 역할