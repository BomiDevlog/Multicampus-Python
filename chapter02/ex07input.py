

name = input('이름을 입력하세요 : ') 
# name은 문자열로 입력받음
print('이름 :',name)
# age = input('나이를 입력하세요 : ') #에러 확인용
age = int(input('나이를 입력하세요 : '))
# age는 문자열로 입력받아  int 형변환
print('10년 후 나이 :', age+10)
# 숫자 형변환 안했다면 9번라인에서 에러.

'''
Traceback (most recent call last):
  File "c:\python\chapter02\ex07input.py", line 9, in <module>
    print('10년 후 나이 :', age+10)
TypeError: can only concatenate str (not "int") to str
'''

# input은 리턴타입이 str.
# 숫자를 가지려면 형변환해야함.

# java의 경우 "2210" : 문자열+다른타입 -> 문자열 결합
# python의 경우 문자열+다른타입 => 에러 // 문자열+문자열(o) // 데이터 분석 시 입력데이터가 잘못되지않았는지 주의!