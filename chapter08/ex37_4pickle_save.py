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

# pickle모듈 (저장하기)

import pickle

def save(fpath, data):
    try: 
        with open(fpath, 'wb') as file: # 바이너리 모드로 작업. encodint='utf-8'은 텍스트에서만 적용되니 작성하지 않음.
            pickle.dump(data, file)
    except Exception as e:
        print(f"{fpath} 파일 쓰기에 실패했습니다")
        print(e)


#함수 호출해 리턴해서 얻은 사전 category_images
category_images = get_category_images(base)

save('category.dat', category_images)
# 확장명 dat는 data의 약자. 확장명은 임의로 정하면 됨.
# 실행하니 category.dat라는 파일이 새로 생성됨

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
파일의 경로를 분류화해서 머신러닝을 훈련시킴
'''

