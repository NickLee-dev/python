# path : function\\func_lambda.py
# module : function.func_lambda
# 파이썬에서 람다함수 만들어 사용하기
# 함수를 만들 것을 한줄로(간결하게) 표현가능하면 lambda사용
'''
리스트 내포(list in for), 간단 조건문처럼 한 줄로 간결하게 표현할 수 있는 새로운 함수 정의 방법
def 로 정의하는 함수를 lambda 로 간단하게 작성함
일회성 코드일 때 이용함
함수 이름 없음
참조변수가 함수명을 대신할 수는 있음 : 참조변수 = 람다식 => 사용시 참조변수(전달값)

작성방법과 사용법 :
작성 : 참조변수 = lambda 매개변수, *매개변수, 매개변수=기본값: 처리구문  <= 한줄 작성이 기본
사용 1 :
참조변수(전달값, 전달값)
사용 2 : 참조변수 없이 바로 사용
(lambda 매개변수 : 처리구문)(전달값)
'''

# 일반함수
def add(x,y):
    return x + y

# 람다함수
add2 = lambda x,y : x+y

if __name__ == '__main__':
    # 일반함수 사용
    result= add(2,3)
    print('결과 :',result) # 결과 : 5

    # 람다함수()
    result2 = add2(2,3)
    print('람다 확인 :',result2) # 람다 확인 : 5

    # 람다는 주로 작성과 실행을 한번에 함께 처리하는 방식으로 주로 사용됨
    print('더하기 결과 : ', (lambda x,y:x + y)(11,22)) # 더하기 결과 :  33

    # 람다함수의 매개변수에도 기본, 키워드, 가변매개변수 적용 할 수 있음
    print('(기본)더하기 결과 : ', (lambda x,y=20:x + y)(11)) # (기본)더하기 결과 :  31
    print('(키워드)더하기 결과 : ', (lambda x,y:x + y)(y=10,x=20)) # (키워드)더하기 결과 :  30
    print('(가변매개변수)더하기 결과 : ', (lambda x,*y:x * y)(3,1,2,3)) # (가변매개변수)더하기 결과 :  (1, 2, 3, 1, 2, 3, 1, 2, 3)

    # 람다함수 안에 간단 조건문(참일때 값 if 조건식 else 거짓일때 값) 사용할 수 있음
    print((lambda x,y : x if x%2==0 else y)(3,5)) # 5
