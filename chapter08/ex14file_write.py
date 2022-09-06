# 파일 입출력 : 5회 정수 입력, 평균, 합계 계산, 파일 저장

f= open('data5.txt', 'w')   # 파일 열기 : 쓰기 모드
for _ in range(5):
    n = input('정수를 입력하세요: ')   # 정수 입력 (n은 문자열. input은 문자열을 리턴함.)
    # print(type(n)) => <class 'str'>  int 아님.
    f.write(n)                     # 입력값을 문자열로 쓰기
    f.write('\n')                  # 줄 바꿈
    
f.close() # 파일 닫기