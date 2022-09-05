# 100일 뒤 날짜 구하기
# timedelta
# 특정날짜로부터 해당 기간후의 날짜 도출.마감기한.

import datetime as dt
print('오늘=', dt.datetime.now()) # 현재 시간
hundred = dt.timedelta(days=100)   #100일 경과 시간
plus100day = dt.datetime.now() + hundred # 현재 시간에 100일 경과시간 더함
print('100일 후', plus100day)

# 500일 후 3주 전 . 8시간 후 등등 다양한 응용가능
# 월, 년 기준은 없다..(years=2, months=6 2년 6개월후는 안되는건가?)