'''chapter05_05_transfer.py v1.0'''

print('[교통카드 프로그램]\n')

total = 10000
bus = 0
subway = 0

while True:
    trans = input('이용하는 교통수단(버스/지하철): ')
    if trans == '버스':
        bus = bus + 1
        total = total - 1200
        print('이용하는 교통수단은 %s입니다. 금액은 %d입니다. 잔액은 %d입니다.' %(trans,1200,total))
    elif trans == '지하철':
        subway = subway + 1
        total = total - 1500
        print('이용하는 교통수단은 %s입니다. 금액은 %d입니다. 잔액은 %d입니다.' %(trans,1500,total))

    if total <= 1000:
        print('버스는 %d, 지하철 %d이용하셨습니다.' %(bus, subway))
        money=int(input('얼마를 충전하시겠습니까?(원): '))
        total = total + money
