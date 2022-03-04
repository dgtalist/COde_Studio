'''chapter04_CA_ai vs human.py v1.0'''

import random

ai = random.choice(["가위", "바위", "보"])
human = input('가위, 바위, 보 중에 고르세요. : ')

if (ai == '가위') and (human == '가위') or (ai == '바위') and (human == "바위") or (ai == '보') and (human == "보"):
    print('인공지능이 %s를 냈습니다. 비겼습니다.' %ai)
elif (ai == '가위') and (human == '보') or (ai == '바위') and (human == "가위") or (ai == '보') and (human == "바위"):
    print('인공지능이 %s를 냈습니다. 졌습니다.' %ai)
elif (ai == '가위') and (human == '바위') or (ai == '바위') and (human == "보") or (ai == '보') and (human == "가위"):
    print('인공지능이 %s를 냈습니다. 이겼습니다.' %ai)
