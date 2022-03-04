'''chapter04_01_rollercoaster.py v1.0'''

print('< 신나는 롤러코스터 입니다. >')

tall = float(input('당신의 키는?(cm) : '))

if tall >= 150:
    print('탑승이 가능합니다.') 
elif tall < 150:
    print('탑승이 불가능합니다.')
