# try예외발생하면 -> except
# 예외발생하지않으면 else

try : 
    a, b = input('두 수를 입력하시오 : ').split()
    result = int(a) / int(b)
except ZeroDivisionError :
    print('오류 : 0으로 나눔을 시도했습니다.')
except ValueError :
    print('오류: 입력 값이 정수나 실수가 아닙니다.')
except :
    print('오류 : 10 2 와 같이 두 정수를 입력하세요')
else:
    print(f'{a} / {b} = {result}')