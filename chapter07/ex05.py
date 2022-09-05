# 1~10까지의 합을 구하여 출력하는데 걸리는 시간을 측정
# time 모듈
# 중요중요!!

import time
start_time = time.time()
print(1+2+3+4+5+6+7+8+9+10)

end_time = time.time()  #
gap = end_time - start_time
print(f'1에서 10까지의 합을 구하고 출력하는 시간 : {gap:7.4f}초')
# :7.4f => 7자리로 표현하는데 소수점이하 4자리까지 표현하라 : 스페이스와 .까지 모두해서 7자리됨.

