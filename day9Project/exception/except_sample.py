# path : exception\\except_sample.py
# module : exception.except_sample
# 파이썬에서의 예외 처리
'''
예외 : 소스 코드로 해결할 수 있는 에러
에러의 종류 :
    - 시스템 에러 : 소스 코드로 해결 못하는 에러
        메모리부족, 하드디스크(저장처리) 용량 부족, 베터리 전원 부족 등
    - 구문(문법) 에러 : 구문을 잘못 작성한 경우의 에러
        개발툴(IDE) 에서 자동 검사함, 구문 수정해서 해결함
    - 런타임 에러 : 실행시 발생하는 에러
        에러 발생이 확인되면 코드를 수정해서 해결함 => 예외처리함

예외 처리 방법 :
    if 조건문으로 에러 상황을 예측해서 미리 조치함
    => 예외 상황을 처리하는 별도의 구문이 있음 : 예외처리 구문을 사용하도록 함
'''

def test_error():
    '에러 발생 테스트용 함수'
    # print('test_error'  # SyntaxError: '(' was never closed

    # a = 10
    # b = 0
    # c = a/b # ZeroDivisionError: division by zero

    # 4 + new * 3 # NameError: name 'new' is not defined

    # lst = [1,2]
    # print(lst[2])  # IndexError: list index out of range

    # dct = {'a':100,'b':200}
    # print(dct['c'])   # KeyError: 'c'
    pass
#-------------------------------------------------------------------------------------
# 런타임 에러 중에 사용자가 입력값을 잘못 입력하는 경우
def test_input_error():
    '입력 오류 관련 에러테스트 함수'
    # num = int(input('정수를 입력하세요 : '))  # ValueError: invalid literal for int() with base 10: '11.1'

    # 해결방법 1 : 조건문으로 해결
    num = input('정수를 입력하세요.')
    if num.isdecimal():  # 10진 정수가 맞는지?
        num = int(num)
        print(num,type(num))
    else:
        print("정수만 입력하세요.")

# 예외 처리 방법 :
'''
try :
    에러 발생 가능성이 있는 구문 (일반구문 포함 가능)
except :
    에러가 발생했을 때 실행될 구문들
'''
def test_input_error2():
    num = input('정수를 입력하세요 : ')
    try:
        num = int(num)    # 에러 발생 가능성이 있는 문장
        print(num,type(num))
    except:
        print('정수만 입력해야 합니다.')

# ---------------------------------------------------------------
# 예외처리시 except: 에 pass를 사용하면
# 오류발생시 프로그램이 멈추지 않고 계속 동작되게 할 수 있음
def except_pass():
    'except 에 pass 사용 테스트 함수'
    lst =['3','예외처리',4,2,65.4,'python']
    digit_num = []
    print(lst)

    # lst에서 숫자만 돌라내서 digit_num에 기록처리
    for index in range(len(lst)):
        try:
            digit_num.append(int(lst[index]))  # 에러가 발생되는 구문임
        except:
            pass

    print(digit_num) # [3, 4, 2, 65]

def except_pass2():
    'except 에 pass 사용과 if 조건문 사용 비교 테스트 함수'
    lst =['3','예외처리',4,2,65.4,'python']
    digit_num = []
    print(lst)

    # lst에서 숫자만 돌라내서 digit_num에 기록처리
    for item in lst:
        print(item,type(item))
        if str(item).isdigit(): # is...() 함수는 문자형 값에 사용하는 함수임/변환한 item의 숫자인지 물어봄
            digit_num.append(int(item))  # 에러가 발생되는 구문임

    print(digit_num) # [3, 4, 2]

#-------------------------------------------------------------------
# finaly : 예외발생과 상관없이 반드시 실행할 구문을 작성하는 영역임
import math         # 수학 계신관련 함수들을 제공하는 모듈임

def test_finally():
    'finally 구문 사용 테스트 함수'
    try:
        radius = float(input('반지름 : '))      # 에러가 발생 가능
    except:  # 에러가 발생하면 실행
        print('숫자만 입력해야 합니다.')
    else: # 에러가 발생하지 않으면 실행
        print('반지름 : ',radius)
        print('원면적 : ',math.pi*math.pow(radius,2))
        print('원둘레 : ', 2 * math.pi*radius)
    finally: # 반드시 실행
        print('예외처리 구문 종료함')

# 파이썬에서 예외처리 구문 조합 형태
'''
try: ~ except: ~
try: ~ except: ~ else: ~
trt: ~ except: finally: ~
try: ~ except: exlse: ~ finally: ~
try: ~ finally:

주의 : try: ~ else: ~  ( 에러)
'''
# def test_except():
#     'try: ~ else: ~ 잘못 사용된 경우의 테스트 함수'
#     try: # SyntaxError: expected 'except' or 'finally' block
#         print('try area...')
#     else:
#         print('else area...')

# -----------------------------------------------------------

# try 쪽에서 여러 종류의 에러가 발생할 경우
# except: 구문을 여러개 작성할 수 있다(사용 갯수에 제한 없음)
# except 에러종류이름:  또는    except 에러클래스명 as 변수명:
# 에러 클래스의 계층구조에 따라 하위 클래스를 먼저 작성할 것(자바의 상속 구조 처리와 같음 / 상속구조 후손부터)
def multi_except():
    '다중 except 사용 테스트 함수'
    try:
        # print(3/0) # 0으로 나눌 수 없습니다.
        lst=[]
        # print(lst[0]) # 리스트 인덱스 잘못 사용됨
        # lst.append(int(input('숫자 입력 : ')))  # 에러 발생함
        print(lst)
        # print('2'+4)  # 계산식 오류
    except ZeroDivisionError:
        print('0으로 나눌 수 없습니다.')
    except IndexError:
        print('리스트 인덱스 잘못 사용됨')
    except TypeError:
        print('계산식 오류')
    except Exception as e:
        print('에러 발생함')
        print(e)

# 예외를 강제로 발생시키기 --------------------------------------------------
# raise 예외클래스명 또는 raise 예외클래스명('에러메세지')
# 주로 함수나 클래스의 메소드 작성시에 이용함
# 코드상 지정하는 조건일 때 에러 발생시키고, 해당 함수를 사용해서 예외처리함

def ndiv(a,b) :
    if b==0 :
        raise Exception('0 나누기 못 함')
    else:
        return a/b

# 위에 정의된 함수를 사용할 때 예외처리함
def test_ndiv():
    '예외 발생 구문이 있는 함수 사용 테스트'
    try:
        # 예외발생 구문을 가진 함수 사용
        result = ndiv(4,2) #
        result = ndiv(4,0) # 0 나누기 못 함
        print(result)
    except Exception as e:
        print(e)



if __name__ == '__main__':
   # test_error()
   # test_input_error()
   # test_input_error2()
   # except_pass()
   # except_pass2()
   # test_finally()
   # test_except()
   # multi_except()
   test_ndiv()
   pass