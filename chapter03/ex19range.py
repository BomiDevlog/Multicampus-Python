# for in range 표현식1
for i in range(5):
    print(i, end = ' ')

# for in range 표현식2
for i in range(0,5):
    print(i, end = ' ')
    

# 파이썬의 경우 print가 줄바꿈포함. 디폴트로 출력 끝에 '\n'포함
# print(i, end = ' ') // 출력 끝 문자를 변경함 -> 줄바꿈없음
# *공백: 스페이스(띄어쓰기) *개행: 줄바꿈, 엔터, 리턴

print(' ')  #줄바꿈

print(1, 2, 3, 4, 5)
# 데이터와 데이터의 구분이 스페이스(공백)으로 이루어짐. 1 2 3 4 5

print(1, 2, 3, 4, 5, sep=', ') # sep: , 로 데이터 구분

print(1, 2, 3, 4, 5, sep=', ', end='==>')  # end: 마지막 데이터 표시