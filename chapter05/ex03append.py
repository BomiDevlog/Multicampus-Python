numbers = [ 13, 25, 67, 30, 46, 84, 95, 62, 21, 89, 97 ]

# 리스트의 요소 중 홀수의 값만 찾아 odd_list에 저장하세요.
# odd_list를 출력하세요

odd_list = [] # 빈 리스트 생성

for n in numbers:
    if n % 2 == 1: # 홀수 검사
        odd_list.append(n)
print(odd_list)

# 데이터 분석에서 자주 사용하는 패턴.
# 전체 리스트에저 일부 데이터를 추출하려고
# 빈 리스트만들어서 for반복문에서 if조건걸고 append로 추가.
