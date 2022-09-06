# 파일 읽기 : read()

f = open('hello.txt','r')   # 1. 파일을 연다 # "rt"
s = f.read()                # 2. hello.txt 파일 전체를 읽어서 리턴한다
print(s)                    # 3. 파일의 내용을 출력한다
f.close()                   # 4. 파일을 닫는다

# 파일이 존재하지 않는 경우 FileNotFoundError -> 예외 처리
try:
    f = open('hello1.txt','r')    # 1. 파일이 존재하지 않는 경우 예외발생
    s = f.read()                  # 2. 파일열었지만 읽기중에 파일이 사라지면 예외 발생 (usb 파일 읽는 도중에 갑자기 usb연결해제 등)
    print(s)                      # 3. 닫기 중 예외 발생 등등
    f.close()   
except :
    print('파일이 없습니다')