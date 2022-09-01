n=7

# 외부 for루프는 n 번 수행, i는 0,1,2,3,4,5,6까지 증가
for i in range(n):
    st=''
    for j in range (i): # 내부 for루프는 i번 수행
        st = st+ ' '    # 공백을 i개 추가
    print(st+'#')       # 공백 추가 후 '#'출력

# 행번호와 공백의 수가 일치하는 형태.

for i in range(n):
    st=''
    for j in range (i):
        st= st+'*'
    print(st)