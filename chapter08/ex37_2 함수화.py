'''
1. images 디렉토리 내용을 읽어 다음 형태의 사전을 구성하세요

base = 'images'

images = {
    'dog' : [ 'dog1.jpg', 'dog2.jpg'...]
    'cat' : [ 'cat1.jpg', 'cat2.jpg'...]
    ...
}
사전의 key는 분류명
value는 리스트로 사진파일명.

2. 기준이 되는 디렉토리를 제시하면 사전이 리턴되도록 프로그램을 구성하세요.
'''

import os
from os import path

base = 'images'

def get_category_images(base): #매개변수
    images = {} # 빈 사전 생성 : 최종적으로 만들고자하는 사전.

    for dir in os.listdir(base): # base디렉토리의 내용 추출 
        # dir의 경로가 필요
        dir_path = path.join(base, dir)
        # print(dir, dir_path)
        images[dir] = os.listdir(dir_path) # => dir이 key가 된다
    
    return images


#함수 호출
category_images = get_category_images(base)
print(category_images)


'''
머신러닝에서 이미지인식할 경우
훈련데이터를 구성하고 해당 파일 정볼르 관리할때 쓰는 기법이다

정답문자열을 만들고 사진을 분류해서
프로그램을 자동적으로 훈련시킬수있다
'''


