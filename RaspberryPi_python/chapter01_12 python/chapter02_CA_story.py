'''chapter02_CA_story.py v1.0'''

story = '''
아주 먼 옛날 숲 속에 일곱 난장이와 ＠＠＠공주님
이 살고 있었습니다.

＠＠＠공주의 미모를 시기하던 ※※※마법사가
독이 든 ＊＊를 먹여 공주가 깊은 잠에 들었습니다.

깊은 잠에 빠진 ＠＠＠공주를 구하기 위해 ☆☆☆왕자가
숲 속에 찾아와 ＠＠＠공주에게 ○○을(를) 하여 ＠＠＠공주가
깨어났고, 행복하게 살았답니다.
'''
story = story.replace('＠＠＠', '이로봇')
story = story.replace('※※※', '못 생긴')
story = story.replace('＊＊', '바이러스')
story = story.replace('☆☆☆', '파이썬')
story = story.replace('○○', '코딩')

print(story)
