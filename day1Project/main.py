# This is a sample Python script.
from itertools import filterfalse


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# 파이썬에서 함수 만들기는 : def(define) 키워드 사용함
# 변수명, 함수명 : 문자, 숫자, _ 사용가능하고 시작은 문자로만
# def 함수명(매개변수):
# 함수구문을 구분짓기위해 들여쓰기 해야됨
# 들여쓰기함 함수의 실행 코드 작성함
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def test_function():
    a = 1
    b = '1'
    c = 1.1
    d = True
    e = 9999999999999999999999999999999999999999999999999999999999999
    f = 4 + 1j
    print(type(a), type(b), type(c), type(d), type(e), type(f))



# if문 시작을 : 을통해 나타내고
# 들여쓰기로 if구문을 구분지음
if __name__ == '__main__':
    # 함수 실행 : 함수명(전달인자) 또는 변수명 = 함수명(전달인자)
    print_hi('PyCharm')  # 함수 실행 구문
    test_function()  # 함수 실행
    a = "안녕"
    b = "하세요"
    print(a + b,type(a+b))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
