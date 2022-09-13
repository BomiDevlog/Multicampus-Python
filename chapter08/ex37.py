'''
images 디렉토리 내용을 읽어 다음 형태의 사전을 구성하세요

base = 'images'

images = {
    'dog' : [ 'dog1.jpg', 'dog2.jpg'...]
    'cat' : [ 'cat1.jpg', 'cat2.jpg'...]
    ...
}

사전의 key는 분류명
value는 리스트로 사진파일명.

1) base디렉토리의 내용을 추출하는 것. => key가 된다.
2) value파트를 알아내야한다.
'''

import os
from os import path #os.path.--로 매번 표기하지 않아도됨. 바로 path.--로 접근 가능

base = 'images'

images = {} # 빈 사전 생성 : 최종적으로 만들고자하는 사전.

for dir in os.listdir(base): # base디렉토리의 내용 추출 
    # dir의 경로가 필요
    dir_path = path.join(base, dir)
    # os.listdir(dir) # 현재디렉토리에 dog cat이 있는 것이 아니라서 FileNotFoundError
    # print(dir)
    print(dir, dir_path)
    # images[dir] = [] # => dir이 key가 된다
    images[dir] = os.listdir(dir_path)
'''
images[dir] = [] 했을 때
cat
dog
{'cat': [], 'dog': []}
이제 []를 알면된다.
'''

print(images) # 확인용





