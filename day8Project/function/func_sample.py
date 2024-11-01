# path : function\\func_sample.py   or   function/func_sample.py
# module : function.func_sample
# 파이썬에서 함수 만들어 사용하기 테스트 스크립트

'''
함수란, 반복 사용되는 소스 코드를 별도로 분리 작성해서 이름 붙인 것
- 파이썬 함수 만들기
def 함수명(매개변수):   => 매겨변수 : 0 ~ n개
    "함수에 대한 설명 문구"  => help(함수명) : 함수에 대한 설명 문구 확인할 수 있음
    함수가 실행할 코드 구문들

- 함수의 사용 : 함수 호출(function call) 이라고 함
    함수가 만들어진 형태(signature)에 맞춰서 사용해야 함
    => 함수이름 틀리지 않아야 함 (대소문자 주의, _갯수 확인)
    => 매개변수의 갯수는 일치되게 전달인자 (argument) 사용해야 함
    => 반환값 여부도 확인 => 반환값 있는 함수는 함수(반환값 있는 함수 중첩사용())
        [반환값 받을 변수 =] 함수명()
'''

# 아무런 기능이 없는 (처리할 코드가 준비중인) 빈 함수를 만들때는 pass 사용함
def func():
    pass

# 함수 이름 아래에 함수 설명(description)을 적어둘 수 있음. 따옴표를 사용함
def hello():
    '이 함수는 함수 작성 연습용입니다.'
    print('Welcome!!',end=' ')
    print('함수명에 공백, 예약어 사용 못함, 대소문자 구분함, _ 만 허용함, 숫자로 시작불가')
    return # 반환값 없는 return은 생략 가능

# 매개변수 있고, 반환값 있는 함수 작성
def add(x,y):
    print(f'x : {x}, y : {y}')
    return x + y

# 파이썬에서는 여러 개의 값을 리턴할 수 있음, 자동으로 tuple 로 반환됨
def func2(x,y):
    print(f'x : {x}, y : {y}')
    return x * 2 , y * 2

# 변수 생성과 사용 영역 (지역, 스코프 : scope)
# 지역 변수 (Local Variable), 전역 변수 (Global Variable)
def func1():
    num=10    # 함수 안에서 만들어진 변수 : 지역변수
    print(f'num : {num}')

# 함수 밖에서 지역변수 사용 못함
# print(f'num : {num}')  # NameError: name 'num' is not defined. Did you mean: 'sum'?

# 파이썬에서의 전역변수 : 함수 밖에서 만든 변수
gnum = 100  # 전역변수 : 변수 만든 위치 아래에서 어디서나 사용 가능함
print(f'gnum : {gnum}')

def func_global():
    global gnum # 전역변수 gnum을 사용한다는 선언임
    print(f'gnum : {gnum}')
    # 파이썬에서는 변수 = 값 구문은 새로운 변수 할당(생성)임
    gnum = 200 # 새로운 생성이 아니고, 기존의 전역변수의 값을 변경하고자 한다면, 바로 위에 global 을 사용함
    print(f'gnum : {gnum}')

# 함수의 매개변수(parameter) 는 전달받은 값을 변경할 수 없다.
# 전달 받은 인자가 군집 자료형일 때는 아이템(요소)은 변경 할 수 있음
# 전달인자가 군집자료형은 매개변수로 주소(메모리에 할당된 위치정보)를 할당함
def list_func(plist):
    print(f'plist 가 받은 주소 : {id(plist)}')
    print('before : ',plist)
    plist[1] = 10  # 아이템은 변경 가능함
    print('after : ',plist)


# 함수 실행
if __name__ == '__main__':
    hello()
    '''
    Welcome!!
    함수명에 공백, 예약어 사용 못함, 대소문자 구분함, _ 만 허용함, 숫자로 시작불가
    '''
    help(hello)
    '''
    hello()
    이 함수는 함수 작성 연습용입니다.
    '''
    help(print)

    #  반환값 있고 매개변수 있는 함수 실행(사용, call)
    # 반환값 받는 변수 = 함수명(매개변수에게 줄 값)

    result = add(10,20)
    print(f'result : {result}')

    result2 = add(1.3,4.6)
    print('result2 : {}%0.3f'%result2)

    result3 = func2(11, 22)
    print(result3, type(result3))

    # 반환값을 각각의 변수가 받을 수도 있음
    n1, n2 = func2(3.3, 4.4)
    print(n1,type(n1),n2,type(n2),sep='\n')

    # 반환값을 일부만 받고자 한다면
    k, _ = func2(3,4)
    print(k,type(k))
    print(_,type(_)) # 파이썬에서는 _ 는 값을 받지 않겟다는 의미로 통상 사용

    # 지역변수
    func1()

    # 전역변수
    func_global()
    print(gnum)

    # 군집자료형
    lst = [1,2,3,4,5]
    print ('lst 가 가진 리스트의 주소 : ',id(lst))
    print(lst)
    list_func(lst)  # 군집 자료형은 주소전달 방식임
    print(lst)