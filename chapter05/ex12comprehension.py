# comprehension 컴프리헨션 : 리스트 요소의 값 조작을 수행하는 단축 표현
# 영어의미는 이해, 이해력/ 포함 

# 새로운 리스트 = [ x가공식 for x in 리스트 ]

# 리스트 리터럴 내에 for문을 넣고, 가공식을 앞에 넣음 
# 원본 리스트가 가공된 결과가 새로운 리스트에 담김

# 새로운 리스트 = [ x가공식 for x in 리스트 if x조건식]
# x에 대해 조건검사하여 True만 x가공식을 거쳐 리스트에 담김. False는 버림.

list1= [10, 20, 30, 40, 50]
list1 = [n*10 for n in list1]
print(list1)

list1= [n+5 for n in list1 if n<=300]
print(list1)

# ------------------------------------------------
numbers = [ 13, 25, -67, 30, 46, -84, 95, 62, 21, 89, 97 ]
# numbers의 데이터에서 홀수를 찾아 새로운 리스트를 만드세요

numbers = [n for n in numbers if n >= 0] # 음수 제거
print(numbers)

# odd_list = [n for n in numbers] #이렇게만하면 카피본 생성

odd_list = [n for n in numbers if n % 2 == 1]  # 홀수 검사
print(odd_list)

 # filter (내가 원하지 않는 데이터를 걸러냄). 이 코드에서 if가 필터 역할.