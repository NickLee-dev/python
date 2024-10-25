# chap04_list.py

# list 자료형 : 파이썬이 제공하는 군집 자료형
# 자바의 List와 같은 자료형임

# 개념 : 여러 종류의 데이터들을 순차적으로 저장하는 자료형임
# 저장 용량의 제한 없음
# 저장되는 데이터의 종류에도 제한 없음
# 저장 순서에 대한 순번(인덱스, index)가 있음

# 리스트 생성 방법
# 1. list() 함수 사용
list_1 = list()
print(list_1,type(list_1))  # [] 비어있는 리스트 확인 가능
# 2. [] 대괄호 사용
list_2 = []
print(list_2,type(list_2)) # [] 비어있는 리스트 확인 가능

# list 자료형 특징
# 1. 문자열(str)과 같이 인덱싱, 슬라이싱 연산이 가능함
# index(순번, 저장 순서, 0부터 시작함)
# 인덱싱 표현 : 리스트 변수[순번]
list_3 = [1,2,3,'python',3.45,"호호호",[11,22,33],True,False]
print(f'0번째 기록된 값 조회 : {list_3[0]}{type(list_3[0])}') # 0번째 기록된 값 조회 : 1<class 'int'>
print(f'3번째 기록된 값 조회 : {list_3[3]}{type(list_3[3])}') # 3번째 기록된 값 조회 : python<class 'str'>
print(f'4번째 기록된 값 조회 : {list_3[4]}{type(list_3[4])}') # 4번째 기록된 값 조회 : 3.45<class 'float'>
print(f'6번째 기록된 값 조회 : {list_3[6]}{type(list_3[6])}') # 6번째 기록된 값 조회 : [11, 22, 33]<class 'list'>
print(f'8번째 기록된 값 조회 : {list_3[8]}{type(list_3[8])}') # 8번째 기록된 값 조회 : False<class 'bool'>

# 슬라이싱 : 리스트에 저장된 데이터들을 부분 추출
# 표현 : 리스트변수[시작인덱스(이상):끝인덱스(미만):간격]
# 시작인덱스부터 끝인덱스 -1 위치까지 추출함
# 간격 : 생략되면 기본값 1
print('0번 인덱스부터 3번 인덱스 까지의 데이터 추출 : {}'.format(list_3[0:4:1])) # 0번 인덱스부터 3번 인덱스 까지의 데이터 추출 : [1, 2, 3, 'python']
print('0번 인덱스부터 3번 인덱스 까지의 데이터 추출 : {}'.format(list_3[:4:])) # 0번 인덱스부터 3번 인덱스 까지의 데이터 추출 : [1, 2, 3, 'python']

# len(리스트변수) : 리스트에 저장된 데이터 갯수 리턴
print('list_3에 저장된 데이터 갯수 : {0}'.format(len(list_3))) # list_3에 저장된 데이터 갯수 : 9
# len() 을 이용해서 마지막 위치의 데이터 조회에 활용할 수도 있음
print(f'list_3 의 마지막 index : {len(list_3)-1}') # list_3 의 마지막 index : 8
print(f'list_3 의 마지막 index의 데이터 : {list_3[len(list_3)-1]}') # list_3 의 마지막 index의 데이터 : False

# list 자료형 특징 2 : 요소(element)의 데이터 변경할 수 있음
# 변경할 데이터의 종류에 제한이 없다.
# 인덱스를 이용하여 변경 : 리스트변수[인덱스] = 바꿀데이터
print('변경전 : {}'.format(list_3)) # 변경전 : [1, 2, 3, 'python', 3.45, '호호호', [11, 22, 33], True, False]
list_3[0] = 77
print('변경후 : {0}'.format(list_3)) # 변경후 : [77, 2, 3, 'python', 3.45, '호호호', [11, 22, 33], True, False]
list_3[1] = 'test'
print(f'변경후 : {list_3}') # 변경후 : [77, 'test', 3, 'python', 3.45, '호호호', [11, 22, 33], True, False]
list_3[2] = [1.2, 2.3, 3.4]
print(f'변경후 : {list_3}') # 변경후 : [77, 'test', [1.2, 2.3, 3.4], 'python', 3.45, '호호호', [11, 22, 33], True, False]

# list 자료형 특징 3 : 리스트를 다루는 함수(메소드)
# list 는 객체다
# list 를 다루는 함수(메소드)는 리스트변수.함수명(전달인자) 로 작성
# append() : 뒤에 추가
# insert() : 다른 element 사이에 추가
# remove() : 삭제
# pop() : 꺼내면서 리스트에서 제거
# reverse() : list 안에 데이터 순서를 반대로 바꿈 (뒤집기)
# clear() : 리스트 비움(전체삭제)

lst = [1, 3.5, '안녕', True, 20, ["a","b",1]]
print(f'before : {lst}')  # before : [1, 3.5, '안녕', True, 20, ['a', 'b', 1]]
print(f'length : {len(lst)}')  # length : 6

# append() : 리스트 마지막 추가, 인덱스 증가됨
# 리스트변수.append(추가할 데이터)
lst.append(456)
print(f'after : {lst}')  # after : [1, 3.5, '안녕', True, 20, ['a', 'b', 1], 456]
print(f'length : {len(lst)}')  # length : 7

# remove() : 값을 이용하여 지정한 데이터 제거함, 갯수 줄어듦
# 리스트변수.remove(추가할 데이터)
lst.remove(20)
print(f'after : {lst}')  # after : [1, 3.5, '안녕', True, ['a', 'b', 1], 456]
print(f'length : {len(lst)}')  # length : 6

# 값은 값들이 여러개 저장되어 있는 리스트인 경우
lst_1 = [1,1,2,2,1,3]
print(f'before : {lst_1}') # before : [1, 1, 2, 2, 1, 3]
print(f'length : {len(lst_1)}') # length : 6
lst_1.remove(1) # 앞에서부터 검색해서 첫번째로 만나는 데이터를 삭제함
print(f'after : {lst_1}') # after : [1, 2, 2, 1, 3]
print(f'length : {len(lst_1)}') # length : 5

# insert() : 리스트 안의 원하는 위치에 데이터 추가
# 리스트변수.insert(index, value)
lst.insert(1,'추가')
print(f'after : {lst}') # after : [1, '추가', 3.5, '안녕', True, ['a', 'b', 1], 456]
print(f'length : {len(lst)}') # length : 7

# pop() : 인덱스 위치의 데이터 꺼냄(제거)
# [꺼낸값 받을 변수 = ] 리스트변수.pop() : 마지막 index의 데이터 꺼냄(제거)
# 리스트변수.pop(index) : 지정한 인덱스의 데이터 꺼냄(제거)
num = lst.pop()
print(f'num : {num}') # num : 456
print(f'after : {lst}') # after : [1, '추가', 3.5, '안녕', True, ['a', 'b', 1]]
print(f'length : {len(lst)}') # length : 6

lst.pop(3)
print(f'after : {lst}') # after : [1, '추가', 3.5, True, ['a', 'b', 1]]
print(f'length : {len(lst)}') # length : 5

# extend() : 기존 list 뒤에 다른 리스트를 추가 연결해서 리스트를 확장함
# 리스트변수1.extend(뒤에 추가 연결할 리스트 변수 2)
lst.extend(lst_1)
print(f'after : {lst}') # after : [1, '추가', 3.5, True, ['a', 'b', 1], 1, 2, 2, 1, 3]
print(f'length : {len(lst)}') # length : 10

# reverse() : 리스트의 저장 순번을 반대로 뒤집기함
# 리스트변수.reverse()
lst.reverse()
print(f'after : {lst}') # after : [3, 1, 2, 2, 1, ['a', 'b', 1], True, 3.5, '추가', 1]
print(f'length : {len(lst)}') # length : 10

# sort() : 리스트의 저장 데이터들을 오름차순 정렬 처리함
# 주의 : 자료형이 한가지 종류의 데이터로만 저장되어 있을때 사용할 수 있음
# lst.sort() # TypeError: '<' not supported between instances of 'list' and 'int'
lst_1.sort()
print(f'after : {lst_1}') # after : [1, 1, 2, 2, 3]
print(f'length : {len(lst_1)}') # length : 5
#int
lst_int = [32,4,8,5,4,3,45,34]
print(f'before : {lst_int}') # before : [32, 4, 8, 5, 4, 3, 45, 34]
print(f'length : {len(lst_int)}') # length : 8
lst_int.sort()
print(f'after : {lst_int}') # after : [3, 4, 4, 5, 8, 32, 34, 45]
print(f'length : {len(lst_int)}') # length : 8
# reverse=False 기본값으로 생략, 오름차순정렬
lst_int.sort(reverse=True)   # reverse=True 일 경우 내림차순정렬
print(f'after : {lst_int}') # after : [45, 34, 32, 8, 5, 4, 4, 3]
print(f'length : {len(lst_int)}') # length : 8

lst_str = ['안녕','banana',"tiger",'kiwi','오렌지','apple','melon']
print(f'before : {lst_str}') # before : ['안녕', 'banana', 'tiger', 'kiwi', '오렌지', 'apple', 'melon']
lst_str.sort()
print(f'after : {lst_str}') # after : ['apple', 'banana', 'kiwi', 'melon', 'tiger', '안녕', '오렌지']
lst_str.sort(reverse=True)
print(f'after : {lst_str}') # after : ['오렌지', '안녕', 'tiger', 'melon', 'kiwi', 'banana', 'apple']

lst_str_kr = ['자바','파이썬','씨샾','자바스크립트','오라클','리액트']
print(f'before : {lst_str_kr}') # before : ['자바', '파이썬', '씨샾', '자바스크립트', '오라클', '리액트']
lst_str_kr.sort()
print(f'after : {lst_str_kr}') # after : ['리액트', '씨샾', '오라클', '자바', '자바스크립트', '파이썬']
lst_str_kr.sort(reverse=True)
print(f'after : {lst_str_kr}') # after : ['파이썬', '자바스크립트', '자바', '오라클', '씨샾', '리액트']

# count() : 리스트에 저장된 같은 값의 갯수 조회
# 리스트변수.count(찾을 값)
print('lst : {}'.format(lst)) # lst : [3, 1, 2, 2, 1, ['a', 'b', 1], True, 3.5, '추가', 1]
print(f'lst 에 저장된 정수 1의 갯수 : {lst.count(1)}') # lst 에 저장된 정수 1의 갯수 : 4
# True 는 1로 인식해서 1이 4개로 카운팅
