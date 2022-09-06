f = open('hello2.txt', 'a', encoding='utf-8')
# 영어외의 언어는 인코딩을 해야 언어가 깨지지않는다.
# 오픈모드도 utf-8이고, 인코딩 키워드도 utf-8

# f.write('Hello World!')
# f.write('Hello~\n')
f.write('안녕하세요!\n')
# 개행문자 넣어서 줄바꿈

# 인코딩 안맞아서 글자 깽짐
# UTF-8 => EUC-KR

f.close()


'''
I/O작업을 누가 수행하는가?

ex08.py - open()요청 -> OS (모든 I/O 작업) 

'''

'''
데이터의 성격
t : text 문자코드 기록. 디폴트라서 t는 생략가능. 'wt'->'w', 'rt'->'r'
b : binary 이진데이터- 이미지, 소리. 'wb', 'rb'

'''