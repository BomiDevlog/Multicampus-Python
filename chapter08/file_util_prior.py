def read_file_lines(fname):
    f = None
    try:
        f=open(fname, 'r', encoding='utf-8')  # 1. 파일 열기
        data = f.readlines()    # 2. 한 줄 단위로 리스트를 얻음
        data = [line.strip() for line in data] # 3. comprehension으로 filter : 공백 제거
        return data
    except Exception as e:      # 6. 예외 처리
        print('error:', e)
    finally:
        if f: #f가 None이 아니라면 실행됨. 즉 파일이 열린다면.
            f.close()               # 4. 파일 닫기 (에러여부와 별개로 파일을 닫아야함)
        # 오픈에서 실패했다면? 파일이 열리지않았는데 닫기해서 또 에러나서 프로그램 사망 -> f를 None설정


# 모듈 테스트
if __name__ == '__main__': # 모듈의 이름 # 자체실행하는 경우라면
    data = read_file_lines('foo.txt')
    print(data)


# if __name__ == '__main__':
#     print('모듈테스트')