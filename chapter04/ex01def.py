# 함수:재사용 가능한 코드 블록
# 코드블록에 이름을 지정(함수명)해서, 이름을 불러 해당 코드블록을 실행(함수 호출)
# 함수정의 def. 함수 코드블록은 반드시 들여쓰기.

def print_star():                 # 함수 정의(매개변수 없음. 리턴값 없음. 가장 단순 형태)
    print('***************************')

print_star()                      # 함수 호출
print_star()                      # 함수 호출 (재사용 가능)

print() # 줄바꿈

for i in range(4):
    print_star()