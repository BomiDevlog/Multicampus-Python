# slicing 슬라이싱 (매우 유용. 매우 중요!!!****)
# 리스트 내 특정 구간을 선택해 잘라내는 기능
# 리스트명[start:end] : end-1까지의 항목을 새 리스트에 삽입
# range와 마찬가지로 end는 포함되지않음 
# 생략하면 start는 디폴트가 0 (처음부터). end는 디폴트가 -1 (끝까지)
# end-start가 개수.ㅣ

# >>> a_list=[10,20,30,40,50,60,70,80]
# >>> a_list[1:5]
# [20, 30, 40, 50]
# >>> a_list[0:1]
# [10]
# >>> a_list[1:]
# [20, 30, 40, 50, 60, 70, 80]
# >>> a_list[:3]
# [10, 20, 30]
# >>> a_list
# [10, 20, 30, 40, 50, 60, 70, 80]
# 원본 리스트는 유지됨.

# a_list[start:end] 
