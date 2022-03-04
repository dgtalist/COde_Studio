'''chapter06_03_9x9.py v1.0'''

def multy(num):
  for i in range(1, 10):
    print('%d * %d = %d' %(num, i, num*i))
  return

multy(int(input('구구단 : ')))
