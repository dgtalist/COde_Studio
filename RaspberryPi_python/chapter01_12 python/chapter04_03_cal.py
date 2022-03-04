'''chapter04_03_cal.py v1.0'''

mw = input("성별을 입력하세요. 남/여 : ")
tall = float(input("키를 입력하세요.(m) : "))
kg = float(input("몸무게를 입력하세요.(kg) : "))

if mw == '남':
    m = tall * tall * 22  #남자
    m_standard = (kg - m)/ m * 100
    if m_standard < -10:
        print('당신은 저체충입니다.')
    elif -10 < m_standard <= 10:
        print('당신은 정상체충입니다.')
    elif 10 < m_standard < 20:
        print('당신은 과체충입니다.')
    elif m_standard >= 20:
        print('당신은 비만입니다.')

elif mw == '여':
    w = tall * tall * 21  #여자
    w_standard = (kg - w)/ w * 100
    if w_standard < -10:
        print('당신은 저체충입니다.')
    elif -10 < w_standard <= 10:
        print('당신은 정상체충입니다.')
    elif 10 < w_standard < 20:
        print('당신은 과체충입니다.')
    elif w_standard >= 20:
        print('당신은 비만입니다.')
