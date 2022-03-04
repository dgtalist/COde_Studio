'''chapter06_04_drink.py v1.0'''

def 음료수(drink, price):
    if drink == '사이다':
        print('사이다 %d개, ' %price, end='')
        return 1000*price
    elif drink == '콜라':
        print('콜라 %d개, ' %price, end='')
        return 1200*price
    elif drink == '물':
        print('물 %d개, ' %price, end='')
        return 500*price

choice = input('음료수를 고르세요.(사이다/콜라/물) : ')
num = int(input('개수를 입력하세요. : '))

print(str(음료수(choice, num)) + '원 입니다.')
