file_names = {
    'song1.mp3',
    'image1.JPG',
    'image2.jPG',
    'song2.Mp3',
    'video1.mp4',
    'song3.mp3'
}

# 전달된 파일면 리스트에서 mp3파일만 담긴
# 튜플을 반환하는 함수(find_song)를 만드세요.

def find_song(names):
    songs=[]
    # 빈 리스트 생성. 튜플로 생성하면 변경불가라서 append가 안된다.
    for name in names:
        test_name = name.lower() #소문자로 통일해서 찾기
        if test_name.endswith('.mp3'): 
            songs.append(name) #리스트에 원본이름으로 저장
    return tuple(songs)

songs = find_song(file_names)
for song in songs:
    print(song)