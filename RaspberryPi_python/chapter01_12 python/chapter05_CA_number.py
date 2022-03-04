'''chapter05_CA_number.py v1.0'''

import random
ai = random.randint(1, 100)
count = 0
print('컴퓨터가 생각한 1부터 100 중에 숫자를 맞추세요.')

while True:
    human = int(input('추측하는 숫자는? : '))
    if ai > human:
        print('그 숫자보다 커야 합니다.')
        count = count + 1
        if count == 5:
            print('기회가 없어졌습니다. ai가 생각한 숫자는 %d 입니다.' %ai)
            break
        continue
    elif ai < human:
        print('그 숫자보다 작아야 합니다.')
        count = count + 1
        if count == 5:
            print('기회가 없어졌습니다. ai가 생각한 숫자는 %d 입니다.' %ai)
            break
        continue
    elif ai == human:
        print('맞췄습니다. ai가 생각한 숫자는 %d 이고 %d 번째에 맞췄습니다.' %(ai,count))
        break
