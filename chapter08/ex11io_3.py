# io 예외 처리

try:
    f = open('hello2.txt','rb')    # 1. 파일이 존재하지 않는 경우 예외발생
    # 바이너리는 텍스트 아니라서 인코딩 적을 수 없음
    s = f.read()                  # 2. 파일열었지만 읽기중에 파일이 사라지면 예외 발생 (usb 파일 읽는 도중에 갑자기 usb연결해제 등)
    print(type(s))   #<class 'bytes'>
    print(s)                      # 3. 닫기 중 예외 발생 등등
    f.close()   
except Exception as e:
    print(e)

'''
(base) C:\python>python -u "c:\python\chapter08\ex11io_2.py"
'cp949' codec can't decode byte 0xec in position 0: illegal multibyte sequence
# hello2에 한글로 적혀있어서 인코딩 문제로 예외발생
'''