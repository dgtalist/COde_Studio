'''chapter04_CA_calculator.py v1.0'''

print('[ 계산기 프로그램 ]')
print()
num1 = float(input('계산할 첫번째 숫자:'))
num2 = float(input('계산할 두번째 숫자:'))
cal = input('계산방법(+, -, *, /) :')

if cal == '+':
    print('결과 : ', round(num1 + num2, 2))
elif cal == '-':
    print('결과 : ', round(num1 - num2, 2))
elif cal == '*':
    print('결과 : ', round(num1 * num2, 2))
elif cal == '/':
    print('결과 : ', round(num1 / num2, 2))
