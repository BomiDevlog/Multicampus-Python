def sum_nums(*numbers):
    print(len(numbers), type(numbers), numbers)
    # 1 <class 'tuple'> ([-1, 10, 40, 35, 80],)
    # 튜플 속에 리스트가 첫번째 요소 하나로 들어간 형태
    # 5 <class 'tuple'> (-1, 10, 40, 35, 80)
    # 리스트가 펼쳐졌기 때문에, 튜플에 각각 5개의 element로 개별적으로 들어간 형태.
    result = 0
    for n in numbers:
        result += n
    return result

# print(sum_nums(10, 20, 30)) # 10, 20, 30 인자들의 합을 출력
# print(sum_nums(10, 20, 30, 40, 50)) # 10, 20, 30, 40, 50 인자들의 합을 출력

# numbers가 값으로 넘어가는게 아니라 리스트나 튜플이 값으로 넘어가는 것..

# positional args로 가변인수를 받으면 tuple로 전달된다.
n_list = [-1, 10, 40, 35, 80]
# sum_nums(n_list)
# TypeError: unsupported operand type(s) for +=: 'int' and 'list'  
# 인트와 리스트를 연산할 수 없다. 라는 내용의 에러.
sum_nums(*n_list)
# 리스트앞에 *붙이면 펼침연산자가 된다
# JS : arr = [...arr1, ... arr2] 자바스크립트의 스페드연산자와 같은 기능.

print(n_list)
print(*n_list)

n_list2 = [*n_list, 45 , 66]
print(n_list2)