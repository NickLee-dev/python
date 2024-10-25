# chap04_tuple.py
# 튜플(tuple) 자료형 : 리스트와 저장 방식은 같음
# 여러 종류의 데이터들을 순차적으로 저장하는 집합자료형임
# 리스트와 다른점은 저장된 앨리먼트를 변경할 수 없음 => 상수 개념이 적용됨, 연산 속도가 빠름

# 튜플 정의 방법
# 1. 소괄호 () 로 정의
tp_1=()
print(tp_1,type(tp_1))

# 2. tuple() 함수 사용
tp_2 = tuple()
print(tp_2,type(tp_2))

# 튜플도 리스트와 같이 인덱싱, 슬라이싱 연산 가능함
lst = [10, 20, 30]
tpl = (11, 22, 33)
print(lst,type(lst))
print(tpl,type(tpl))

print('0번째 값 : {}, {}'.format(lst[0], tpl[0]))
print('0번째부터 1번째까지의 값들 : {}, {} : '.format(lst[0:2],tpl[0:2]))
print('0번째부터 1번째까지의 값들 : {}, {} : '.format(lst[:2],tpl[:2]))
print('리스트 합치기 : {}'.format(lst+lst))
print('튜플 합치기 : {}'.format(tpl+tpl))

# 튜플과 리스트의 차이점 : 튜플은 값 변경 못함
lst[2] = 99
print(lst)
# tpl[3] = 15 # TypeError: 'tuple' object does not support item assignment

# 주의사항 :
# 튜플 생성시에 1개의 데이터만 저장 할 때는 반드시 값 뒤에 콤마(,) 붙일것

tp_3 = (10) # int
print(tp_3,type(tp_3))  # 확인
tp_3 = (10.5) # float
print(tp_3,type(tp_3))  # 확인
tp_3 = (10,) # int
print(tp_3,type(tp_3))  # 확인

# 튜플 생성시 저장 데이터가 1개 일 때는 소괄호 생략해도됨
tp_4 = 10,
print(tp_4,type(tp_4))

# 튜플 내장함수
# count() : 찾는 값의 갯수 조회
# 튜플변수.count(찾는값)
number_count = tpl.count(11)
print('tpl에 저장된 11의 갯수 : {}'.format(number_count)) # tpl에 저장된 11의 갯수 : 1

# index() : 찾는 값의 인덱스(순번) 조회
# 튜플변수.index(찾는값)
# 찾는값이 없으면 error => find() 사용하면 됨
find_index = tpl.index(33)
print('tpl에 저장된 33의 위치 : {}'.format(find_index)) # tpl에 저장된 33의 위치 : 2
# print('tpl에 저장된 33의 위치 : {}'.format(tpl.index(55))) # ValueError: tuple.index(x): x not in tuple

# len(튜플변수) : 튜플에 저장된 엘리먼트의 갯수 리턴
print('tpl에 저장된 데이터 갯수 : {}'.format(len(tpl)))  # tpl에 저장된 데이터 갯수 : 3

# 참고사항 : () 없이 하나의 변수에 값 나열 대입하면 자동 튜플이 됨
x = 1,2,3
print(x,type(x)) # (1, 2, 3) <class 'tuple'>

# 참고사항 :
# 프로그래밍 언어의 원칙 : return 문은 한개만 반환 할 수 있음(값 또는 주소)
# return 값; 또는 return 레퍼런스변수; 또는 return 변수;
# 파이썬에서는 여러개의 값을 리턴할 수 있음 => 자동 튜플이 됨
# return 값,값,값 또는 return (값,값,값)

# 샘플 함수 정의-----------------------------------------
def f_test():
    return (3,5)
def f_test2():
    return 1,2,3

# 함수 사용(호출, call)----------------------------------
# 함수가 리턴하는 값이 여러 개인 경우에는 반드시 값 받아줄 변수도 갯수 맞춰서 준비함
x,y = f_test()  # x,y에 3,5 각각대입
print(f_test())  # (3, 5)
print(x,type(x)) # 3 <class 'int'>
print(y,type(y)) # 5 <class 'int'>

# 여러개의 값을 리턴하는 함수 실행시, 변수 한개가 반환값들을 받으면 자동 튜플이 됨
z = f_test2()
print(z,type(z)) # (1, 2, 3) <class 'tuple'>