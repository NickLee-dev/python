# chap02_input.py

# 파이썬에서 실행시 키보드로 값 입력받기 : input() 함수 사용함
# 변수 = input('입력을 위한 메시지 문장')
'''
# 입력을 위한 메세지 없이 실행 테스트
# input 함수의 데이터 자료형은 str이다
# num = input()
num = input('숫자를 입력하세요 : ')
print('num : ', num, type(num))

# 파이썬의 input() 함수로 입력 들어오는 값은 모두 문자형(str)이다.
# print ('더하기 : ', num+100) # 문자와 숫자는 계산 할 수 없음 : TypeError 발생

# 숫자형으로 바꾸고자 한다면
# 정수는 int('정수문자'), 실수는 float('실수형문자') 함수 사용함

inum = int(num)
print('inum : ', inum, type(inum))
print('더하기 : ', inum + 100)
'''
'''
# 입력 예 :
# 정수 2개를 각각 입력 받아서, 사칙 연산 결과를 출력

first = int(input('첫번째 정수 : '))
second = int(input('두번째 정수 : '))

print(first,'+',second,'=',first+second)

# f'str' : format string
print(f'{first} - {second} = {first - second}')

# format() 함수 이용
print('{} * {} = {}'.format(first, second, first * second))

# format 함수와 순번(index)을 적용할 수도 있음
print('{1} / {0} = {2:.2f}'.format(second, first, first / second))
# 중괄호 안에 인덱스 순번 및 포맷 형식을 정해서 출력할 수 잇음

print(f'{first} ** 2 = {first ** 2}')
print(f'{second} ** 2 = {second ** 2}')
'''
# 입력 연습1
'''
신상정보를 입력받아, 각 변수에 저장하시오. 변수이름은 임의대로 지정함
이름(str), 나이(int), 성별(str, 남|여로 입력), 키(float), 몸무게(float)
각 변수의 값을 아래의 형식으로 출력하는 코드를 작성하시오
홍길동은 27세 남자이고, 키는 178.5cm  몸무게는 72.0kg 입니다.


name = input('이름 : ')
age = int(input('나이 : '))
gender = input('성별 [남/여] : ')
height = float(input('키 : '))
weight = float(input('몸무게 : '))

print(name, '은', age, '세', gender,'자이고, 키는',height,'cm이고 몸무게는', weight,'kg이다.')
# format() 함수를 이용한 출력문
print('{}은 {}세 {}자이고 키는 {}cm이고 몸무게는 {}kg이다'.format(name, age, gender, height, weight))
# format() 함수와 순번을 적용한 출력문
print('{1}은 {0}세 {3}자이고 키는 {2:.1f}cm이고 몸무게는 {4:.1f}kg이다'.format(age, name, height, gender, weight))
'''
# 입력 연습2
'''
키보드로 값을 입력받아 요구조건대로 처리하고 출력되게 코드를 작성하시오.
기본값을 가진 변수 생성 할당해 둠 : 
    total_point = 12500
입력 내용 : 
    고객 이름 : 황지니(custom_name : str)
    결재 금액 : 3000000 (price : int)
처리 내용 : 
    결재금액의 5%를 포인트(point : float)로 처리
    계산된 포인트를 누적포인트(total_point)에 증가 연산 처리함
출력 내용 : 
    황지니 고객님의 사용금액은 3000000 원, 발생 포인트는 15000
    현재 이용하실 수 있는 누적 포인트는 162500 점 입니다. 
'''

total_point = 12500
custom_name = input('고객 이름 : ')
price = int(input('결재 금액 : '))
point = price * 0.05
total_point += point

print('황지니 고객님의 사용금액은 {} 원, 발생 포인트는 {}\n\
현재 이용하실 수 있는 누적포인트는 {} 점 입니다'\
      .format(price, int(point), int(total_point)))

# 기본 출력
print(custom_name, '고객님의 사용금액은 ',price,'원, 발생 포인트는',int(point))
print("현재 이용하실 수 있는 누적포인트는 ", int(total_point),"점입니다.")

# format() 사용
print('{} 고객님의 사용금액은 {} 원, 발생포인트는 {}'.format(custom_name, price, int(point)))
print("현재 이용하실 수 있는 누적포인트는 {} 점 입니다.".format(int(total_point)))

# f-string 포매팅 사용 : print(f'출력문장 {변수명} 출력문장')
print(f'{custom_name} 고객님의 사용금액은 {price}원, 발생 포인트는 {int(point)}')
print(f'현재 이용하실 수 있는 누적포인트는 {int(total_point)} 점 입니다.')