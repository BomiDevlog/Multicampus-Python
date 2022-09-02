# swap

a=100
b=200
print('swap 이전: a= ',a, 'b= ',b)

a,b=b,a # 튜플의 패킹, 언패킹을 이용한 swap
print('튜플을 사용한 swap 결과: a= ',a, 'b= ',b)

# 별도의 임시변수가 필요 없이 바로 swap 가능

# ----------------
numbers = [26, 13, 45, 82, 55, 77, 88, 90, 54, 69]

#아래와 같이 출력해보세요.
# [26, 13, 45, 82, 55, 77, 88, 90, 54, 69]
# [13, 45, 82, 55, 77, 88, 90, 54, 69]
# [45, 82, 55, 77, 88, 90, 54, 69]
#  ...
# [54, 69]
# [69]

end = len(numbers)

# algorithm
# 카드 정렬 알고리즘 : 섞여있는 카드를 하나씩 옆으로 옮기는 것처럼.
# 최소값을 찾아 왼쪽 끝으로 옮겨 리스트를 오름차순 정렬시킴

for i in range(end) :
    # 알고리즘 과정 확인해보기
    print(numbers[:i], numbers[i:]) #처음부터 i까지, i부터 끝까지
    # 왼쪽은 최소값을 정렬해가고, 오른쪽은 원래리스트에서 최소값을 찾아 하나씩 빠짐.

    # print(numbers[i:])
    # numbers[i:]에서 최소값과 인덱스를 찾으세요
    min_v=min(numbers[i:])
    # min_ix=numbers[i:].index(min_v) # numbers[i:]에서의 인덱스번호
    min_ix=numbers[i:].index(min_v) + i  # 원본 리스트에서의 index는 i만큼 더해주면 된다.
    # print(min_v, min_ix)
    
    # numbers[i]와 numbers[min_ix]의 값을 교환하세요 
    numbers[i], numbers[min_ix] = numbers[min_ix], numbers[i]

# 합계와 평균을 구하는 함수
def calc(numbers):
    size = len(numbers)
    total = sum(numbers)
    average = total/size

    return total, average # 튜플 리턴. 괄호가 생략된 것.


print(numbers)
# 원본이 변경됨. 오름차순 정렬

# "합계: xxx, 평균: xxx" 을 출력하세요
total, average = calc(numbers) # 튜플 이용 : unpacking # 데이터 분석에서 이러한 형태를 보면 튜플을 리턴하고 언팩하는구나. 리턴타입으로 1개튜플에서 2개의 값이 나오는구나라고 해석할줄 알아야함 
print(f'합계: {total}, 평균: {average}')