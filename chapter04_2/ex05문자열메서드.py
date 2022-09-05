# 문자열 메서드

# endswith() ~~ 끝나느냐
# startswith() ~로 시작하느냐
# True, False를 반환

# 서브문자열 찾아주는것
# find() 못찾으면 -1, index() 못랒으면 에러

# upper(), 대문자 lower() 소문자. 대소문자구분없이 처리해야하는 통계처리할때 종종 사용.



'''
>>> 'abcABC'.upper()
'ABCABC'
>>> 'ABCABC'.lower()
'abcabc'
>>> 'hobby'.count('h')
1
>>> 'abcABC'.find('a')
0
>>>  'abcABC'.find('A')\
  File "<stdin>", line 1
    'abcABC'.find('A')\
IndentationError: unexpected indent
>>> 'abcABC'.find('A')
3
>>> 'abcABC'.find('D')
-1
>>>  'abcABC'.index('c')
  File "<stdin>", line 1
    'abcABC'.index('c')
IndentationError: unexpected indent
>>>
'''
# join 각 element를 결합
# rstrip() 오른쪽 공백 제거
# lstrip() 왼쪽 공백 제거
# strip() 양쪽 공백 제거
# split() 문자열을 콜론으로 분리해서 리스트로 반환.
# 스플릿(분리)과 조인(연결)을 같이 기억하기
'''
>>> ','.join('ABCD')
'A,B,C,D'
>>> ' hello '.rstrip()
' hello'
>>> ' hello'.lstrip()
'hello'
>>>  ' hello '.strip()
  File "<stdin>", line 1
    ' hello '.strip()
IndentationError: unexpected indent
>>> '  hello  '.strip()
'hello'
>>> s="X:Y:Z"
>>> s.split(':')
['X', 'Y', 'Z']
'''