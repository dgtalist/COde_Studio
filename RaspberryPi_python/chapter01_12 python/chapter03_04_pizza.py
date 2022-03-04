'''chapter03_04_pizza.py v1.0'''

num = (12 * 7) / 32
piece = (12 * 7) % 32
price = 7 * 12000

print('1인당 %d개의 피자를 먹을 수 있고, %d개가 남아요.' %(num, piece))
print()
print('1인당 %d원을 내야 합니다.' %round(price/32))
