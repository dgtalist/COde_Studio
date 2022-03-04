'''chapter05_01_divisor.py v1.0'''

num = int(input('약수를 알고 싶은 수 : '))
for i in range(1, num+1):
    if num % i ==0:
        print('%d 의 약수는 %d 입니다.' %(num, i))
