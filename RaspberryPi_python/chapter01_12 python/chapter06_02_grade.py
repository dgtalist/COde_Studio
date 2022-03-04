'''chapter06_02_grade.py v1.0'''

def floor(x):
  if 1 <= x < 3:
    return '%d학년은 1층으로 가세요.' %x
  elif 3 <= x < 5:
    return '%d학년은 2층으로 가세요.' %x
  elif 5 <= x <= 6:
    return '%d학년은 3층으로 가세요.' %x

print(floor(int(input('학년을 입력하세요. : '))))
