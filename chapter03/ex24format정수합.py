# 임의의 양의 정수를 입력받아 1~n까지의 정수 출력
n= int(input('합계를 구할 수 를 입력하세요 : '))
total = 0

for i in range(n):
    total = total + (i+1) 
print (f'1부터 {n}까지의 합은 {total}')

# for i in range(n+1):
#     total = total + i
# print (f'1부터 {n}까지의 합은 {total}')
# 같은 표현. range를 n까지 포함시키기위해 +1해준 것.

# 클래스명과 같은 이름의 형변환 함수
# int -> int()
# float -> float()
# str -> str()
# bool -> bool()