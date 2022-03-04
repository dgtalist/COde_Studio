'''chapter03_CA_score.py v1.0'''

year = input('학년:')
cla = input('반:')
name = input('이름:')

lan = input('국어:')
eng = input('영어:')
math = input('수학:')
sci = input('과학:')
soc = input('사회:')
art = input('미술:')

print('## 성적관리 프로그램 ##')
print('학년 : ' + year + ', 반 : ' + cla + ', 이름 : ' + name)
print('-'*30)
print('국어 : ' + lan + ', 영어 : ' + eng + ', 수학 : ' + math)
print('과학 : ' + sci + ', 사회 : ' + soc + ', 미술 : ' + art)
print('-'*30)
total = int(lan)+int(eng)+int(math)+int(sci)+int(soc)+int(art)
ave = round(total / 6, 1)
print('총점 : ' + str(total) + ', 평균 : ' + str(ave))
