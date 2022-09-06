# 파일 읽기: f.read()인자로 숫자를 주면 부분만 문자열 반환
# t-> 5글자. b->5byte

try:
    f = open('hello2.txt','r', encoding='utf-8')    
    # 인코딩 적는 것을 습관화하기
    s = f.read(3)                  #부분 읽기
    print(s)       

    s = f.read(3)                  #읽은 부분 이후의 부분을 또 읽어간다. (다시 처음x)
    print(s)           
    f.close()   
except Exception as e:
    print(e)

# 읽기/쓰기의 위치 -> OS (운영체제가 관리) : file pointer

# [                               ]
# ^0     ^5     ^10
# 처음엔 맨앞. 이후 이동한다. 이러한 정보는 OS가 관리. 내부적으로 자동으로 조정됨.

