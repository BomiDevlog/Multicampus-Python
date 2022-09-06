# csv
# 파일 처리할 때 

try:
    with open('sensors.csv', 'rt', encoding='utf-8') as f:
        data = f.readlines() # 파일 관련 작업은 여기까지이기에, for문은 with밖에서 작업해도 됨.

    for row in data: # 데이터를 다듬는 후속작업. 
        row = row.strip().split(',') #개행문자 제거, 콤마단위 분할
        print(row)

except Exception as e:
    print(e)

'''
ex30.py의 출력상태

19,livingroom,temp,28,"2022-08-31 12:23:38"

개행문자 제거가 안되었기때문에 엔터 빈줄이 들어감
데이터로써 날짜에 따옴표까지 들어감 -> 제거해야함
콤마단위로 끊음 -> 리스트로 변경
데이터는 전부 문자열이라 변환 필요
'''