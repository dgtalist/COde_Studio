'''chapter09_CA_memo2.py v1.0'''

import time

t = time.localtime()

title = input('제목:')
L1 = input('내용1:')
L2 = input('내용2:')

with open(title + '.txt', "w", encoding='UTF-8') as memo:
    memo.write('%d-%d-%d\n' %(t.tm_year, t.tm_mon, t.tm_mday))

with open(title + '.txt', "a", encoding='UTF-8') as memo:
    memo.write('%s\n' %L1)
    memo.write('%s\n' %L2)
