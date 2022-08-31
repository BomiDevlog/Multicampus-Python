age = 18
# age = 25

if age < 20: # 조건식 true
    print('나이', age)
    print('청소년 할인')
    print('1000원 할인')
print('방문을 환영합니다')
# if문이 아닌 독립적인 문장. false여도 실행.

'''
  File "c:\python\chapter03\ex01if.py", line 5
    print('1000원 할인')
                           ^
IndentationError: unindent does not match any outer indentation level
들여쓰기 안맞추면 생기는 에러
'''

# 다른언어에서 if(){}
#  {}로 시작과 끝을 알려주었는데.
# 
# 파이썬은 중괄호 없음.()있어도 되고 없어도 됨.
# if 조건식 : (콜론)
# (들여쓰기)실행문
# 들여쓰기로 시작과 끝을 표현 (마치 {}처럼.). 중요한 문법!
# 2개든 3개든 4개든. 들여쓰기의 스페이스 개수가 일치해야함.

# :콜론 뒤에 들여쓰기 되는 부분을 코드블럭 이라고 한다.
# 같은 코드블럭에서는 들여쓰기가 일치해야한다.