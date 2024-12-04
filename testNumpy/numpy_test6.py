# numpy_test6.py

import numpy as np

# 배열 생성과 초기화 처리 함수 사용 연습
# 초기값 : 변수 공간에 첫번째로 기록되는 값
# 변수 공간 만들면서 바로 초기값 기록하는 것을 초기화라고 함
# np.array([......]) => 리스트 값들로 초기화됨

# zeros() : 배열 생성시 0으로 초기화 함
# 사용 : 배열변수 = np.zeros(배열 할당 갯수) => 1차원 배열 생산하고, 0으로 초기화함
# 사용 : 배열변수 = np.zeros((행 할당 갯수, 열 할당 갯수)) => 2차원 배열 생산하고, 0으로 초기화함
# 사용 : 배열변수 = np.zeros((면 할당 갯수, 행 할당 갯수, 열 할당 갯수)) => 3차원 배열 생산하고, 0으로 초기화함

ar = np.zeros(5)
print(ar)       # [0. 0. 0. 0. 0.]
print(ar.dtype) # float64


br = np.zeros((2,3)) # 튜플로 묶어서 (행,열) 값 입력
print(br)
'''
[[0. 0. 0.]
 [0. 0. 0.]]
'''
print(br.dtype) # float64

# array() 함수와 마찬가지로 zeros() 함수도 dtype 매개변수 사용할 수 있음
car = np.zeros((5,2),dtype='i4')  # int 4byte로 지정
print(car)
'''
[[0 0]
 [0 0]
 [0 0]
 [0 0]
 [0 0]]
'''
print(car.dtype) # int32

# zeros() 함수로 문자배열로 초기화 할 수도 있음
# 문자열은 빈 문자열('',"")로 초기화됨
dar = np.zeros(5,dtype='U4')
print(dar)   # ['' '' '' '' '']
print(dar.dtype)   # <U4 : 유니코드문자 4글자

# 각 인덱스에 값 기록
dar[0] = "abc"
dar[1] = 'abcd'
dar[2] = 'abcde'    # U4 이므로, 마지막 'e'는 기록되지 않음
print(dar)  # ['abc' 'abcd' 'abcd' '' '']

# ones() 함수
# 배열 생성하면서, 1로 초기화 함
ear = np.ones((2,3,4),dtype='i8') # 2면 3행 4열 3차원배열 생성, 정수 1로 초기화
print(ear)
'''
[[[1 1 1 1]
  [1 1 1 1]
  [1 1 1 1]]

 [[1 1 1 1]
  [1 1 1 1]
  [1 1 1 1]]]
'''

print('-------------------------------')
# zeros_like() 함수, ones_like() 함수
# 다른 배열과 같은 크기의 배열을 생성하면서 초기화할 때 사용함
# 예 : 2행 3열의 2차원 배열인 br과 같은 크기의 배열을 생성하려면
far = np.ones_like(br,dtype='f')
print(far, far.dtype)

# empty() 함수
# 값이 기록되지 않은 빈 배열 생성시 사용함 : 배열 생성 시간이 짧아짐 (초기화 시간이 제외됨)
gar=np.empty((4,3))
print(gar)  # 이전에 메모리에 기록되어 있는 쓰레기 값이 출력됨
'''
[[6.23042070e-307 1.42417221e-306 1.37961641e-306]
 [1.37962660e-306 1.42420345e-306 6.23054972e-307]
 [1.78021527e-306 1.42419530e-306 1.86921143e-306]
 [6.89813979e-307 1.78021527e-306 2.22522596e-306]]
'''
# 해당 인덱스에 값을 기록하면, 덮어쓰기(overwrite)되면서 지워지게 됨

# arange() 함수
# 파이썬의 range() 함수와 같음
# 배열 생성시 지정한 범위들의 값들을 초기값으로 기록해 넣을때 사용함
# 초기값, 종료값, 증가치 로 설정하면, 규칙에 따라 증가하는 수열을 만듦
har = np.arange(10)   # 10개의 값을 가진 1차원 배열 생성, 0~9 까지 1씩 증가된 값들로 초기화됨
print(har)  # [0 1 2 3 4 5 6 7 8 9]

har2 = np.arange(3,21,2) # 3이상 ~ 21미만의 값을 넣는데 2씩 증가함
print(har2)  # [ 3  5  7  9 11 13 15 17 19]

# linespace(), logspace() 함수
# linespace(시작값, 끝값, 구간 갯수) : 나누어진 구간을 초기값으로 해서 배열 생성
# logspace(시작값, 끝값, 구간 갯수) : 구간 갯수만큼의 로그구간을 초기값으로 해서 배열 생성
iar = np.linspace(0,100,5) # 0~100까지 5구간으로 나눈 위치의 값으로 초기화 됨
print('iar : ', iar) # iar :  [  0.  25.  50.  75. 100.]

iar2 = np.logspace(0.1,1,10)
print('iar2 : ', iar2)
'''
iar2 :  [ 1.25892541  1.58489319  1.99526231  2.51188643  3.16227766  3.98107171
  5.01187234  6.30957344  7.94328235 10.        ]
'''