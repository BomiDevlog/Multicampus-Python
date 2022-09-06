# 에러 - 복구 불가 (하드웨어 이상 등)
# 예외 - 복구 가능 (소프트웨어 이상 등 )
# 예외처리 - 프로그램 안정성에 매우 중요한 작업

# try~except 
try:
    a, b = input('두 수를 입력하시오. : ').split()
    result = int(a) / int (b)
    print(f'{a}/{b}={result}')
    # print('{}/{}={}'.format(a,b,reult))
except:
    print('수가 정확한지 확인하세요.')

'''
*try~except 작성하기 전. 

(base) C:\python\chapter07_2>python -u "c:\python\chapter08\ex01try_except.py"
두 수를 입력하시오: 2 2
2/2=1.0


(base) C:\python\chapter07_2>python -u "c:\python\chapter08\ex01try_except.py"
두 수를 입력하시오: 2
Traceback (most recent call last):
  File "c:\python\chapter08\ex01try_except.py", line 7, in <module>
    a, b = input('두 수를 입력하시오: ').split()
ValueError: not enough values to unpack (expected 2, got 1)

(base) C:\python\chapter07_2>python -u "c:\python\chapter08\ex01try_except.py"
두 수를 입력하시오: 사백 이백
Traceback (most recent call last):
  File "c:\python\chapter08\ex01try_except.py", line 8, in <module>
    result = int(a) / int (b)
ValueError: invalid literal for int() with base 10: '사백'
'''

'''
*try~except 작성 후.
(base) C:\python>python -u "c:\python\chapter08\ex01try_except.py"
두 수를 입력하시오. : 이백 사백
수가 정확한지 확인하세요.

(base) C:\python>python -u "c:\python\chapter08\ex01try_except.py"
두 수를 입력하시오. : 5
수가 정확한지 확인하세요.

(base) C:\python>python -u "c:\python\chapter08\ex01try_except.py"
두 수를 입력하시오. : 5 2
5/2=2.5

'''