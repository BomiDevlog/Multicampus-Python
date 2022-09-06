# try구문일 경우
# try는 필수이고
# except나 finally는 최소1개는 반드시 써야하고 # try~except, try ~ finally
# else는 옵션
# 전부 사용해도 됨.

def divide (x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print('0으로 나누는 오류 발생')
    else:
        print('결과 :', result)
    finally: # 예외 발생 여부와 상관없이 '항상' 싱행됨
        print('수행 완료')

print('divide(100,2) 함수 호출 : ')
divide(100,2)
print('divide(100,0) 함수 호출 : ')
divide(100,0)

''' 
일반적으로 else는 거의 사용하지 않음
try문에 같이 묶는 편.

def divide (x,y):
    try:
        result = x/y
        print('결과 :', result)
    except ZeroDivisionError:
        print('0으로 나누는 오류 발생')
    finally: 
        print('수행 완료')

'''

