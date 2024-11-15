# path : module\\sample_module.py
# module : module.sample_module
# 파이썬에서 모듈 만들어서 사용하기

# 모듈 : 파이썬 소스 파일이다.(파일명.py)
# 파일명이 모듈명이 됨
# 모듈용 소스 파일에는 함수와 전역변수, 클래스가 저장됨
# 모듈용 소스 파일에는 main이 있으면 안 됨(필요시 사용 후 주석처리)
# 모듈이 제공하는 함수, 전역변수, 클래스를 사용하려면, import 모듈명으로 선언한 다음에
# 모듈명.전역변수명, 모듈명.함수명(), 모듈명.클래스명 으로 사용하면 됨

import keyword
#keyword.py 파일을 의미함
help('keyword')
print(keyword.kwlist) # 예약어 리스트 출력됨
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# 모듈은 다른 파이썬 파일에서 사용할 수 있도록 함수(기능)와 변수(값)들을 따로 저장해서 제공하는 목저의 소스 파일임
# 모듈 임포트시에 모듈명이 길 경우 줄임말을 같이 선안할 수도 있음
# import 모듈명 as 줄임말 => 사용시 모듈명.함수명()을 줄임말.함수명()으로 사용할 수 있음
import keyword as k

print(k.kwlist)
print(k.__file__)  # 해당 모듈(파이썬 파일) 의 위치가 출력됨
# C:\Users\ict01-13\AppData\Local\Programs\Python\Python313\Lib\keyword.py

# help('modules') # 현재 설치되어 있는 모듈 확인

# 모듈설치
# help('random')

# 파이썬이 제공하는 표준 모듈들 확인 -------------------------------------------------------------
# 파일이나 디렉토리 관련 기능을 제공 - os ------------------------------------------------
import os
print(os.getcwd()) # D:\python_workspace\day8Project\module

# 날짜와 시간 관련 기능 제공 - time --------------------------------------------------------
import time

print(time.localtime()) # 현재 날짜와 시간 정보 출력
# time.struct_time(tm_year=2024, tm_mon=11, tm_mday=4, tm_hour=12, tm_min=15, tm_sec=4, tm_wday=0, tm_yday=309, tm_isdst=0)

time.sleep(1) # 1초 멈춤
print(time.time()) # 현재 시간을 밀리세컨드로 출력 # 1730690227.8520744

# 임의의 숫자를 발생시키는 기능 제공 - random -----------------------------------------
import random as r

print(r.random()) # 0.0 <= random < 1.0
print(r.randint(1,5)) # 1<= random <= 5
print(r.randrange(1,10,2)) # 1 <= 2간격의 정수 < 10

# 수학 계산 관련 기능 제공 - math -----------------------------------------------------
import math as m
print('원주율 : ', m.pi)  # 원주율 :  3.141592653589793
print('5! : ', m.factorial(5))   # 5! :  120   (펙토리얼)

# 달력을 출력해서 날짜 지정 기능 제공 - calendar ----------------------------------------------------
import calendar

calendar.prmonth(2024, 11)

# __name__ : 현재 실행 되고 있는 모듈이름 확인
print(__name__)    # main 파일이름이 출력됨
# 프로그램을 실행하면 기본 파일은 main 모듈임. 즉, 프로그램은 main 만 실행할 수 있다는 의미임

# ----------------------------------------------------------------------------------
# 사용자 정의 모듈 사용하기
import mymodule as my

print('더하기 : ', my.sum(10,20))
print('빼기 : ', my.sub(15,7))
print('곱하기 : ', my.mul(15,3))
print('나누기한 몫 : ', my.div(12,5))
try:
    print('나누기한 나머지 : ', my.mod(12,0))
except Exception as msg:
    print(msg)
    pass  # 프로그램 진행시켜라

print('가장 큰 값 : ', my.max())
print('가장 큰 값 : ', my.max(10))
print('가장 큰 값 : ', my.max(1,2,3,4,5,6,7,8,9))

print('가장 작은 값 : ', my.min())
print('가장 작은 값 : ', my.min(10))
print('가장 작은 값 : ', my.min(1,2,3,4,5,6,7,8,9))

print('글자 갯수 : ', my.strlen())
print('글자 갯수 : ', my.strlen('module test'))

print('원주율 : ', my.pi)
print('count : ', my.count)