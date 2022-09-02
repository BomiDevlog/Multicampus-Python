# list 값 수정 - 순서, 개수는 유지하면서 값만 수정. 
# 데이터분석에서 자주 이용됨. 일종의 전처리 가공 작업

list1 = [10, 20, 30, 40, 50]

i=0

for n in list1:
    list1[i] = n*10
    i = i +1
print(list1)

for ix, num in enumerate(list1) :
   list1[ix] = num *10
print(list1)

# [x]
# for ix, num in enumerate(list1) :
#    num *= 2
# print(list1)


