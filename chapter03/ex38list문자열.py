# 문자열은 문자로 구성된 콜렉션
# 단위 데이터는 글자하나하나.
# 문자열도 순서가 있는 자료(Sequence) -> 그래서 list변환 가능

for ch in 'Hello':
    print(ch, end = ' ')

# 문자열이 콜렉션이 for문에 올수 있고, 글자하나하나의 단위로 진행됨.

# >>> st='Hello'
# >>> list(st)
# ['H', 'e', 'l', 'l', 'o']