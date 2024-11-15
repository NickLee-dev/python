# path : make_class/class_oop.py
# module : make_class.class_oop
# 파이썬에서 객체 지향 프로그래밍 (OOP) 사용

# 객체지향 프로그래밍에서의 클래스 맴버는
# field(맴버변수, property), method(맴버함수), constructor(생성자), destructor(소멸자)
# oop에 사용되는 기술도 적용해야 함
# 캡슐화(encapsulation), 상속(inheritance), 다형성(polymorphism), 추상화(abstraction)
# 오버로딩(overloading), 동적바인딩 등 사용됨

# 피이썬은 객체지향 스크립트 언어이다.
# 절차지향 프로그래밍 가능함 : 함수 단위로 실행 순서를 정해서 작동되게 함

# 객체지향 프로그래밍은 클래스 만들기부터 시작함
'''
class 클래스명:
    맴버변수 = 초기값
    ......
    def 함수명(self, 매개변수, *매개변수, 매개변수=기본값):  # 무조건 self 앞에 붙여야함
        맴버변수들에 대한 값 처리를 담당함
        self.맴버변수 = 변경할 값 | 계산식
        return self.필드명 또는 return 결과값

self 매개변수 : 자바, C++, javascript, C# 의 this와 같음
'''

# 클래스 이름은 첫글자는 영어대문자 사용을 권장함
class SClass:
    pass      # 맴버가 없는 빈 클래스 작성할 수 있음
# 비어 있는 클래스 실행시  namespace 가 할당됨 => 이름만 있어도 메모리 공간이 할당됨

# 만들어진 클래스를 사용하는 방법 : 객체 생성(메모리에 클래스에 대한 객체공간(인스턴스,instance) 할당)
# 레퍼런스 변수 = 클래스명()
# 레퍼런스 변수 : 메모리에 할당된 해당 클래스의 인스턴스의 주소를 가지는 변수
ref1 = SClass()
ref2 = SClass()

# print('ref1 이 가진 객체의 주소 : ',id(ref1))
# print('ref2 이 가진 객체의 주소 : ',id(ref2))

# 파이썬은 실행할 때(동적으로) 멤버 변수(필드)를 추가할 수 있음
ref1.score = 100   #  ref1이 참조하는 인스턴스 안에 score 를 추가하고, 100을 기록 저장함
# print('ref1이 참조하는 객체 안의 score : ',ref1.score)
# print('ref2이 참조하는 객체 안의 score : ',ref2.score) # AttributeError: 'SClass' object has no attribute 'score'

# oop 적용 기술 1 : 캡슐화
# 캡슐화 : data 보호가 목적임, 필드에 접근 제한을 설정하는 것
# 필드에 접근제한자(access modifier)를 사용하게 됨
# private(비공개),public(공개),protected(상속시 후손에게만 공개)

# 파이썬에서는 접근제한자가 없음 (해당 단어 키워드 제공 안함)
# 파이썬에서는 기본적으로 모든맴버는 public 임
# 레퍼런스.필드명, 클래스명.필드명
# 레퍼런스.메소드명(), 클래스명.메소드명()

# private : 클래스 밖에서 사용 못 함, 클래스 안에서만 사용할 수 있음
# 파이썬에서는 클래스 맴버를 비공개(private) 처리 하려면
# 필드명이나 메소드명 이름 앞에 '_'(underscore)를 2개 붙이면 됨

class PClass:
    #file (property,attribute) : private
    __num = 10

    # constructor : 매개변수 있는 생성자
    def __init__(self,num): # 매개변수가 있는 생성자
        self.__num = num

    # method(public)
    def set_num(self,num):
        self.__num = num

    def get_num(self):
        return self.__num
    # -----------------------------------

# 클래스 사용
pref = PClass(20) # 기본생성자 자동 실행됨 : 객체 공간 할당하고 주소 리턴함
print('pref 가 가진 주소 : ',id(pref))
print('인스턴스 안의 __num 값 : ',pref.get_num())   # getter활용 값 가져오기
# pref.__num = 20 # private 필드는 클래스 밖에서 사용 못함

# 생성자(Constructor)
# 클래스에 대한 객체 인스턴스가 메모리에 할당될 때, 필드 초기화가 목적인 함수
# 생성자가 없으면, 내부에서 기본생성자 자동 작동됨
# 생성자를 작성한다면, __init__ 이름으로 정의해야 함 (파이썬이 정해 놓음)
# 파이썬에서는 생성자 오버로딩(overloading) 할 수 없음 : 생성자는 1개 (기본 | 매개변수 있는 생성자)

'''
class 클래스명 : 
    def __init__(self, 매개변수) : # 주로 매개변수 있는 생성자를 작성함
        self.필드명 = 매개변수
        
생성자 사용 :
레퍼런스변수 = 클래스명() # 기본생성자
레퍼런스변수 = 클래스명(전달값) # 매개변수 있는 생성자
'''
pref2 = PClass(200)
print('pref2 가 참조하는 인스턴스 안의 필드값 : ',pref2.get_num())

# destructor (소멸자 함수)
# 객체 인스턴스가 메모리에서 제거(소멸)될 때 자동 실행되는 함수임
# 클래스 안에 직접 작성한다면, __del__ 로 함수 정의함
# 해당 클래스에 대한 객체 인스턴스가 메모리에서 제거 될 때,
# 해당 객체 관련 메모리나 자원들의 공유 설정, 점유 설정 등을 해제하고자 할 때 이용함
'''
class 클래스명 :
    def __del__(self):  # 모든 메소드의 self는 무조건 들어감
        해당 객체가 소멸될 때 같이 제거 또는 해제할 내용에 대한 코드 작성
'''
class Var:
    # feild : private
    __number = 100

    # constructor
    def __init__(self, number):
        self.__number = number

    # destructor
    def __del__(self):
        print('인스턴스 제거시 자동 작동됨',id(self))

    # method
    def set_number(self, number):
        self.__number = number

    def get_number(self):
        return self.__number
# Var -----------------------------------------------------

v1 = Var(77)
v2 = Var(88)

print('v1 : ',v1.get_number(),id(v1))
print('v2 : ',v2.get_number(),id(v2))
# 프로그램 종료시 소멸자가 자동 작동됨

# 키보드로 값을 입력받아서 필드값 변경 처리
v1.set_number(int(input('v1 참조객체의 변경할 필드값 : ')))
print('v1 : ',v1.get_number(),id(v1))
v2.set_number(int(input('v2 참조객체의 변경할 필드값 : ')))
print('v2 : ',v2.get_number(),id(v2))

# 정적 메소드 (static method) ----------------------------------------------
# 프로그램 실행시 정적 메모리(static)에 따로 기록되는 메소드를 말함
# 메소드 작성시 메소드 이름 위에 장식자(decorator==어노테이션,annotation)를 표시하면 됨
# @staticmethod
# self가 없는 메소드임 => 사용 : 클래스명.메소드명()

class C:
    def ham(self,x,y):
        print('instance method : ', x,y)# 주소를 자동으로 self 가 전달받음

class D:
    @staticmethod
    def spam(x,y): # static 메소드는 self 없음
        print('static or class method : ', x,y)

# static 메소드 실행 : 주소가 필요없음 => 객체 생성 없이 바로 사용함
D.spam(100,200)

# instance 메소드 실행 : 주소 전달 받아야 함 => 객체 생성해서 주소 발생시킴
cref = C()
cref.ham(22,33)
# 또 다른 사용법
C.ham(cref, 44, 55)





