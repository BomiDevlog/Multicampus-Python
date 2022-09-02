# 무한 루프를 돌면서 검색어를 입력함
# 검색어로 exit를 입력하면 루프 종료
# 입력한 검색어의 검색 회수 관리 => 딕셔너리 이용. 검색어 : 카운트
# 결과 출력
#  검색어1 : n
#  검색어2 : m ...

keywords = {} # 빈 딕셔너리 생성

while True: 
    keyword = input('검색어 : ')
    if keyword == 'exit' :
        break

    print('----------------')
    # 검색어를 찾아서 기존에 존재하면 검색어의 카운트를 1 증가 시킴
    # 처음 등장하는 키워드는 0으로 간주하고 카운트 1로 추가
    keywords[keyword] = keywords.get(keyword, 0) + 1


    #정렬
    #상위 10개 추출 -> 실시간 인기검색어

# 결과 출력 : 딕셔너리 순회
for keyword, count in keywords.items() :
    print(f'{keyword} : {count}')

