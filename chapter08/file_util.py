def read_file_lines(fname):
    try:
        with open(fname, 'r', encoding='utf-8') as f:  # 1. 파일 열기
            data = f.readlines()    # 2. 한 줄 단위로 리스트를 얻음
            data = [line.strip() for line in data] # 3. comprehension으로 filter : 공백 제거
        return data
    except Exception as e:      # 6. 예외 처리
        print('error:', e)
    
# 모듈 테스트
if __name__ == '__main__': # 모듈의 이름 # 자체실행하는 경우라면
    data = read_file_lines('foo.txt')
    print(data)


