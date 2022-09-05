datas = [
    "livingroom, temp, 24.5",   # ---> 사전
    "livingroom, humi, 60.4",   # ---> 사전...
    "bedroom, temp, 28.5",
    "bedroom, humi, 60.2",
]
#아두이노로 입력받은 데이터들

# 전달된 문자열 리스트 데이터를 
# place, type, value 키를 가지는 사전의 리스트로 
# 변환하는 함수 load_data()를 만드세요

def load_data(datas) :
    # pass
    dict_list = [] # 빈 리스트 생성
    for line in datas: # 입력받은 데이터를 for문
        # pass
        row = line.split(',') #, 단위로 데이터를 분할.(split)
        data = {
            'place' : row[0].strip(),
            'type' : row[1].strip(),
            'value' : float(row[2]) # 플로트 형변환하니까 좌우공백제거는 할 필요 없음.
        }
        dict_list.append(data)
        # 사전을 생성해, 리스트에 추가(append)
    
    return dict_list

dict_list = load_data(datas)

print(dict_list)

for data in dict_list:
    print(data)