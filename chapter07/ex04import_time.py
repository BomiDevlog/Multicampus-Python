# time모듈

# 숫자 1개로 날짜/ 시간 표현. UTC(세계 협정시. 세슘원자로 시간 측정. 세계표준. 기준은 영국 그리니치) GMT(영국 그리니치 측정 시간. 그러나 오차있음)
# UTC(에폭)는 1970-1-1-0-0-0에서 흐른 시간을 측정
# utc로 시간을 저장하고 전분야에서 사용
# 전분야에서 utc로 사용하고 사람이 읽기쉽게 변환해서 사용

'''
>>> import time
>>> seconds = time.time()
# time이라는 메소드안에 time()함수를 호출
>>> print('에폭 이후의 시간=', seconds)
에폭 이후의 시간= 1662355805.2997422
'''


# strftime()
import time
unix_timestamp = time.time()
# utc기준
local_time = time.localtime(unix_timestamp)
print(time.strftime('%Y-%m-%d %H:%M:%S', local_time)) # 날짜계산에 유용! 중요!
# 2022-09-05 14:33:46 : %Y 4자리년도  %H 24시간기준
print(time.strftime('%y-%m-%d %H:%M:%S', local_time))
# 22-09-05 14:35:23 : %y 2자리년도

print(__name__)
# __main__