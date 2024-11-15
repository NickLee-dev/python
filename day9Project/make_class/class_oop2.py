# path : make_class/class_oop2.py   or make_class\\class_oop2.py
# module : make_class.class_oop2

# 파이썬에서의 연산자 오버로딩 테스트 스크립트

# 오버로딩(overloading) : 클래스 안에 이름이 같은 메소드를 여러개 작성하는 것
# 조건 : 메소드 이름만 같고, 매개변수를 반드시 다르게 구성해야 함(갯수, 자료형 나열순서)

# 연산자(operator) : 값 계산에 사용되는 기호 문자
# c++, python 에서는 기존 값 계산에 사용되는 연산자에다가 클래스 객체에 대한 연산으로 새 의미를 정의할 수 있음
'''
객체 + 값 : __add__(self,값) : return self.필드명 + 값
객체 - 값 : __sub__(self,값) : return self.필드명 - 값
객체 * 값 : __mul__(self,값) : return self.필드명 * 값
객체 / 값 : __truediv__(self,값) : return self.필드명 / 값
객체 > 값 : __gt__(self,값) : return self.필드명 > 값
객체 >= 값 : __ge__(self,값) : return self.필드명 >= 값
객체 < 값 : __lt__(self,값) : return self.필드명 < 값
객체 <= 값 : __le__(self,값) : return self.필드명 <= 값
객체 == 값 : __eq__(self,값) : return self.필드명 == 값
객체 != 값 : __ne__(self,값) : return self.필드명 != 값
'''
class OOP:
    __num = 0

    def __init__(self,num):
        self.__num = num

    def __add__(self,other):
        '+ 연사자를 메소드로 오버로딩 처리'
        return self.__num+other

    def __sub__(self,other):
        '- 연사자를 메소드로 오버로딩 처리'
        return self.__num-other

    def __mul__(self,other):
        '* 연사자를 메소드로 오버로딩 처리'
        return self.__num*other

    def __truediv__(self,other):
        '/ 연사자를 메소드로 오버로딩 처리'
        return self.__num/other

    def get_num(self):
        return self.__num

    def set_num(self,num):
        self.__num = num
# OOP -------------------------------------------------------------------------

# 클래스 객체 생성
ref = OOP(100)

# 객체와 값의 연산 : 객체와 값의 연산은 기본적으로 불가능
# 클래스 안에 연산자 오버로딩 메소드가 작성된 경우에만 객체와 값 연산이 가능함
# print('ref > 30 : ',ref > 30) # TypeError: '>' not supported between instances of 'OOP' and 'int'
# 오버로딩 안한 연산자는 사용 불가
print('ref + 30 : ',ref + 30) # ref + 30 :  130

print('ref - 30 : ',ref - 30) # ref - 30 :  70

print('ref * 30 : ',ref * 30) # ref * 30 :  3000

print('ref / 30 : ',ref / 30) # ref / 30 :  3.3333333333333335



