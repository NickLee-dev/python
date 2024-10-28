# path : conditional\\ifSample.py or conditional/ifSample.py
# module : conditional.ifSample

# 제어문 : 조건문
# if문, if else 문, if elif ... else 문 사용 테스트 스크립트

'''
제어문의 종류 : 조건문, 반복문, 분기문
조건문 : 조건을 제시해서 결과가 참(True) 또는 거짓(False)이 나오게끔 작성해서
        결과에 따라 처리 내용을 선택 작동되게 하는 구문
        if문, if else문, if elif ... else 문
반복문 : loop(루프, 반복되는 구간)가 있는 문장, 루프문이라고 함
        반복 실행할 구문을 원하는 횟수 만큼 또는 종료 조건이 될 때까지 반복 실행 되게 작성
        for문, while문
분기문 : 실행 순서를 중간 생략하거나 강제로 종료 시키는 구문(break, continue)
        반복문 내에서만 사용할 수 있음
        continue 문, break 문
'''

# 조건문에서는 조건 표현식(expression) 작성이 중요함
# 조건 표현식은 반드시 결과가 참 또는 거짓이 나오게끔 작성해야함
# 비교, 논리 연산자 주로 사용됨
'''
if 조건식 : 
    조건이의 결과가 참일 때 실행할 구문들 (반드시 들여쓰기함)
    구문은 최소 1개는 작성해야 함
'''
# 조건문 작성형식 1 : if만 사용한 경우
# 입력받은 정수 숫자가 1이냐?
def test_if():
    num = int(input('정수 숫자 입력 : '))
    if num ==1:
        print('num : ', num)

# 정수를 입력 받아서 짝수인지 확인
# 짝수 : 2의 배수, 2로 나눈 나머지 값이 0인 수
# 홀수 : 2의 배수가 아닌수, 2로 나눈 나머지 값이 1인 수
def test_even():
    num = int(input('정수 숫자 입력 : '))
    if num % 2 == 0:
        print(f'{num} is even')

# 조건문 작성형식 2 : if else 문
'''
if 조건식 : 
    참일 때 실행할 구문들 1개 이상
else :
    거짓일 때 실행할 구문들 1개 이상
'''
def test_even2():
    num = int(input('정수 숫자 입력 : '))
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')

# 정수를 하나 입력 받아서, 1부터 100 사이의 값이면 입력값의 제곱을 출력헉ㅎ
# 해당 범위의 값이 아니면, '1 ~ 100 사이의 값만 입력하세요.' 출력처리
def test_range():
    num = int(input('정수 숫자 입력 : '))
    if (num >= 1  and num <= 100):
        print(f'{num} 의 제곱은 {num **2}')
        print(f'{num} 의 제곱은 {pow(num,2)}')
    else:
        print(f'1 ~ 100 사이의 값만 입력하세요.')

# in 연산자 : 군집 자료형(list, tuple, set, dict, str) 에 사용함
# 변수 또는 값 in 군집자료형변수 : x in s => s 안에 x가  있느냐? => x가 있으면 True, 없으면 False 리턴
# x not in s => s 안에 x 가 없느냐 => x 가 없으면 True, 있으면 False 리턴

def test_in():
    print(2 in [1,2,3,4,5,6]) # True
    print(2 not in[1,2,3,4,5,6]) # False
    print('a' in 'abcdef') # True
    print('a' not in 'abcdef') # False

# 결제 수단중에 'money' 가 있으면, '5000원을 현금 지불하였습니다.' 출력하고
# 없으면 '다른 결제 수단을 선택하세요.' 출력
def checkPayment():
    payment = ['card','money','mobile']
    price = 5000

    if 'money' in payment:
        print(f'{price}원을 현금 지불 하였습니다.')
    else :
        print('다른 결재 수단을 선택하세요.')

# 조건문 작성형식 3 : 다중if문
# if... elif... elif... elif... else
# if... elif... elif... elif...
def checkPayment2():
    payment = ['결제수단','card','money','mobile','zeropay']
    print('===========결재 수단 선택=============')
    print('1. 카드')
    print('2. 현금')
    print('3. 모바일')
    print('4. 제로페이')

    no = int(input('결제 수단 선택 : '))
    price = int(input('결제 할 금액 : '))

    if no == 1:
        print(f'{price} 원을 {payment[1]} 로 지불 하였습니다.')
    elif no == 2:
        print(f'{price} 원을 {payment[2]} 로 지불 하였습니다.')
    elif no == 3:
        print(f'{price} 원을 {payment[3]} 로 지불 하였습니다.')
    elif no == 4:
        print(f'{price} 원을 {payment[4]} 로 지불 하였습니다.')
    else :
        print('다른 결재 수단을 선택하세요.')

# 간단 if문
# 변수 = 참일때 실행 값 if 조건식 else 거짓일 때 실행할 값
def shortCondition():
    a = 1
    message = 'a is 1' if a == 1 else 'a is not 1'
    print(message)

def shortCondition2():
    score = int(input('점수 : '))
    message = '합격' if score >= 60 else '불합격'
    print(message)