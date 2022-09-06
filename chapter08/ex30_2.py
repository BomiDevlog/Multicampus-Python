# csv
# 파일 처리할 때 기본 골격
try:
    with open('sensors.csv', 'rt', encoding='utf-8') as f:
        pass
except Exception as e:
    print(e)

