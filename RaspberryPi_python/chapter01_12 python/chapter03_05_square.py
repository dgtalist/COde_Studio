'''chapter03_05_square.py v1.0'''

print('## 사다리꼴을 구하는 프로그램입니다. ##')
print()
top = input('윗면의 길이 : ')
bottom = input('아랫면의 길이 :')
height = input('높이 : ')
print()
area = (int(top)+int(bottom))*int(height)/2
print('입력한 사다리꼴의 단면적은 %.1f㎠ 입니다.' %area)
