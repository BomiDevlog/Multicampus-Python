# 파이썬 리스트
# 자바의 어레이리스트, JS의 배열, C++의 Vector와 같은 기능

# 많은 변수(항목)에 대해 1개의 변수(리스트)로 처리하기위해 생성.

# 인덱스가 있다 = 순서가 있다 (sequence)

# 리스트 요소의 데이터 타입은 달라도 됨 권장은 아님 (인터프리터 언어의 특징)
# 자바의 경우 데이터타입을 일치시킴. 

# list() 변환함수

# >>> list1 = list() # 빈 리스트 생성하기 1
# >>> list2 = [ ] 
# 아무 값도 안주면 빈 리스트 생성. 마치 디폴트 생성자.
# 두가지 표현은 동일함.


# >>> n_list = [11,22,33,44,55,66]
# >>> n_list[0] # 리스트의 첫 번째 항목의 인덱스는 0이다.
# 11
# >>> n_list[5]
# 66
# >>> n_list[6]  # 배열의 인덱스를 벗어나 에러 발생
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range 
# >>> n_list[-1] #리스트의 마지막 요소 값
# 66
# >>> n_list[-3] # 음수 인덱스. 리스트의 끝에서부터 해석.
# 44
# >>> n_list[-10] # 배열의 인덱스를 벗어나 에러 발생
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range
# >>> len(n_list) # len() # 리스트의 요소의 개수를 구하는 함수
# 6


# append() 메서드 : 기존 list의 끝에 새로운 항목을 추가
# 인스턴스.append()

# >>> list('abcde')
# ['a', 'b', 'c', 'd', 'e']
# >>> list.append('f')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: descriptor 'append' for 'list' objects doesn't apply to a 'str' object
# >>> append('f')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'append' is not defined


