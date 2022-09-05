# 모듈(부품) : 재사용 가능한 코드를 저장한 파일 -> 반복코딩을 줄임.

# 모듈은 3가지가 있다.
# 파이썬이 제공하는 모듈 (표준 모듈)
# 내가 만들어서 제공하는 모듈
# 제3자가 만들어서 제공하는 모듈 (추가 설치해서 사용)

# C:\ProgramData\Anaconda3\Lib 여기에 기본모듈들

# datetime모듈

# datetime.datetime.now()
# 모듈명.객체명.메서드()
# datetime이라는 모듈안에 datetime이라는 객체 인스턴스가 있다 now메서드를 이용한다.
'''
>>> import datetime
>>> datetime.datetime.now()
datetime.datetime(2022, 9, 5, 12, 37, 6, 992713)
년 월 일 시 분 초 밀리세컨드

데이터분석 시 항상사용 . 날짜 시간
'''
# date클래스 today() 날짜정보. 년월일
''' import하고 써야함.
>>> today=datetime.date.today()
>>> print(today)
2022-09-05
>>> today
datetime.date(2022, 9, 5)  #2022, 9, 5는 멤버변수
>>> today.year
2022
>>> today.month
9
>>> today.day
5
>>> type(today)
<class 'datetime.date'>
문자열 아니고 데이트클래스이다
'''

# dir()함수 : 모듈/객체가 가진 내용물의 목록을 출력
'''
>>> dir(datetime)
['MAXYEAR', 'MINYEAR', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
'''
# datetime이 가진 클래스가 문자열 리스트로 출력됨.
'''
>>> dir(list)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', 
'__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
'''
# 양쪽으로 __ㅇㅇ__ 형태는 파이썬 내부에서 사용하는 특수 메소드/ 특수 변수
# '__str__'는 자바의 toString()과 같은 역할. : 프린트에서 문자열로 대체해서 오버라이드 하고싶을 때

# replace() 메소드
'''
>>> start_time = datetime.datetime.now()
# 모듈명.객체명.메서드()
>>> start_time.replace(month=12, day=25)
datetime.datetime(2022, 12, 25, 14, 1, 35, 467952)
'''

# import 모듈형 으로 사용해야함.
# 매번 모듈명.객체명.메서드() 적는 것이 번거로움

# import[모듈이름] as [모듈별칭] 
# 모듈명은 파일명이다. datetime.py라는 파일이 존재함
'''
>>> import datetime as d
>>> start_time = d.datetime.now()
>>> start_time.replace(month=12, day=25)
datetime.datetime(2022, 12, 25, 14, 5, 38, 507781)
'''
# import datetime as dt
# 구글에서 제공하는 딥러닝 라이브러리
# import numpy as np
#  import tensorflow as tf

# 모듈명을 생략하고 싶을 때
# from datetime import datetime
# 호출할때 모듈명 생략핵서  객체명.메서드() 로 접근

# import하는 4가지 방법
# import A
# import A as a
# import A import T
# import A import as t