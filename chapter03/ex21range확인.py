# 표현식 1 : 2에서 5-1까지 연속값 2, 3, 4 출력
for i in range(2, 5):
    print(i, end = ' ')
print() #줄바꿈

# 표현식 2 : 간격 값을 사용하여 0, 2, 4, 6, 8 출력
for i in range(0, 10, 2):
    print(i, end = ' ')
print()

# 표현식 3 : 음수 간격 값 사용, -2, -4, -6, -8 출력
for i in range(-2, -10, -2):
    print(i, end = ' ')

# python 대화모드에서 eliment를 간단히 보고싶으면 list형변환하면 됨
# >>> list(range(5))
# [0, 1, 2, 3, 4]
# file에서 하면 print함수호출함. 작업량 많아지니깐.

# range(5) = range(0, 5) =  range(0, 5, 1)
# list(range(0,10,2)) // 0~9사이 짝수 리스트
# list(range(1,10,2)) // 0~9사이 홀수 리스트
# list(range(-2,-10,-2)) // 음수의 경우