# chap02.py
from pickle import FALSE

# 식별자 : 개발자가 지어주는 이름
# 변수(variable) : 프로그램 구동시 메모리(RAM)에 값 기록하는 공간(방)
# 함수(function) : 반복 사용되는 코드를 분리 작성하여 이름 붙여준 것(코드의 조각 코드 묶음)
# 모듈(modul) : 함수들을 따로 모아놓은 파일
# 클래스(class) : 파이썬은 객체지향형 스크립트 언어임

# 파이썬의 이름 작성 규칙 (식별자 조건 : Naming Rule)
# 1. 대소문자 구분함 : name과 Name 은 다른 이름임
#    문자형은 '' 또는 "" 사용
NAME = '홍길동'
name = '이순신'
Name = '황지니'
print(NAME,name,Name)

# 2. 이름의 첫글자에 숫자 사용 못함 : 1num(에러)
# 1num = 100
# print(1num)

# 3. 이름의 첫글자는 문자 또는 _(underscore) 만 사용할 수 있음
_score = 100.0
print(_score)

# 4. _ 를 제외한 기호문자, 공백 사용 못 함
# $menu, all*, one num : 에러
# num& = 12
# print(num&)

# 5. 이름의 중간 위치나 끝에 숫자 사용할 수 있음 : num1, first1_num
num1 = 10
num2 = 20
print(num1>num2)

# 6. 예약어 (프로그램 언어가 사용하기 위해서 별도로 정해놓은 단어들)는 이름으로 사용할 수 없음
#True = 1 # error
true = 1
print(true)

# 파이썬이 제공하는 예약어 확인
# keyword 모듈에서 제공함 : import 해서 사용함
import keyword
print(len(keyword.kwlist)) # 35개의 키워드가 있음
print(keyword.kwlist) # 35개의 키워드가 있음

# 파이썬에서 제공하는 내장함수 : 기본으로 제공됨
# 별도의 import 선언하지 않고 바로 사용함
# max, min, type, len, range, str, int, float, print, input 등의 함수들

# type(값 또는 변수명) : 값의 자료형 리턴

# len(값 또는 변수) : 길이(저장된 값의 갯수) 리턴
a = 'abcd'
b = [1,2,3,4,5]
print(len(a),len(b)) # 4 5

#max(값들 또는 변수) : 최대값(가장 큰 값), min(값들 또는 변수) : 최소값(가장 작은 값)
print(max("abcdefg"))  # g
print(max("123456789"))  # 9
print(min("abcdefg"))  # a
print(min("123456789"))  # 1

# 주석 (comment)
# 한 줄 주석(line comment)
'''
여러줄 주석
작은 따옴표 또는 큰 따옴표를 앞뒤에 3개씩 표시함
파이썬에서는 single quotation 과 double quotation 은 동일하게 취급됨
'''

print(abs(-10)) # 10
# 파이썬에서는 변수는 반드시 값을 가져야 생성됨
# num # name 'num' is not defined
num = 12
print(num)

# 파이썬에서는 변수에 기록할 값의 종류(data type : 자료형)를 정하지 않음
# 자료형 변수명 = 기록할 값 => 변수명 = 기록할 값
# 변수방에 기록되는 값에 따라 자료형이 정해짐 : 동적할당(변경시에도 바뀜)

value = 100
print(value,type(value))

value = 'python'
print(value,type(value))

value = 3.12
print(value,type(value))

value = False
print(value,type(value))

# 변수 제거: del 변수명
del value
# print(value,type(value)) # error
