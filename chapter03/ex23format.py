# 1~10까지 정수의 합
# 중간 결과 출력을 위한 포맷팅

total=0
for i in range(1,11):
    total += i
    print('i = {}, total = {}'.format(i,total))
print('1~10까지의 합:', total) 

# c++의 printf와 같은 기능
# 대체문자{}

total2 = 0
for j in range(1, 11):
    total2 += j
    print(f'j = {j}, total2 = {total2}')
print('1에서 10까지의 합:', total2)

# JS의 `${a}=${b}` 변수a의 기능을 여기에 넣어라 (템플릿 문자열)
# f'i={i} 변수를 중괄호에 넣어주면 변수의 값이 출력된다. (포맷팅 문자열) 