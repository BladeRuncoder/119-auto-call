#119 응급출동 서비스, 횟수제한 

index = 5

while index>=1:
    call = input('119입니다, 무엇을 도와드릴까요?')
    if '화재' in call:
        print('화재출동, 화재출동')
    elif '벌' in call:
        print('기타출동 : 말벌집')
    else:
        index-=1
        print('장난전화시 과태료가 부과됩니다 남은 요청횟수: {0}'.format(index))
    
    if index == 0:
        print('과태료부과대상입니다. 통화를 종료합니다')
        break
