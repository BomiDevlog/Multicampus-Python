# 멤버 연산자: in, not in
# 콜렉션에 내가 찾는 데이터가 있는지 확인할 때 사용

#  * for ~ in 과 헷갈리면 안돼용!

n_list = [11, 22, 33, 44, 55, 66]
if(55 in n_list) : 
    n_list.remove(55)
if(88 in n_list) :
    n_list.remove(88)
print(n_list)
