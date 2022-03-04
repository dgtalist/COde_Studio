'''chapter03_02_money.py v1.0'''

print('< 환율 계산기 입니다. >')
print()
kor = int(input('한국 돈을 원단위로 입력하세요. : '))
print()
america = kor * 0.00091
japan = kor * 0.093
china = kor * 0.00591
print('미국 : ' + str(america) + '달러')
print('일본 : ' + str(japan) + '엔')
print('중국 : ' + str(china) + '위안')
