# 반환 return 

def get_sum(a,b):
    result = a+b
    return result #return문이 없으면 None. 값을 알 수 없기 때문.

n1= get_sum(10,20)
print('10과 20의 합 =', n1 )

n2= get_sum(100,200)
print('100과 200의 합 =',n2)

print('======================')

def print_sum(a,b):
    result = a+b
    print(a, '과', b, '의 합은', result, '입니다') # 출력문은 변수로 반환하지 않아도 함수 호출 때 잘 동작함.

print_sum(5, 12)
print_sum(200,500)