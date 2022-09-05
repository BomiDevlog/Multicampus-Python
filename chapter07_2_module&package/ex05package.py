# 패키지는 주로 from으로 import

# from mypack.calc import * 
# 과거 버전은 가능하지만 현재 버전에서 지원안됨.
# __init__.py에서 __all_지정 후 사용 가능
# 비권장

from mypack.calc import add, multi
# 현재 작성중인 지점을 기준으로 서브 디렉토리의 경로가 일치해야한다. 위치 중요!
# 권장 표기

# from mypack.calc.add import outadd 로 서술해주어도 가능o.

add.outadd(1, 2)
multi.outmulti(1, 2)

