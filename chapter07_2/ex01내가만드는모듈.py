# 내가 만드는 모듈
# 모듈의 정의 (util.py)
# -> 모듈의 사용

import ex01util

print('util.py')
print('module name:', __name__)

print("1inch = ", ex01util.INCH)
print("~10 = ", ex01util.calcsum(10))


# 정의파일을 저장하지않았다면 에러남 저장확인!

# 단독으로 쓸 때는 모듈이라고 부르지않음.
# 다른 곳에서 가져다가 쓰는 파일 -> 모듈이 됨.
'''
ex01util.py실행
util.py
module name: __main__ (단독실행)

ex01내가만드는모듈.py실행
util.py
module name: ex01util (모듈로 실행되면 파일명 = 다른 곳에서 import로 부른 것.)
util.py
module name: __main__
1inch =  2.54
~10 =  55
'''

