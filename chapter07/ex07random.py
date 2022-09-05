# random()함수

'''
>>> import random as rd
>>> rd.random() # 0 이상 1 미만의 실수를 반환함
0.19452357419514088
>>> rd.random() # 매번 다른 실수를 반환함
0.6947454047320903

# int 정수값만 가지고 싶을 경우 randrange
>>> rd.randrange(1, 7) # 1 이상 7 미만의 정수를 반환함
6
# 주사위값 1~6

>>> rd.randrange(0, 10, 2) # 1 이상 10 미만 정수 중 2의 배수를 반환함
2

>>> rd.randint(1, 10) # 1 이상 10 이하의(1, 10이 포함) 임의의 정수를 반환함
3
# randint는 10이 포함!!!
'''

# 0~100사이의 랜덤한 실수 : random*100하면 된당