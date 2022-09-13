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
# listdir, join 의 활용이 매우 중요

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


#함수 호출해 리턴해서 얻은 사전 category_images
category_images = get_category_images(base)
# print(category_images)


'''
머신러닝에서 이미지인식할 경우
훈련데이터를 구성하고 해당 파일 정볼르 관리할때 쓰는 기법이다

정답문자열을 만들고 사진을 분류해서
프로그램을 자동적으로 훈련시킬수있다
'''

'''
3. images 사전을 순회하여 모든 이미지 파일의 경로를 다음과 같이 출력하시오.

dog:
    images/dog/dog1.jpg
    images/dog/dog2.jpg
    images/dog/dog3.jpg
    ...
cat:
    images/cat/cat1.jpg
    images/cat/cat2.jpg
    images/cat/cat3.jpg
    ...

[힌트]
사전을 어떻게 순회하는지. 
key와 value를 어떻게 추출할지. # value는 파일명이 들어있는 리스트
내가 아는 정보로 어떻게 이러한 경로를 만들지.
'''

# 사전category_images에서 items를 호출해서 key와 value를 얻음
for dir, fnames in category_images.items():
    for fname in fnames:
        print(dir, fname)
        file_path = path.join(base, dir, fname)
        print(file_path)

        # base=>images , dir=>dog/cat, fname=>각 파일명으로 출력됨.
        # key는 dir, value는 fnames이고 이걸 다시 fname.


'''
(base) C:\python\chapter08>python -u "c:\python\chapter08\ex37_3.py"
cat cat1.png
images\cat\cat1.png
cat cat2.png
images\cat\cat2.png
cat cat3.png
images\cat\cat3.png
cat cat4.png
images\cat\cat4.png
cat cat5.png
images\cat\cat5.png
dog dog1.png
images\dog\dog1.png
dog dog2.png
images\dog\dog2.png
dog dog3.png
images\dog\dog3.png
dog dog4.png
images\dog\dog4.png
dog dog5.png
images\dog\dog5.png
'''

'''
파일의 경로를 분류화해서 머신러닝을 훈련시킴
'''

