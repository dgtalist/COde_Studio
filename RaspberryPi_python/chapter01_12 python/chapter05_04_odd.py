'''chapter05_04_odd.py v1.0'''

first = int(input('첫숫자:'))
second = int(input('두번째숫자:'))

for i in range(first, second+1):
    if i % 2 == 1:
        print(i)
