numbers = [ 25, 67, 30, 46, 84, 95, 62, 21, 13, 89, 97 ]

# 최솟값을 찾아서 인덱스를 리턴하는  find_min()함수 작성

def find_min(numbers) :
    # numbers에서 최소값을 찾아 그 인덱스를 리턴

    # 검사 전 첫번째 eliment를 최소값으로 간주
    min_value = numbers[0] 
    min_index = 0

    for ix, n in enumerate(numbers):  # 반복문을 돌면서 값을 비교
        if n < min_value :  # 새로운 최소값이라면 
            min_value = n   # 값 교체
            min_index = ix

    return min_index        # 함수블럭의 들여쓰기 중요!

print(numbers)  # 원본 리스트 출력
min_index = find_min(numbers) # 함수 호출해 최솟값 찾기
print(min_index, numbers[min_index]) # 최솟값 : 8번째 인덱스의 항목 13

# ---------최댓값으로도 적용

def find_max(numbers) :
    # numbers에서 최댓값을 찾아 그 인덱스를 리턴

    # 검사 전 첫번째 eliment를 최댓값으로 간주
    max_value = numbers[0] 
    max_index = 0

    for ix, n in enumerate(numbers):  
        if n > max_value :  
            max_value = n   # 값 교체
            max_index = ix

    return max_index        

max_index = find_max(numbers) # 함수 호출해 최대값 찾기
print(max_index, numbers[max_index]) # 최대값 : 10번째 인덱스의 항목 97