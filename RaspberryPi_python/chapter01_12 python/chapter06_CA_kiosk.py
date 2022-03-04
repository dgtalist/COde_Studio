'''chapter06_CA_kiosk.py v1.0'''

def food(menu, num):
    if menu == '김치볶음밥':
        print('김치볶음밥 %d개 주문' %num)
        return 4000*num
    elif menu == '오므라이스':
        print('오므라이스 %d개 주문' %num)
        return 4500*num
    elif menu == '짜장면':
        print('짜장면 %d개 주문' %num)
        return 3500*num
    elif menu == '짬뽕':
        print('짬뽕 %d개 주문' %num)
        return 4000*num
    elif menu == '돈가스':
        print('돈가스 %d개 주문' %num)
        return 5000*num

#print(food('김치볶음밥', 3))

total = 0

while True:
    choice = input(
'''
[메뉴]
김치볶음밥 : 4000원
오므라이스 : 4500원
짜장면 : 3500원
짬뽕 : 4000원
돈가스 : 5000원

메뉴를 고르세요.(종료=x) : '''
)
    if choice == 'x':
        money=int(input('결제할 금액을 입력하세요.:'))
        break

    number = int(input('갯수? :'))
    total = total + food(choice, number)
 
print('계산하실 금액은 %d원 입니다. 잔돈은 %d원입니다.' %(total, money-total))
