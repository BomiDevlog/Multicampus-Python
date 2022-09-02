
numbers = [26, 13, 45, 82, 55, 77, 88, 90, 54, 69]

#아래와 같이 출력해보세요.
# [26, 13, 45, 82, 55, 77, 88, 90, 54, 69]
# [13, 45, 82, 55, 77, 88, 90, 54, 69]
# [45, 82, 55, 77, 88, 90, 54, 69]
#  ...
# [54, 69]
# [69]

end = len(numbers)

# 카드 정렬 알고리즘 : 섞여있는 카드를 하나씩 옆으로 옮기는 것처럼.
# 최대값을 찾아 왼쪽 끝으로 옮겨 리스트를 내림차순 정렬시킴
# 알고리즘 중에서 가장 쉽고. 성능이 안좋은ㅋ 알고리즘.

for i in range(end) :
    # 알고리즘 과정 확인해보기
    print(numbers[:i], numbers[i:]) #처음부터 i까지, i부터 끝까지
    # 왼쪽은 최소값을 정렬해가고, 오른쪽은 원래리스트에서 최소값을 찾아 하나씩 빠짐.

    # print(numbers[i:])
    # numbers[i:]에서 최대값과 인덱스를 찾으세요
    max_v=max(numbers[i:])
    max_ix=numbers[i:].index(max_v) + i  # 원본 리스트에서의 index는 i만큼 더해주면 된다.
    # print(max_v, max_ix)
    
    # numbers[i]와 numbers[max_ix]의 값을 교환하세요 
    numbers[i], numbers[max_ix] = numbers[max_ix], numbers[i]

print(numbers)
# 원본이 변경됨. 내림차순 정렬