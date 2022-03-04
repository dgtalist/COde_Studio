'''chapter08_CA_chatbot.py v1.0'''

human_name = input('당신의 이름:')
bot_name = 'AI'

qna_dict = {
"안녕" : "안녕 하세요. ^^",
"이름" : "제 이름은 AI 입니다.",
"기분" : "저도 기분이 좋아요~!",
"음악" : "저는 방탄소년단이 좋아요."
}

while True:
    talk = input("%s : " %human_name)
    for qna in qna_dict:
        if talk in qna:
            print("%s : %s\n" %(bot_name, qna_dict[qna]))
            break
    if talk not in qna:
        print('죄송해요. 답변을 준비하도록 할께요.\n')
        continue
