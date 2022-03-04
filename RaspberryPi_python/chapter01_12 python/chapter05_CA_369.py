'''chapter05_CA_369.py v1.0'''

count = 0
print('3, 6, 9 게임')
print()

while True:
  count = count + 1
  print(count)
  c = input()
  if '3' in str(count) or '6' in str(count) or '9' in str(count):
    if c == ' ':
      continue
    else:
      print('아웃!!')
      break
    
