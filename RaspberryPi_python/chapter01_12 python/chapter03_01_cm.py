'''chapter03_01_cm.py v1.0'''

print('< 길이 단위를 변환해 줍니다. >')
print()
cm = float(input('바꾸고 싶은 길이를 입력하세요. cm : '))
print()
print('입력하신 숫자의 m : ' + str(round(cm/100, 2)))
print('입력하신 숫자의 mm : ' + str(cm*10))
