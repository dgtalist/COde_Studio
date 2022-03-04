'''chapter03_05_circle.py v1.0'''

print('## 원기둥의 겉넓이와 부피를 구하는 프로그램입니다. ##')
print()
radius = float(input('반지름의 길이 : '))
height = float(input('높이 : '))
print()
surface = (2*3.14*radius*height) + (2*3.14*radius*radius)
volume = 3.14*radius*radius*height
print('입력한 원기둥의 겉넓이는 %.1f㎠, 부피는 %.1f㎤ 입니다.' %(surface, volume))
