import datetime as dt

today = dt.date.today()
print(f'오늘은 {today.year}년 {today.month}월 {today.day}일입니다')
xMas = dt.datetime(2022,12,25)
time_gap = xMas - dt.datetime.now()
# timedelta객체. datetime - datetime
print(f'다음 크리스마스 까지는 {time_gap.days}일 {time_gap.second//3600}시간 남았습니다.')
# 3600은 60분 60초로 나누어준 것인지?

