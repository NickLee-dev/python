# 경로(path) 표현
# test_bool\\operator_sample.py
# test_bool/operator_sample.py
# 모듈(module) 표현
# test_bool.operator

# bool 자료형 확인
def func_bool():
    flag = True
    print("flag : ",flag,type(flag)) # True <class 'bool'>

    flag = False
    print("flag : ",flag,type(flag)) # False <class 'bool'>

    # 파이썬에서는 대소문자 구분함
    # flag = true # NameError: name 'true' is not defined. Did you mean: 'True'?

    # bool() 함수 사용 : 값의 논리상태를 확인할 때 사용함
    print('result1 : ',bool('abcd')) # result1 :  True
    print('result2 : ',bool('')) # result2 :  False

    # 0을 제외한 모든 숫자는 참(True)임
    print('result3 : ',bool(1)) # result3 :  True
    print('result4 : ',bool(0)) # result4 :  False

    # 값이 저장되어 있는지, 비어 있는지 확인하는 용도로 bool() 함수 사용함
    print('result5 : ',bool({'a':1,'b':2})) # result5 :  True
    print('result6 : ',bool({})) # result6 :  False
    print('result7 : ',bool(dict())) # result7 :  False
    print('result8 : ',bool([1,3,2,4])) # result8 :  True
    print('result9 : ',bool([])) # result9 :  False
    print('result10 : ',bool((1,3,2,4))) # result10 :  True
    print('result11 : ',bool(())) # result11 :  False

# 비교(관계) 연산자
# 2개의 값을 가지고 크냐(>, 촤과), 작으냐(<, 미만), 크거나 같으냐(>=, 이상), 작거나 같으냐(<=, 이하)
# 같으냐(==), 같지 않느냐(!=)
# 이항 연산자 : 값1 연산자 값2 / 값을 두개를 가지고 비교
def func_compare():
    print('1==1 : ', 1==1) # 1==1 :  True
    print('1==2 : ', 1==2) # 1==2 :  False
    print('1>0 : ', 1>0) # 1>0 :  True
    print('1<0 : ', 1<0) # 1<0 :  False
    print('1>=1 : ', 1>=1) # 1>=1 :  True
    print('1!=0 : ', 1!=0) # 1!=1 :  True

def func_logical():
    # 논리 연산자 : 논리값(True, False)을 계산에 사용하는 연산자
    # and, or, not
    a = 1
    b = 2
    print(a>0 and b>1) # True
    print(a==0 or b!=1) # True

    # and 연산자의 특징 :
    # 앞 and 뒤 : 앞이 False 이면 뒤를 실행 안함
    # 앞이 True 이면 뒤를 실행함
    # 이 성질을 이용하는 짧은 조건문이 있음(모든 스크립트에서 사용 가능)
    print('a' and 'b') # b
    print('' and 'b') # '' 출력(안보임)

    # or 연산자의 특징 :
    # 앞 or 뒤 : 앞이 False 이면 뒤를 실행함
    # 앞이 True 이면 뒤를 실행 안 함
    print('a' or 'b') # a