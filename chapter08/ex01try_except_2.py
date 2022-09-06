# 에러 - 복구 불가 (하드웨어 이상 등)
# 예외 - 복구 가능 (소프트웨어 이상 등 )
# 예외처리 - 프로그램 안정성에 매우 중요한 작업

# try~except 
try:
    a, b = input('두 수를 입력하시오. : ').split()
    result = int(a) / int (b)
    print(f'{a}/{b}={result}')
    # print('{}/{}={}'.format(a,b,reult))
except Exception as e:
    print('error: ', e)

# 영어, 개발자에게 주는 메시지 -> 소비자에게 보여주기에 적합하지않음.

'''
(base) C:\python>python -u "c:\python\chapter08\ex01try_except_2.py"
두 수를 입력하시오. : 10 0
error:  division by zero

(base) C:\python>python -u "c:\python\chapter08\ex01try_except_2.py"
두 수를 입력하시오. : 5
error:  not enough values to unpack (expected 2, got 1)

(base) C:\python>python -u "c:\python\chapter08\ex01try_except_2.py"
두 수를 입력하시오. : 이백 사백
error:  invalid literal for int() with base 10: '이백'

(base) C:\python>python -u "c:\python\chapter08\ex01try_except_2.py"
두 수를 입력하시오. : 0x12 010
error:  invalid literal for int() with base 10: '0x12'

(base) C:\python>python -u "c:\python\chapter08\ex01try_except_2.py"
두 수를 입력하시오. : 8 2
8/2=4.0
'''