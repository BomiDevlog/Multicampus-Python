# csv
# 파일 처리할 때 

try:
    with open('sensors.csv', 'rt', encoding='utf-8') as f:
        data = f.readlines()
        # 개행문자 제거가 안되었기때문에 엔터 빈줄이 들어감
        for row in data:
            print(row)

except Exception as e:
    print(e)

