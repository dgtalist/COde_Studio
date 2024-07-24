import time
import Adafruit_ADS1x15
from RPLCD.i2c import CharLCD

# ADS1115 설정
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1  # 입력 범위를 설정 (±4.096V)

# LCD 설정
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=16, rows=2, dotsize=8,
              charmap='A00', auto_linebreaks=True,
              backlight_enabled=True)

def read_sound_level():
    # A0 채널에서 아날로그 값을 읽기
    value = adc.read_adc(0, gain=GAIN)
    return value

def display_on_lcd(value):
    # LCD에 값을 표시
    lcd.clear()
    lcd.write_string(f'Sound Level:\n{value}')

try:
    while True:
        # 소리 센서 값을 읽기
        sound_level = read_sound_level()
        
        # LCD에 값을 표시
        display_on_lcd(sound_level)
        
        # 0.5초 대기
        time.sleep(0.5)

except KeyboardInterrupt:
    # 프로그램이 중지될 때 LCD를 지움
    lcd.clear()
    print("프로그램을 종료합니다.")
