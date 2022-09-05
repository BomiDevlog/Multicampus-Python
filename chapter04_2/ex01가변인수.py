# 가변 인수
# print( , , )

# *args => positional (tuple 읽기전용) 위치기반 index
# **kargs => keyword (dict) name = value. name이 key값, value가 value값 
# 
#
#  

def greet(*names) :  # positional 가변인수
    # print(type(names)) # 확인용 # <class 'tuple'>
    print('인자의 개수:', len(names))
    print('인자들:', names)
    for name in names:
        print('안녕하세요', name, '씨')
greet('홍길동', '양만춘', '이순신')
greet('James', 'Thomas')
greet()         # 비어있는 튜플이 된다
greet('kim')    # element가 1개인 튜플이 된다