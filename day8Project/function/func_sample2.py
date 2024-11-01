# path : function/func_sample2.py
# module : function.func_sample2
# 파이썬의 함수 정의(definition, 만들기)와 함수 호출(call, 사용) 연습 스크립트

def tmax(a, b):
    '두 개의 값을 전달 받아서 둘 중 큰 값을 리턴하는 함수이다.'
    print(f'a: {a}, b: {b}, type: {type(a)}, type: {type(b)}')
    if a > b:
        return a
    else:
        return b
def func_param_args():
    '매개변수와 전달인자 갯수 일치 테스트용 함수이다.'
    result = tmax(10,20)
    print(f'큰값 : {result}')
    print(f'큰값 : {tmax(44.5,23.4)}')
    print(f'큰값 : {tmax('M','m')}')
    # result2 = tmax(120) # 전달값과 매개변수 갯수다름 # TypeError: tmax() missing 1 required positional argument: 'b'
    # result2 = tmax(10,20,30) # 전달값과 매개변수 갯수다름 # TypeError: tmax() takes 2 positional arguments but 3 were given
#---------------------------------------------------------------------------------------------------------
def tmax2(a,b): # call by value(값을 전달받는 방식)
    '두 개의 값을 전달받아서, 둘 중 큰값 리턴하는 함수이다.'
    print(f'a: {a}, b: {b}, type: {type(a)}, type: {type(b)}')
    max_value = 0
    if a > b :
        max_value = a
    else:
        max_value = b

    a = 100 # 매개변수의 값을 변경하는 것으로 작성된 구문임
    b = 200 # 지역변수 새로운 할당임 => 함수 밖의 변수에 영향을 안 줌
    return max_value

def func_callByValue():
    '함수로 값 전달 방식 테스트용 함수'
    num1 = 10
    num2 = 20
    print(f'num1:{num1},num2:{num2}')
    result=tmax2(num1,num2) # 변수가 가진 값 전달함 : call by value 임
    print(f'큰값 : {result}')
    # 함수 쪽에서 변경한 값이 호출부의 변수에 영향이 있는지 확인
    print(f'num1:{num1},num2:{num2}')
#------------------------------------------------------------------------------------------
# 파이썬에서는 군집자료형을 전달받는 매개변수는 주소를 받는다.
def list_in_max(plist):
    '리스트 객체를 전달받아서, 리스트 안의 값들 중 가장 큰 값을 찾아내서 리턴하는 함수'
    print(f'plist: {plist},주소 : {id(plist)}')
    max_value = plist[0]  # q비교의 시작값 지정
    for item in plist:
        if max_value < item:
            max_value = item
    # 전달 받은 주소위치의 각 요소의 값들을 변경 처리해 봄
    plist[0] = 100
    return max_value

def func_callByAddress():
    '함수쪽으로 주소 전달 테스트용 함수.'
    nlist = [4,1234,325,343,2,4,56,7,8,856,5,67]
    print(f'nlist: {nlist}, 주소 : {id(nlist)}')
    result=list_in_max(nlist) #  nlist 의 주소가 전달됨 : call by address
    print(f'가장 큰 값 : {result}')
    print(f'nlist : {nlist}')

# ------------------------------------------------------------------------------
# 기본 매개변수 : 기본값(default)을 가진 매개변수
# 함수 만들때 매개변수에 기본값을 지정할 수 있음
# def 함수명(매개변수=기본값,매개변수=기본값):
# 주의 : 매개변수 일부만 기본값을 지정할 경우, 뒤쪽 매개변수부터 기본값 지정해야 함
#       즉, def 함수명(매개변수, 매개변수=기본값, 매개변수= 기본값):   # 정상구동
#           def 함수명(매개변수=기본값, 매개변수, 매개변수):   # error 출력
#           def 함수명(매개변수,매개변수=기본값,매개변수): # error 출력

# 해당 함수 실행시 기본 매개변수에 전달값은 생략 할 수 있음
# 전달값이 없으면 준비된 기본값을 사용하게 됨
# def tmin(a,b,c=0):
# def tmin(a,b=0,c=0):
def tmin(a=0,b=0,c=0):
    '3개의 값을 전달받아서, 가장 작은 값을 찾아서 리턴함'
    print(f'a: {a}, b: {b}, c: {c}')
    min_value = a
    if a < b and a < c:
        min_value = a
    elif b < c:
        min_value = b
    else :
        min_value = c

    return min_value

def func_default_params():
    '사용할 함수의 기본값 있는 매개변수 사용 테스트용'
    print(f'가장 작은 값 : {tmin(12,3, 20)}')
    print(f'가장 작은 값 : {tmin(12,3)}')  # c값은 생략되었으므로 기본값이 들어감
    print(f'가장 작은 값 : {tmin(12)}') # b,c의 값은 매개변수 생략으로 기본값이 들어감
    print(f'가장 작은 값 : {tmin()}') # a,b,c의 값은 매개변수 생략으로 기본값이 들어감

#-------------------------------------------------------------------------------------------
# 키워드 매개변수
# 함수 사용할 때 (함수 호출시) 매개변수 = 전달값 의 형태로 사용하는 경우를 말함
# 함수명(전달값, 전달값) => 매개변수에게 전달할 순서가 중요함, 순서대로 전달됨
# 함수명(매개변수=전달값, 매개변수=전달값) => 매개변수 순서와 상관없이 사용가능함
def num_calc(a,b,c,d,e):
    return a + b - c * d / e

def func_keyword_param():
    '전달값을 매개변수명을 지정해서 전달하는 함수 사용 테스트용.'
    result = num_calc(10,9,8,7,6) # 10+9-8*7/6
    # 매개변수 순서대로 갯수 맞춰서 값이 전달됨
    print(f'result : {result}')
    # 매개변수 명을 지정해서 값 전달 실행 시킬수도 있음 : 키워드 매개변수 사용임
    result= num_calc(c=8,b=9,a=10,e=6,d=7)
    print(f'result : {result}')

# 함수 실행
if __name__ == '__main__':
    # func_param_args()
    # func_callByValue()
    # func_callByAddress()
    # func_default_params()
    func_keyword_param()

# 여러 데이터를 취급시 call by address를 활용
