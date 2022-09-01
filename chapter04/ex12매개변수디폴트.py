#함수의 인자 전달 방식

def print_star(n=1):        # 매개변수 n은 디폴트값으로 1 지정됨
    for _ in range(n):
        print('***********')

print_star()        # 인자 없어도 에러없이 수행됨.