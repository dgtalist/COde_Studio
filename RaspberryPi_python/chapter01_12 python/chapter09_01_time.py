'''chapter09_01_time.py v1.0'''

import time

while True:
    t = time.localtime()
    print('현재 시간은 %d시 %d분 %d초 입니다.' %(t.tm_hour, t.tm_min, t.tm_sec))
    time.sleep(1)
