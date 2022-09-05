# 혼용할 때 순서 주의

# : 일반변수, 가변변수, 키워드 가변변수 순서로 배치
# 일반변수(필수), 포지셔널, 키워드는 옵션인 가변변수이다.
# (예)calcstep(name,*score, **option)
# library함수에서 이러한 형태를 많이 취함
# xxx(*args, **kargs)

def calcscore(name, *score, **option) :
    print(name)
    total = 0
    for s in score:
        total += s
    
    print("총점 :", total)
    # if(option['avg']== True):
    # get으로 디폴트값을 주어야 생략가능한 옵션이다.
    if(option.get('avg',True)):
        print("평균 :", total/len(score))

calcscore("홍길동", 88, 99, 77, avg=True)
calcscore("고길동", 99, 88, 95, 85, avg=False) # 평균안나옴
calcscore("도우너", 91, 86, 85, 75) # 디폴트가 True라서 평균나옴
# calcscore("희동이", 91, 86, avg=False, 85, 75)  순서가 안맞아서 에러.
# calcscore("둘리")   
''' 에러.
total/len(score)) 
ZeroDivisionError: division by zero
'''



    