# 1~10까지 정수의 합

total=0
for i in range(1,11):
    total += i
    # total = total + i
print('1~10까지의 합:', total) 

# 1~10까지 정수 중 홀수 짝수의 합

total1=0
for i in range(1,11,2):
    total1 += i
print('1~10까지의 홀수의 합:', total1) 

total2=0
for i in range(2,11,2):
    total2 += i
print('1~10까지의 짝수의 합:', total2) 