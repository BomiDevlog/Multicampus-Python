# 리스트를 매개변수로 전달 받는 함수
# min() 최솟값 -값을 리턴
# max() 최댓값 -값을 리턴
# sum() 합계 -값을 리턴
# len() 리스트 내 항목의 개수를 반환

# >>> list1 = [20, 10, 40, 50, 30]
# >>> min(list1) # 리스트의 원소들 중 가장 작은 원소를 구한다.
# 10
# >>> max(list1) # 리스트의 원소들 중 가장 큰 원소를 구한다.
# 50
# >>> sum(list1) # 리스트내의 원소의 합을 구한다.
# 150

# ----------------------------------
# primitive : int, float, bool, None
# reference : 나머지

# 파이썬에서 primitive는 매개변수 전달시 call by value
# reference는 call by reference -> 함수 내에서 원본을 수정할 수 있다.


# c++의 경우 pointer로 인해 복잡함...
# 매개변수로 전달 시 
# call by Value 값의 복사 -> 원본수정 x
# call by reference  주소가 전달 -> 원본 수정 가능.