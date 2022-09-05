# keyword args로 가변인수를 받으면 dict로 전달된다.

def calcstep(**args): #가변 인수
    print(args)
    # begin = args['begin']
    # end = args['end']
    # step = args['step']
    begin = args.get('begin', 0)
    end = args.get('end', 0)
    step = args.get('step', 0)
    # 가변키워드인자방식에서 인자에 디폴트 값을 배정

    total = 0
    for num in range(begin, end +1, step):
        total += num
    
    return total

# 키워드 호출
print("3 ~ 5 =", calcstep(begin=3, end=5, step=1))
print("3 ~ 5 =", calcstep(step=1, end=5, begin=3))
print("3 ~ 5 =", calcstep(step=1, end=5, begin=3, END=4, BEGIN=3))
# 내부적으로 처리안되지만 dict에 담긴다. 호출에는 영향을 주지않는다
print("3 ~ 5 =", calcstep(step=1, end=5))
# KeyError: 'begin'
# 없는 키에 대해 인덱싱에 추출을 못해서 에러 발생 (읽기못해서 에러)
# get으로 디폴트값을 부여하니 정상적으로 실행됨
print("3 ~ 5 =", calcstep(step=1, end=4, Begin=2 ))
# 대소문자 구분. begin 0부터.

# dict
even = {
    'begin': 0,
    'end': 100,
    'step': 2    
}

print(calcstep(**even))
# dict의 펼침은 **별표2개.

odd = {
    **even,
    'begin':1
}
# 사전 내에서 사전을 펼치고 begin만 재정의
# 그러면 even의 'end': 100, 'step': 2 을 유지하면서 begin은 1로 시작해 홀수표현. 
print(odd)
print(calcstep(**odd))