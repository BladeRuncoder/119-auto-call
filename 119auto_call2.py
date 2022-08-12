#119 응급출동 서비스, 횟수제한 


shutdown = False #응답기 종료구문 


def asking_address():  #주소묻기 함수
    while True:
        address = input('주소를 입력하여 주세요: ')
        sure = input('입력하신 주소는 ' +address+' 입니다. 맞으면 1,틀리면 2를 눌러주세요')
        if str(1) in sure :
            print('요청하신곳으로 119 출동합니다')
            break

        

while shutdown == False :
    call = input('119입니다, 원하시는 서비스를 선택해주세요 \n1.화재 \n2.기타출동 \n3.응급이송 서비스 \n4.수신원 연결')

    if '1' in call: #화재
        fire = input('경보기 오작동이면 1번을, 응급 화재는 2번을 눌러주세요')
        if '1' in fire:
            print('119는 경보기 오작동 출동을 나가지 않습니다.\n건물 소방안전 관리자를 호출하여 해결해주세요')
            break
        else:
            asking_address()
            shutdown = True


    
    if '2' in call: #기타
        type = input('엘리베이터는 1번, 벌집은 2번, 문갇힘은 3번, 기타 수신원 연결은 4번을 눌러주세요')
        if '1' in type:
            print('119는 엘리베이터는 나가지 않습니다, 건물 관리자를 호출하여 해결하세요')
            break
        if 1<int(type)<4 :
            asking_address()
            shutdown= True
        else:
            print('수신원을연결합니다')
            break

    if '3' in call: #구급대
        er = input('입원목적이면 1번, 응급실목적이면 2번을 눌러주세요')
        if '1' in er:
            print('알아서 가 이섀끼야')
            shutdown = True
        else:
            print('택시타고 가 이섀끼야')
            shutdown = True

    if '4' in call: #수보대 직통
        print('수신원을연결합니다')
        break



#숫자값 미입력시 구문 재전송 필요 