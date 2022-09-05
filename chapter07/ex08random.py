# random모듈 - 매개변수로 리스트를 받음

# shuffle(list) list를 랜덤하게 섞음
# choisce(list) list에서 랜덤하게 하나 고름
# sample(list, n) list에서 랜덤하게 n 개 고름

'''
>>> numlist = [10,20,30,40,50]
>>> rd.shuffle(numlist)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'rd' is not defined
>>> import random
>>> import random as rd
>>> numlist = [10,20,30,40,50]
>>> rd.shuffle(numlist)
>>> numlist
[10, 50, 30, 20, 40]
>>> rd.choice(numlist)
40
>>> rd.sample(numlist, 3)
[40, 20, 30]
'''