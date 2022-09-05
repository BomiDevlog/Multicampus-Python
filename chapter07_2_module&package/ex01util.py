# 내가 만드는 모듈

# 모듈의 정의

INCH=2.54
# 대문자로 사용 -> 상수로 사용하겠다는 명명 관례 (final처럼실제로 상수가 되는 것은 아님. 대입, 변경하지 말라는 시그널일 뿐.) 

def calcsum(n):
    sum = 0
    for num in range(n+1):
        sum+= num
    return sum


print('util.py')
print('module name:', __name__)
# 단독으로 사용하는 것은 모듈이 아님
# 다른 파일에서 import로 부를 때 모듈이 됨!

# 모듈 테스트 코드 : 내 모듈의 함수가 제대로 동작하는지 테스트할 때 배치
if __name__ == '__main__': # (모듈이 아니라) 자체실행된 경우인가? 
    print(calcsum(10))
    print(calcsum(20))
# 자체실행이라면 True라서 코드 실행
# 다른 파일에서 import로 부른 경우라면 False라 실행x