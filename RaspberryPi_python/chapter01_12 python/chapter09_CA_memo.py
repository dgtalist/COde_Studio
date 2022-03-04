'''chapter09_CA_memo.py v1.0'''

import time

while True:
    print()
    print('1.메모 쓰기')
    print('2.메모 읽기')
    sel = input('입력(1/2): ')
    if sel == '1':
        t = time.localtime()
        memo = input('내용 쓰기 : ')
        f = open('memo.txt', 'a')
        f.write('\n%d-%d-%d\n' %(t.tm_year, t.tm_mon, t.tm_mday))
        f.write('%s\n' %memo)
        f.close()
        print('메모가 작성 되었습니다.')
    elif sel == '2':
        f = open('memo.txt', 'r')
        r = f.read()
        print(r)
