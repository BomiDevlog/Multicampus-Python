numbers = [ 13, 25, 67, 30, 46, 84, 95, 62, 21, 89, 97 ] #전역변수
numbers2 = [23, 5, 7, 6, 89, 99, 51, 60, 77]

# 리스트의 요소 중 짝수의 값만 찾는 함수를 생성

even_list = []

def find_evens():
    for n in numbers:
        if n % 2 == 0: #짝수 검사
            even_list.append(n)
find_evens() # 짝수를 even_list에 추가
print(even_list) # even_list 출력

# 그러나 함수의 재사용 측면에서 전역변수로 인해 범용성이 떨어짐
# numbers 대신 매개변수로 받아주고, even_list는 빈 리스트이니 지역변수로 만들어 주면 됨.

def find_odds(numbers) : #numbers매개변수는 지역변수
    odd_list = [] # 지역변수
    for n in numbers:
        if n%2 == 1: # 홀수 검사
            odd_list.append(n)
    
    return odd_list

odd_list = find_odds(numbers) #numbers는 전역변수 # odd_list 전역변수
print(odd_list)


# 매개변수로 전달하면 일반화된 함수로 구성함. 어떤 리스트든 처리가능함.
odd_list = find_odds(numbers2)
print(odd_list)