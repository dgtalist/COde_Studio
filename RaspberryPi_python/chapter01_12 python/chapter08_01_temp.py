'''chapter08_01_temp.py v1.0'''

weather = {
'서울' : '23도',
'대전' : '24도',
'대구' : '26도',
'부산' : '24도',
'광주' : '25도'
}

city = input('도시이름:')

for i in weather:
    if city in i:
        print(city + '(은)는 현재 ' + weather[city] + '입니다.')
        break
if city not in i:
    print('해당 도시의 정보는 없습니다.')
