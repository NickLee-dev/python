# test_dict\\dict_sample.py
# 모듈로 표현한다면 : test_dict.dict_sample
# 모듈(module) : 함수들을 따로 모아서 저장해 놓은 소스 파일
# 모듈은 사용 : 다른 파일에서 필요시 import 해서 사용함

# 사전(dict) 자료형
# 자바의 Map 과 같은 구조로 key와 value 를 쌍으로 저장하는 집합자료형임
# dict 에서 key는 변경되지 않는 값이어야 함 (키는 지정하면 변경할 수 없음) => 키에 튜플을 사용할 수 있음
# dict 에 저장하는 value는 모든 자료형 데이터 가능함
# json, xml 로 변환할 때 많이 사용됨

# dict 정의방법
def test1():
    # 방법 1 : dict() 함수
    dict1 = dict()
    print(dict1, type(dict1))
    # 방법2 : {} 중괄호 사용
    dict2 = {}
    print(dict2, type(dict2))

# list 나 tuple 처럼 인덱스를 사용할 수 없음 : 인덱스 없음
# 키(key)를 이용해서 값 조회, 변경, 추가할 수 있음 : 사전변수[키]
# 키는 변경할 수 없음, 키는 중복할 수 없음
# 키와 매칭된 값은 변경할 수 있음, 값 객체는 중복 가능함

# dict 에 값 저장 방식 : (키 : 값) 쌍으로 지정함
def test2():
    dict1 = {'a':1, 'b':2, 'c':3}
    print(dict1, type(dict1)) # {'a': 1, 'b': 2, 'c': 3} <class 'dict'>

    dict2 = {1: 'python', 'a': [1,2,3], (1,2): 345}
    print(dict2, type(dict2))
    # {1: 'python', 'a': [1, 2, 3], (1, 2): 345} <class 'dict'>

# dict 저장된 값 변경 : 사전변수[키] = 바꿀 값
# 키가 존재하지 않으면 자동 추가 저장됨
# 없는 키를 출력하면 에러남
def test3():
    dict2 = {1: 'python', 'a': [1, 2, 3], (1, 2): 345}
    print(dict2, type(dict2)) # {1: 'python', 'a': [1, 2, 3], (1, 2): 345} <class 'dict'>

    # 값 변경
    dict2['a'] = 77
    print(dict2, type(dict2)) # {1: 'python', 'a': 77, (1, 2): 345} <class 'dict'>

    # 아이템 추가
    dict2[3] = [11,2,34]
    print(dict2, type(dict2)) # {1: 'python', 'a': 77, (1, 2): 345, 3: [11, 2, 34]} <class 'dict'>

    # 값 조회 : 사전변수[키]
    print(dict2[3]) # [11, 2, 34]
    # print(dict2[5]) # KeyError: 5

# dict 내장함수 활용
def test4():
    dict1 = {
        'a':10,
        'b':25,
        'c':77
    }
    print(dict1, type(dict1)) # {'a': 10, 'b': 25, 'c': 77} <class 'dict'>

    # 키에 대한 리스트 만들기 : keys() 함수
    print('dict1의 키 목록 : {}'.format(dict1.keys()))
    # dict1의 키 목록 : dict_keys(['a', 'b', 'c'])

    # 값에 대한 리스트 만들기 : values() 함수
    print('dict1의 값 목록 : {}'.format(dict1.values()))
    # dict1의 값 목록 : dict_values([10, 25, 77])

    # (키, 값) 한 쌍(아이템)에 대한 리스트 만들기 : items() 함수
    print('dict1의 아이템 목록 : {}'.format(dict1.items())) # 아이템은 튜플로 반환
    # dict1의 아이템 목록 : dict_items([('a', 10), ('b', 25), ('c', 77)])

# 사전과 사전을 합치기 : update() 함수 사용
# 사전1.update(사전2) = 사전1 이 변경됨
# 사전1과 사전2에 중복된 키가 있을시에는, 사전1의 키 값(사전2의 값으로)이 변경됨

def test5():
    dict1 = {'name':'갤럭시', 'price':1200000,'tax':0.1}
    dict2 = {'content':'최신 모델입니다.', 'price':880000}
    print(dict1) # {'name': '갤럭시', 'price': 1200000, 'tax': 0.1}
    print(dict2) # {'content': '최신 모델입니다.', 'price': 880000}
    dict1.update(dict2)
    print(dict1) # {'name': '갤럭시', 'price': 880000, 'tax': 0.1, 'content': '최신 모델입니다.'}

# dict 내장함수 2
def test6():
    dict1 = {'name': '갤럭시', 'price': 1200000, 'tax': 0.1}
    print('dict1 : ',dict1)

    # pop(key) 함수 : 해당 키에 대한 아이템을 꺼내면서 제거함
    tax = dict1.pop('tax')
    print('dict1 : ',dict1) # dict1 :  {'name': '갤럭시', 'price': 1200000}
    print('tax: ',tax) # tax:  0.1

    # clear() 함수 : 사전 안을 비움 (저장 아이템 전체 삭제)
    dict1.clear()
    print('dict1 : ',dict1) # dict1 :  {}

    dict2 = {'content': '최신 모델입니다.', 'price': 880000}
    print('dict2 : ',dict2, id(dict2))
    # dict2 :  {'content': '최신 모델입니다.', 'price': 880000} 3056473351680

    # copy() 함수 : 사전 객체를 새로 만들고 아이템들을 복사함 (deep copy)
    dict3 = dict2.copy()
    print('dict3 : ',dict3, id(dict3)) # id(변수) : 할당 위치에 대한 id 값 확인(자바의 hashCode()와 같음)
    # dict3 :  {'content': '최신 모델입니다.', 'price': 880000} 3056473351424

    dd = dict2 # 주소복사 : 얕은 복사(shallow copy)
    print('dd : ', dd, id(dd)) # dd :  {'content': '최신 모델입니다.', 'price': 880000} 3056473351680

# dict 안에 키 또는 값이 존재하는지 확인 : in 사용 (반환값 논리값)
def test7():
    dict1 = {'name': '갤럭시', 'price': 1200000, 'tax': 0.1}
    print('dict1 : ',dict1) # dict1 :  {'name': '갤럭시', 'price': 1200000, 'tax': 0.1}

    # 키 존재 여부 : 키 in 사전변수
    print('name 키가 존재하느냐 : ', 'name' in dict1) # name 키가 존재하느냐 :  True
    print('content 키가 존재하느냐 : ', 'content' in dict1) # content 키가 존재하느냐 :  False

    # 값 존재 여부 : 값 in 사전변수
    print('0.1 값이 존재하느냐 : ', 0.1 in dict1.values()) # 0.1 값이 존재하느냐 :  False
    print('880000 깂이 존재하느냐 : ', 880000 in dict1.values()) # 880000 깂이 존재하느냐 :  False

    # 키 제거 : del 사전변수[키]
    del dict1['name']
    print('dict1 : ',dict1) # dict1 :  {'price': 1200000, 'tax': 0.1}

    # 키로 값 조회 : 사전변수[키] == get(key)
    # print('name : ', dict1['name'])   # error
    print('name : ', dict1.get('name'))   # None 리턴



52852852852












