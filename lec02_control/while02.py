'''
while 문 연습


'''

# while True:
    # 무한루프 : 계속 반복해도 True다.
while True:
    print('[1] 입력')
    print('[2] 수정')
    print('[3] 삭제')
    print('[0] 종료')
    print('--------')
    print('메뉴 선택>>')
    menu = input()
    if menu == '0':
        break

print('프로그램 종료') # 계속 프로그램을 돌릴 수 있는 원천
# or
while 1: # 1 = True 이므로 / cf. while 0: 0 = false 이므로 실행하지 않음!
    print('[1] 입력')
    print('[2] 수정')
    print('[3] 삭제')
    print('[0] 종료')
    print('--------')
    print('메뉴 선택>>')
    menu = input()
    if menu == '0':
        break

print('프로그램 종료')
