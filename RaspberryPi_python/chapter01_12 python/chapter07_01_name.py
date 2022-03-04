'''chapter07_01_name.py v1.0'''

번호 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
이름 = []

for i in range(0, 10):
    이름.append(input('이름:'))

이름.sort()
print()
print('[참가자 명단]')
for i in range(0, 10):
    print('%d번 %s' %(번호[i], 이름[i]))
