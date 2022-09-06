for i in range(5):
    print(i)
else: # for루프를 5번 정상실행하면 실행되는 구문
    print('정상루프 실행1')

# -------------

for i in range(5):
    print(i)
    if i == 3:
        break
else: # for루프를 5번 정상실행하면 실행되는 구문
    print('정상루프 실행2')
    # break로 인해 루프가 완전하지 않아서 실행안됨.


# 로그인할 때 최대 3번 할 때 같은 조건이었다.
# 적용해보면 루프를 다 돌았다면 로그인 실패. 
# for문에 else를 붙여서 로그인 확인 과정.

# try에서는 try구문을 다했으면 else실행
# for에서는 for구문을 다 했으면 else실행
# if에서는 if가 아니라면 다른 조건.else.