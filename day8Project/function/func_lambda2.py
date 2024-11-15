# path : function/func_lambda2.py
# module : function.func_lambda2
# 람다함수를 이용하는 파이썬 내장함수 사용 테스트

# map 내장함수
# 맵객체변수 = map(실행할 함수명, 시퀀스객체)
# 시퀀스(Sequence) 객체 : 값을 순차적으로 저장하는 객체, 리스트나 튜플이 해당됨 (인덱스를 사용하는 객체)
# 시퀀스 객체의 각 요소값을 하나씩 꺼내서 함수로 보내고, 처리결과를 리턴 받아서 맵 객체에 저장
def func(x):
    return x*x

def test_map():
    lst = [1,2,3,4,5]
    m = map(func,lst)
    print(m,type(m)) # 맵 참조변수 출력 : 참조객체 타입과 16진수 주소(id)가 출력됨
    # <map object at 0x000001A4C300E3E0> <class 'map'>
    print(list(m)) # 맵 참조변수가 가진 값들을 리스트로 만들어서 출력
    # [1, 4, 9, 16, 25]

    # 함수명 대신에 람다함수로 작성을 바꾼다면
    m = map((lambda x: x*x),lst)
    print(list(m))
    # [1, 4, 9, 16, 25]

    # 람다는 코드를 간결하게 표현하는게 목적임
    # 위의 코드를 한줄로 표현한다면
    print(list(map((lambda x: x*x),[1,2,3,4,5])))
    # [1, 4, 9, 16, 25]

# ----------------------------------------------------------------------
# filter 내장 함수 :
# 필터결과객체 = filter(실행할 함수명, 시퀀스 객체)
# 시퀀스 객체가 가진 각 요소(인덱스, 순번)의 값에 대해 함수 처리 결과가 참(True)인 요소만 골라서 저장하는 함수

def func1(x):
    return x>2

def test_filter():
    nlist = [1, -2, 4, 7]
    f = filter(func1, nlist)
    print(f,type(f)) # <filter object at 0x000001F4F6A5E5F0> <class 'filter'>
    print(list(f)) # [4, 7]
    # 람다 활용 한줄 표현식
    print(list(filter((lambda x: x>2),[1,-2,4,7]))) # [4, 7]

# ------------------------------------------------------------------------------------
# sorted 내장함수 : 정렬 함수
# 시퀀스에 저장된 복잡한 객체를 정렬할 때 사용하는 함수
# 정렬객체변수 = sorted(정렬할 시퀀스 객체, key=정렬에 사용할 키, reverse=True(내림차순) | reverse=False(기본,오름차순))
# 키 지정시에 파이썬이 제공하는 operator 모듀을 이용할 수 있음
import operator

def test_sorted():
    student = [('김영희', 'A', 95),('홍철수','B',86),('이길동','C',70)] # 객체 생성
    print(student) # [('김영희', 'A', 95), ('홍철수', 'B', 86), ('이길동', 'C', 70)]

    print(sorted(student)) # 키 지정 누락시 자동으로 각요소의 [0]가 키로 지정됨
    # [('김영희', 'A', 95), ('이길동', 'C', 70), ('홍철수', 'B', 86)]
    print(sorted(student,key = lambda x: x[1])) # 각 아이템(튜플)의 [1]번째가 정렬의 키가 됨
    # [('김영희', 'A', 95), ('홍철수', 'B', 86), ('이길동', 'C', 70)]
    print(sorted(student,key = lambda x: x[2])) # 각 아이템(튜플)의 [2]번째가 정렬의 키가 됨
    # [('이길동', 'C', 70), ('홍철수', 'B', 86), ('김영희', 'A', 95)]
    print(sorted(student, key = operator.itemgetter(2))) # 각 아이템(튜플)의 [2]번째가 정렬의 키가 됨
    # [('이길동', 'C', 70), ('홍철수', 'B', 86), ('김영희', 'A', 95)]
    #내림차순 정렬 : reverse=True 로 지정함
    print(sorted(student,key = operator.itemgetter(2), reverse=True)) # 점수 기준 내림차순 정렬됨
    # [('김영희', 'A', 95), ('홍철수', 'B', 86), ('이길동', 'C', 70)]

#--------------------------------------------------------------------------------------
# 리스트 내포와 람다함수
# 예 : 구구단 2단부터 9단까지 곱하기한 결과만 리스트에 저장 처리한다면
def list_lambda():
    print([dan*su for dan in range(2,10) for su in range(1,10)]) # 리스트 내포
    print([(lambda d,s:f'{d}*{s}={d*s}')(dan,su) for dan in range(2,10) for su in range(1,10)])


if __name__ == '__main__':
    #test_map()
    #test_filter()
    #test_sorted()
    list_lambda()