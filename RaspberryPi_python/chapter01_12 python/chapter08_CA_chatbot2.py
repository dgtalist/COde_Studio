'''chapter08_CA_chatbot2.py v1.0'''

AI = 'SE'
human = input('당신의 이름 : ')

product_dict = {
'핸드폰' : '핸드폰 안내입니다.\t구매 / 수리 / 문의',
'냉장고' : '냉장고 안내입니다.\t구매 / 수리 / 문의',
'TV' : 'TV 안내입니다.\t구매 / 수리 / 문의'
}

qna_dict = {
'구매' : '가까운 디지털프라자를 방문해 주세요.',
'수리' : '증상을 메모해서 가까운 AS 센터로 보내주세요.',
'문의' : '상담원과 연결을 하겠습니다.'
}

while True:
    print('SE 입니다. 가전제품을 입력하세요.')
    talk1 = input('%s : ' %human)
    for qna1 in product_dict:
        if talk1 in qna1:
            print('%s : %s' %(AI, product_dict[qna1]))
            talk2 = input('%s : ' %human)
            for qna2 in qna_dict:
                if talk2 in qna2:
                    print('%s : %s\n' %(AI, qna_dict[qna2]))
                    break
            if talk2 not in qna2:
                print('없는 질문입니다. 상담원으로 통해 답변 받으세요.\n')
                break
            break
        continue
    if talk1 not in qna1:
        print('제품 분류를 다시 입력해 주세요.\n')
        continue









