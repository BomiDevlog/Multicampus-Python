list = [ 13, 25, 67, 30, 46, 84, 95 ]
print(list)
print(list[3])
# 변수명으로 list를 사용해서
# list() 변환함수가 작동하지 않고 변수로 작동해서 에러.
print(list('abcd'))
'''
Traceback (most recent call last):
  File "c:\python\chapter05\ex02list.py", line 6, in <module>
    print(list('abcd'))
TypeError: 'list' object is not callable
'''