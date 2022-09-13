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

category_images = get_category_images(base)

# 파일명 변경
for dir, fnames in category_images.items():
    for ix, fname in enumerate(fnames, 1):
        src_path = path.join(base, dir, fname)
        dst_path = path.join(base, dir, f'{ix:04}'.jpg)
        print(f'{src_path} => {dst_path}')
        os.rename(src_path, dst_path)

#파일의 확장자 분리
# path.splitext("images/dog/aaaa.png") => ('images/dog/aaaa', '.png')