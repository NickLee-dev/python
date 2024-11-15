# path : loop/forSample.py or loop\\forSample.py
# module : loop.forSample
# 파이썬에서의 for 문 사용 테스트 스크립트
'''
for 문 작성형식 1 :
for 변수 in 리스트 | 튜플 | 딕셔너리 | 집합 | 문자열 : => 군집자료형을 넣어야됨
    반복 실행할 구문들 작성 (들여쓰기 중요)
주의사항 : in 오른쪽에는 값 하나(리터럴) 사용 못함
for 변수 in 값 :  => TypeError 발생함
'''
def test_for1():
    # list 사용
    for i in [10,20,30]:
        print(f'{i} 는 5의 배수이다.')

    # for k in 10 : # TypeError : 'int' object is not iterable
    #   print(k)

    # tuple 사용
    for t in (11, 22, 33):
        print(f'{t}는 짝수다.' if t % 2 == 0 else f'{t}는 홀수다.')

    # set 사용
    for s in {1, 2, 3, 4, 5, 6}:
        print(f'{s}의 제곱은 {s ** 2}')

    # str 사용
    for st in 'Python':
        print(f'{st} 문자의 유니코드는 {ord(st)} 이다.')

    # dict 사용 : 바로 사용시 key만 추출 가능
    for d in {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}:
        print(f'{d}')

    # 해결방법 : dict 는 따로 생성하고 사용함
    dict_1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
    for key in dict_1.keys():
        print(f'dict_1 {key} : {dict_1[key]}')

    for value in dict_1.values():
        print(f'value {value}')

'''
for 문 작성형식 2 : range() 함수 사용
range(시작, 끝값) 또는 range(시작값, 끝값, 간격) 또는 range(끝값)
시작값(이상, 값 포함), 생략되면 0 임
끝값(미만, 포함안됨), 반드시 표기
간격은 생략되면 기본 1임( 1씩증가 )

for 변수 in range(start, end): (콜론 표기 주의)
    변수를 사용한 반복 실행 구문 작성 (들여쓰기 주의)
'''

# 1부터 100까지 정수들의 합계 구해서 출력
def for_sum():
    sum = 0
    for n in range(1, 101):
        print(n, '+', end="")
        sum += n
    print()  # 줄바꿈 처리
    print(f'합계 : {sum}')

#-------------------------------------------------------------------------------------------------------------
# import collections.iterable   # deprecated : 버전 업 하면서 사용 중지됨
import collections.abc

def test_iterable():
    nlist = [1, 2, 3, 4, 5, 6]
    # iterable object : 리스트처럼 순차적으로 값을 나열해서 저장한 객체를 말함
    # isinstance() 함수 : 객체의 종류를 확인할 때 사용함(자바의 instanceOf 연산자와 같음)
    print(isinstance(nlist, collections.abc.Iterable)) # Iterable 은  첫글자가 대문자임

def test_range():
    print(range(10)) # range(0, 10, 1)

    lst=list(range(10))
    print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for 문 작성형식 3 : range(len(군집자료형변수)) -> 연속된 값을 인덱스로 처리
def for_indexing():
    # 리스트에 저장된 아이템 추출
    list1 = ['apple', 90, [1,2,3],('A','B','C')]
    for item in list1:
        print(item)

    # 리슽의 저장 아이템을 인덱스를 이용하여 연속 처리 한다면
    for idx in range(len(list1)): # len(list1) :4 => range(4) => range(0,4) : 0,1,2,3 숫자 발생함
        print(list1[idx])

# 키보드로 구구단의 단수를 입력 받아서, 해당 구간의 구구단 출력
def print_gugudan():
    a = int(input('구구단 단수 입력 : '))

    for i in range(1,10):
        print (f'{a} * {i} = {a*i}')

# for 문 안에 for문 사용
# 구구단 2단부터 9단까지  출력 처리

def doubleFor():
    for i in range(2,10):
        for j in range(1,10):
            print(f'{i} * {j} = {i * j}')
        print('--------------------------------------')

# list | tuple | set 안에 list, tuple, set 이 저장된 경우
# 첫번쨰 추출은 리스트(튜플, 셋) 안의 아이템이(리스트, 튜플, 셋) 추출임
# 꺼낸 아이템이 리스트(튜플)일 경우, 해당 아이템 안의 값들을 하나씩 추출하려면
# 이중 for 문 사용이 필요함

# 리스트 안의 아이템 안의 값의 갯수가 동일할 경우에는 단순 for문으로 해결 가능함
def list_in_list():
    fruit_list = [['apple',10,800],['banana',3,2500],['orange',15,500]]
    for fname,famount,fprice in fruit_list:
        print(f'{fname} 의 단가는 {fprice}원이고, 구매 수량은{famount}개,, 구매가격 {famount*fprice}원')

# 리스트 안의 아이템 안의 값 갯수가 제각각인 경우
# 아이템 안의 각 값들을 처리하려면 이중 for문 사용함
def list_in_list2():
    nlist=[['a','bb','cde'],[10,20],[1.2,3.4,33,89.90]]
    for item in nlist:
        print(item)
        for data in item:
            print(data)
        print('----------------------------------')

# 위의 리스트 처리를 인덱스 방식으로 바꾼다면
def list_in_list3():
    nlist=[['a','bb','cde'],[10,20],[1.2,3.4,33,89.90]]
    for index in range(len(nlist)):
        print(nlist[index])
        for jindex in range(len(nlist[index])):
            print(nlist[index][jindex])
        print('----------------------------------')
