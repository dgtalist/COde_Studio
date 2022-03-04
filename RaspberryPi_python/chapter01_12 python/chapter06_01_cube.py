'''chapter06_01_cube.py v1.0'''

def area(x, y):
  num = (x * y * 6)
  return num

width = float(input('가로 또는 세로의 길이 : '))
height = width

cube = area(width, height)
print('입력한 정육면체의 넓이는 %.1f㎠ 입니다.' %cube)
