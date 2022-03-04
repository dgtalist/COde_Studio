'''chapter08_CA_chat.py v1.0'''

bot_name = 'SE'
human_name = input('당신의 이름:')

product_dict = {
'스마트폰' : '스마트폰 안내입니다. 구매 / 수리 / 문의',
'냉장고' : '냉장고 안내입니다. 구매 / 수리 / 문의',
'TV' : 'TV 안내입니다. 구매 / 수리 / 문의',
}

qna_dict = {
'구매' : '가까운 디지털프라자를 방문해 주세요.',
'수리' : '증상을 메모해서 가까운 AS 센터로 보내주세요.',
'문의' : '상담원과 연결을 하겠습니다.'
}

#print(type(qna_dict))

while True:
    print('SE 입니다. 가전제품을 입력하세요.')
    talk1 = input('%s : ' %human_name)
    for qna1 in product_dict:
        if talk1 in qna1:
            print('SE : %s' %product_dict[qna1])
            talk2 = input('%s : ' %human_name)
            for qna2 in qna_dict:
                if talk2 in qna2:
                    print('SE : %s\n' %qna_dict[qna2])
                    break
            if qna2 not in talk2:
                print('없는 항목입니다. 상담원에 바로 연결하겠습니다.')
                break
        continue
    if qna1 not in talk1:
        print('제품 분류를 다시 입력해 주세요.\n')
        continue
