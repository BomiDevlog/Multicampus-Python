# 리스트 항목의 추가와 삭제

# del명령어: del numbers[2] 3번째 element삭제. index기반
# remove()메서드: numbers.remove(30) 30이라는 데이터 삭제. 데이터 기반. 해당 데이터 없으면 예외 발생
# pop() 메서드: 삭제하고 해당 값을 반환. xxx= numbers.pop(3)
# 리턴값이 존재하여 삭제하는 값을 반환한다. 
# pop() 매개변수안넣으면 디폴트가 -1이라서 마지막요소를 삭제하고 반환.

from tkinter import N


n_list = [11, 22, 33, 44, 55, 66]
print(n_list) # 전체 항목 출력

del n_list[3] # 4번째 항목 (44) 삭제
print(n_list)

n_list.remove(55) # 55라는 값을 가진 항목 삭제
print(n_list)

# 예외 발생때문에 이러한 값이 있니? 라는 검사를 거친다 (예) in 멤버 연산자
# n_list.remove(100) 
'''
Traceback (most recent call last):
  File "c:\python\ex05list.py", line 19, in <module>
    n_list.remove(100)
ValueError: list.remove(x): x not in list
없는 값을 삭제하라는 remove()는 예외 발생
'''

print('---------------------')

a_list = [15, 25, 35, 45, 55, 65]
print(a_list)

a_list.pop() # 마지막요소 삭제
print(a_list)

print(a_list.pop()) # 삭제하면서 마지막 요소 값을 반환


a_list.pop(-1) # 마지막요소 삭제
print(a_list)

a_list.pop(0) # 첫 번째 요소 삭제
print(a_list)

print(a_list.pop(0)) # 삭제하면서 첫번째 요소 값을 반환

# ----------------------------
# stack : LIFO (last in first out)
# stack = [] 삭제되고 추가됨
# stack.append(20),  stack.append(10), stack.append(30)
# stack.pop() : 가장 위에 있는 요소가 리턴됨 -> 30, 10 순서
# stack.append(40)한다면 stack은 아래에서부터 20, 40이 쌓임

# Queue : FIFO (first in first out. 먼저 들어간것이 먼저 나옴. 줄세우기 순서 보장)
# q.append(10), q.append(20), q.append(30)
# q.pop(0)->10리턴. q.pop(0)->20리턴. q.pop(0)->30리턴.
# 순서를 유지하면서 데이터를 보관할 때 큐 사용. 버퍼라고도 부름.
# ----------------------------
# ----------------------------