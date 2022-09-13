# 문자열, datetime간 변환
'''
datetime.strftime(datetime 객체, 포맷문자열) : datetime -> 문자열
datetime.strptime(날짜문자열, 포맷문자열) : 문자열 -> datetime

f는 format의미. p는 parse분석하다를 의미
'''

from datetime import datetime
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
now = datetime.now()

# datetime -> 문자열 변환
now_str = datetime.strftime(now, DATE_FORMAT)
print(now_str)

# 문자열 -> datetime 변환
str_date = "2022-08-31 11:31:27"
s_date = datetime.strptime(str_date, DATE_FORMAT)
print(type(s_date), s_date)

# 출력 
# 2022-09-08 10:39:54
# <class 'datetime.datetime'> 2022-08-31 11:31:27


# 파일2.pdf참고