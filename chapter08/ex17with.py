# with 문법 : with ~ as문

# f= open('hello.txt', 'w') # 파일 열기
# open 성공하면 변수 f에 배정됨
with open('hello.txt', 'w') as f:
    f.write('Hello world!')
    # with 코드블럭을 벗어날 때 close() 자동 호출
# open 실패하면 다음으로 넘어감


'''
java의 경우
try() {

}

try with resource

'''