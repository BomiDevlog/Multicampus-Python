# 리스트가 제공하는 메소드
# index(x) 원소 x 를 이용해 위치를 찾는다 : 내가 원하는 데이터의  인덱스를 찾는다

# append(x) 원소 x를 리스트의 끝에 추가한다 : 리스트 끝에 데이터 추가
# insert(index, x) 원하는 index 위치에 x를 추가한다 : 리스트의 원하는 위치에 데이터 추가

# count(x) 리스트 내 object 원소의 개수를 반환한다 : 원소개수
# extend([x1, x2]) [x1, x2] 리스트를 리스트에 삽입한다 : 리스트를 매개변수로 받아서 리스트 확장

# remove(x) x원소를 리스트에서 삭제한다
# pop(index) index위치의 원소를 삭제한 후 반환한다.  
#               index는 생략될 수 있으며, 리스트의 마지막 원소를 삭제한 후 반환한다.
# sort() 값을 오름차순 순서대로 정렬한다.
# sort(reverse = True) 값을 내림차순 순서대로 정렬한다
# reverse() 리스트를원래 원소들의 역순으로 만들어준다. : 순서를 거꾸로.

# .index(값)
# >>> a_list = ['a', 'b', 'c', 'd', 'e']
# >>> a_list.index('a') # 'a' 원소의 인덱스를 반환함
# 0
# >>> a_list.index('b')
# 1
# >>> a_list.append('a') # 같은 데이터 'a'를 추가
# >>> a_list
# ['a', 'b', 'c', 'd', 'e', 'a']
# >>> a_list.index('a')
# 0                      # 리스트의 가장 앞에서 찾은 인덱스만 반환함.
# >>> a_list.index('x') # 존재하지 않는 'x' 원소의 인덱스를 조회 – 오류 발생
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: 'x' is not in list
# 그러니 인덱스 검사 전에 in으로 검사해야함

# .count(값) : 지정한 값이 몇개 있는지 계산
# >>> a_list.count('a') # 'a'가 몇 개 있는지 그 개수를 반환
# 2
# >>> a_list.count('e')
# 1
# >>> a_list.count('f') # 없는 데이터는 0개로 표시
# 0

# .extend(리스트) : 매개변수로 전달 받은 리스트의 값을 현재 리스트 끝에 추가
# >>> list1 = ['a', 'b', 'c']
# >>> list2 = [1, 2, 3]
# >>> list1.extend(list2) # list1에 list2가 더해져 확장됨
# >>> list1 # list1 확장형태로 변화
# ['a', 'b', 'c', 1, 2, 3]
# >>> list2 # list2 유지
# [1, 2, 3]
# >>> list1.extend('d') # 원소를 넣으면 추가됨
# >>> list1
# ['a', 'b', 'c', 1, 2, 3, 'd']

# + 했을 때 원본 리스트는 유지, 새로운 리스트 생성됨.
# >>> a_list
# ['a', 'b', 'c', 'd', 'e', 'a']
# >>> b_list = [1,2,3,4,5]
# >>> c_list = a_list + b_list
# >>> c_list
# ['a', 'b', 'c', 'd', 'e', 'a', 1, 2, 3, 4, 5]
# >>> a_list
# ['a', 'b', 'c', 'd', 'e', 'a']
# >>> b_list
# [1, 2, 3, 4, 5]

# append()와 extend()의 차이점
#  .insert(index, 값) :지정한 index 위치에 값을 삽입
# 기존 index 위치 이후의 값들은 한 칸 씩 뒤로 밀림
# >>> list2
# [1, 2, 3]
# >>> list2.insert(0,0)
# >>> list2
# [0, 1, 2, 3]

# .reverse() : 요소의 순서를 반대로 재배치
# >>> list2.reverse()
# >>> list2
# [3, 2, 1, 0]

# .remove(값)
# ○ 지정한 값을 리스트에서 삭제
# ○ 값이 여러 개가 있는 경우 찾은 첫 번째 값만 삭제
# ○ 지정한 값이 존재하지 않는 경우 예외 발생
# >>> list3 = ['a', 'b', 'c', 'b', 'd']
# >>> list1.remove('b') # 제일 먼저 나타나는 'b' 원소를 삭제함
# >>> list1
# ['a', 'c', 'b', 'd']
# >>> list1.remove('b') # list1에 있는 'b' 원소를 삭제함
# >>> list1
# ['a', 'c', 'd']

# ---------------------------------
# 리스트의 연산

# 리스트 * n : 리스트를 n번 반복하는 새로운 리스트 생성
# >>> num_list=[1,2,3,4,5]
# >>> num_list * 3
# [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# >>> num2_list = num_list * 2
# >>> num2_list
# [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# == 자바에서는 참조가 같냐는 물음. 파이썬은 내용이 같냐는 물음
# ==연산자 : 두 리스트의 항목 값이 모두 같은 지를 검사.
# >>> list1 = [1, 2, 3, 4]
# >>> list2 = [1, 2, 3, 4]
# >>> list1 == list2
# True
# >>> list3 = [4, 1, 2, 3]
# >>> list1 == list3
# False

# ================================
# TERMINAL에서 python이라고 검색해야 대화모드. exit()해서 종료.