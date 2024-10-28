# test_set/set_sample.py
# test_set.set_sample

# 집합(set) 자료형
# 교집합(&), 합집합(|), 차집합(-) 연산이 가능한 자료형
# 저장 방식은 자바의 Set 과 같음 : 같은 값 중복 저장 안 함, 저장 순서 없음

# set 정의 방법 1 : {} 중괄호 사용, 단 빈 {} 는 무조건 dict임
# set 으로 사용하려면 {} 안에 초기값 지정해야 됨

def test1():
    # set1 = {}  # {} <class 'dict'> # 그냥 이렇게 선언하면 dict 으로 인식
    set1 = {1,3,2,4,5}
    print(set1, type(set1))  # {1, 2, 3, 4, 5} <class 'set'>

    # set 정의 방법 2 : set() 함수 사용
    set2 = set()
    print(set2, type(set2)) # set() <class 'set'>

    # set 에 문자열을 저장하는 경우 : 문자 하나씩 저장됨
    set3 = {"Hello World"} # {'Hello World'} <class 'set'>
    # 사용 권장 안함
    print(set3, type(set3))

    set3 = set("Hello World") # {' ', 'l', 'o', 'W', 'd', 'H', 'e', 'r'} <class 'set'>
    # 사용 권장
    print(set3, type(set3)) # 값 중복 저장 안함 : 'l' 한개만 저장

    set3 = set('python') # {'o', 't', 'h', 'y', 'n', 'p'} <class 'set'>
    print(set3, type(set3)) # 저장 순서가 유지 안됨 : 인덱싱 못 함

    # set에 list 저장 할 수 있음
    set4 = set([1,2,4,8,5,6,7,3,9]) # {1, 2, 3, 4, 5, 6, 7, 8, 9} <class 'set'>
    print(set4, type(set4)) # 리스트는 유지되지 않음 => 값 순서대로 저장됨 : set이 저장 순서를 유지하게끔 하는 방법임

def test2():
    # set 자료형은 집합 연산
    set1 = set([1,2,3,4,5,6,7,8,9])
    print(set1, type(set1)) # {1, 2, 3, 4, 5, 6, 7, 8, 9} <class 'set'>
    set2 = set([4,5,6,7,8,9,10])
    print(set2, type(set2)) # {4, 5, 6, 7, 8, 9, 10} <class 'set'>

    # 교(곱)집합 : & 연산자 사용 또는 intersection() 메소드 사용
    print(set1.intersection(set2)) # {4, 5, 6, 7, 8, 9}
    print(set1&set2) # {4, 5, 6, 7, 8, 9}

    # 합집합 : | 연산자 사용 또는 union() 메소드 사용
    print(set1|set2) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    print(set1.union(set2)) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    # 차집합 : - 연산자 사용 또는 difference() 메소드 사용
    print(set1-set2) # {1, 2, 3}
    print(set1.difference(set2)) # {1, 2, 3}

def test3():
    # 값 추가, 삭제 가능함
    set1 = set([1,2,3,4,5,6,7,8,9])
    print(set1, type(set1)) # {1, 2, 3, 4, 5, 6, 7, 8, 9} <class 'set'>

    # 값 1개 추가 : add()
    set1.add(99)
    print(set1, type(set1)) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 99} <class 'set'>
    # 값 여러개 추가 : update([리스트])
    set1.update([777])
    print(set1, type(set1)) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 777} <class 'set'>
    set1.update([33,44,55])
    print(set1, type(set1)) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 777, 33, 44, 55} <class 'set'>

    # 값 삭제 : remove(삭제할 값)
    set1.remove(777)
    print(set1, type(set1)) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 33, 44, 55} <class 'set'>

    # list의 값 중복을 제거할 때 set을 주로 이용함
    list1 = [1,1,1,2,2,2,3,3,4,4,5,6,7,78,6,5,3,3,3,4,7,4,2]
    print(list1, type(list1)) # [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 6, 7, 78, 6, 5, 3, 3, 3, 4, 7, 4, 2] <class 'list'>
    set2 = set(list1)
    print(set2, type(set2)) # {1, 2, 3, 4, 5, 6, 7, 78} <class 'set'>
    list1 = [set2]
    print(list1, type(list1)) # [{1, 2, 3, 4, 5, 6, 7, 78}] <class 'list'>

