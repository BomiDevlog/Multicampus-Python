# 튜플 () : 수정 불가능. 읽기전용리스트

# 지원o : index(x) count(x)
# 지원x : append(x) insert(index, x) remove(x)  pop(index) 

# 하나의 요소를 가진 튜플은 반드시 쉼표를 사용해야함 
# (1), (-1)은 그저 괄호 연산자. 튜플 아님

# 괄호 생략하고 데이터 나열해서 표현 가능.

# a, b = 100, 200 
# for ix, value in enumerate(list) 
# 튜플 tuple / 값을 나열하면 튜플의 형태로 생각해라.

# tuple( ) 튜플 형변환 함수

# ------------
# >>> t= (1,2.3,4)
# >>> t[0]
# 1
# >>> t[2]
# 4
# >>> t[1]=2
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment
# 튜플은 읽기전용이기에 값 수정 안됨.
# >>> t[1:2] # slicing
# (2.3,)
# >>> t.index(1)
# 0
# >>> t.count(4)
# 1
# >>> t
# (1, 2.3, 4)

# return 값은 1개임
# return n1,n2,n3...   튜플 1개를 반환 (값 여러개 반환 x)

# ----------
# packing 하나의 변수에 여러개의 값을 넣는것. a = 3,4
# unpacking 패킹된 변수에서 여러 개의 값을 꺼내 오는 것 b, c = a
# 언패킹할 때 주의! 개수가 맞아야함. 개수가 안맞으면 예외 발생.
# >>> a=3,4
# >>> b,c=a
# >>> b
# 3
# >>> c
# 4
# >>> a
# (3, 4)

# >>> d,e,f=a
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: not enough values to unpack (expected 3, got 2)
# 개수가 안맞에서 예외발생
# >>> h=a
# >>> h
# (3, 4)

# >>> z=1,2,3,4
# >>> x,y=z
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: too many values to unpack (expected 2)
# 개수가 안맞에서 예외발생