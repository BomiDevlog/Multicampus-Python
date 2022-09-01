# 매개변수는 데이터타입안씀. 매개변수는 지역변수임.
# 매개변수를 마지막에 return해줌. 
# 호출할 때 매개변수를 지정해줌 이때 순서에 따라 값이 전달됨(positional argument 위치기반)
# 매개변수의 역할은. 매개변수를 통해 문제를 일반화 시킬수 있음. 어떤 문제든 적용시킬수 있게끔.

# 별표 출력을 매개변수 n 번 만큼 반복하는 프로그램
def print_star(n):
    for _ in range(n):
        print('**************')
    # 변수를 제시해야하지만 쓰이지않을 경우 _ 언더바로 지정하는 명명관례가 있다.


print_star(4)
# 매개변수의 값은 함수 호출할 때 (사용할 때) 지정


print() # 줄바꿈

# 변경해서 사용하고싶다면 변수로 지정함 
def print_pattern(n, ch):
    for _ in range(n):
        print(ch*20)
        #  문자열 * n(정수) => 문자열을 n번 반복.

print_pattern(4, '@')
print_pattern(2,'-')

# 컴파일언어는 컴파일러가 에러체크하는데, 파이썬은 빨간 밑줄은 안생김
# 매개변수의 개수를 틀린다면? (런타임에러. 작성할때가 아닌 실행할때 생기는 에러)

# print_pattern(3)
'''
Traceback (most recent call last):
  File "c:\python\chapter04\ex02파라미터.py", line 28, in <module>
    print_pattern(3)
TypeError: print_pattern() missing 1 required positional argument: 'ch'
'''

# print_star(2, '+', 9)
'''
Traceback (most recent call last):
  File "c:\python\chapter04\ex02파라미터.py", line 39, in <module>
    print_star(2, '+', 9)
TypeError: print_star() takes 1 positional argument but 3 were given
'''

# 에러난 위치를 알려주는 부분을 컨트롤 키 누르고 클릭하면 에러난 위치로 이동.