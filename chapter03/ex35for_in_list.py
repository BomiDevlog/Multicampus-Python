# for in 구문
# in 뒤에 리스트 자료형 (순서가 있는 자료 - 리스트(파이썬은 배열 없음))
#  대괄호 [ ]  리스트를 나타내는 리터럴. element를 ,로 나열.

numbers=[11, 22, 33, 44, 55, 66]

print(type(numbers))
# <class 'list'>

for n in numbers:
    print(n, end = ' ')

# int가 element
# ---------------------
print()
# 문자열이 element

summer_fruits = ['수박', '참외', '체리', '포도']

print(type(summer_fruits))
# <class 'list'>

for fruit in summer_fruits:
    print(fruit, end = ' ')

# 순서가 있는 데이터를 시퀀스데이터라고 한다(Sequence)
# 리스트는 시퀀스데이터이며, 순서대로 데이터가 나오는게 보장된다.

# index정보 얻기 : enumerate()
for ix, fruit in enumerate(summer_fruits):
    print(ix, fruit, end = ' ')

# 인덱스정보를 제공하지 않는가? 함수를 써서 인덱스번호를 알아낸다
# 콜렉션앞에 enumerate함수 -> index, element 값을 2개 반환하니 for문에 변수 2개를 제시

for ix, fruit in enumerate(summer_fruits, 100):
    print(ix, fruit, end = ' ')
    # index번호 디폴트는 0부터 시작. 시작수를 정할 수 있다
