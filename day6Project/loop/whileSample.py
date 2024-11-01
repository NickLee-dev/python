# path : loop/whileSample.py  or loop\\whileSample.py
# module : loop.whileSample
# while 문 사용 테스트 스크립트
'''
while(반복에 대한 조건식):  (콜론 주의)
    반복 실행 구문들 (들여쓰기 주의)

반복에 대한 조건식은 무한루프가 되지 않게 작성할 것 (주로 종료값 제시)
만약, 조건식에 그냥 True를 사용한다면, 반드시 루프 안에서 종료에 대한 조건처리 구문이 있어야함
while True:
    반복 실행 구문
    if 종료조건:
        break
'''

def test_while():
    num = 5
    while num > 0:
        print(num)
        num -= 1

# 반복 횟수가 정해지지 않은 경우 while문 주로 사용함
# 예 : 문자 하나 입력 받아서, 그 문자의 유니코드를 출력처리 하는 구문이 반복 실행됨
# 단, '0'이 입력되면 반복이 종료됨

def print_unicode2():
    ch = input('문자 하나 입력 [0이 입력되면 종료됨] : ')
    while ch!='0':
        print(f'{ch} is unicode {ord(ch)}')
        ch = input('문자 하나 입력 [0이 입력되면 종료됨] : ')

def print_unicode():
    while True:
        a = input("문자 하나 입력해 주세요[0입력시 종료] : ")
        if len(a) >= 2:
            print('한글자만 입력하세요.')
            continue
        elif a == "0":
            break
        print(f'{a}의 유니코드 값 : {ord(a)}')

# 파이썬에서는 여러 줄의 물자열 값을 표현할 때 3쌍의 따옴표 이용할 수 있음
def display_menu():
    prompt = '''
        *** 원하는 메뉴 번호를 선택하세요. ***
        1. 추가
        2. 삭제
        3. 출력
        4. 끝내기
    '''
    # print(prompt)
    while True:
        print(prompt)
        no = int(input('번호 입력 : '))

        if no == 4:
            break

    print('-----END-----')
