# numpy_test9.py

import numpy as np
from numpy.ma.core import arange

# 배열간의 연산 : 백터화 연산
# 백터화 연산을 사용하면, 반복문을 쓰지 않고 각 원소에 대한 연산 가능함
# 또 다른 장점은 선형대수 공식과 동일한 연산을 간단하게 작성 할 수 있음

x = np.arange(1,10001) # 1만개 (1~ 10000 초기화)
y = np.arange(10001,20001) # 1만개 (10001 ~ 20000 초기화)
z = np.zeros_like(x)    # 1만개, 0으로 초기화

# 배열에 대한 백터화 연산을 사용하지 않으면, 반복문으로 각 원소에 대한 연산 처리해야 함
# z[0] = x[0] + y[0], ...  1만번 반복 실행
for i in range(10000): # i: 0~9999
    z[i] = x[i] + y[i]

print(z[:10])  # 슬라이싱 : 0 ~ 9 까지 10개만 출력 처리

# 백터화 연산 사용 :
z = x+y
print(z[:10])  # 위에 반복문과 동일결과 출력

# 산술연산, 비교연산, 논리연산 모두 백터화 연산 가능함
ar = np.array([1,2,3,4])
br = np.array([4,2,2,4])

print(ar == br) # ar[0]==br[0] => 결과 : True|False [False  True False  True]
print(ar >= br) # ar[0]>=br[0] => 결과 : True|False [False  True  True  True]

# 만약, 배열 각 인덱스 값끼리 하나씩 비교한 결과가 아니라,
# 배열의 모든 요소가 다 같은지 알고 싶다면 all() 을 사용하면 됨
cr = np.array([1,2,3,4])

print(np.all(ar == br))  # False
print(np.all(ar >= cr))  # True

# 지수함수(exp), 로그함수(log) 등 수학 함수들도 백터화 연산을 지원함
dar = np.arange(5)
print(np.exp(dar)) # [ 1.          2.71828183  7.3890561  20.08553692 54.59815003]
# exp() 함수 : 지수 e의 x제곱을 구하는 함수

print(10**dar)  # 10의 제곱
print(np.log(dar+1))  # [0.         0.69314718 1.09861229 1.38629436 1.60943791]

# 스칼라와 백터 / 행렬의 곱셈
x = np.arange(10)
print(x)
print(100*x)

y = np.arange(12).reshape(3,4)
print(y)
print(100*y)

# 브로드캐스팅(broadcastion)
# 백터, 행렬(2차원 배열)끼리 덧셈 또는 뺄셈을 하려면, 값 갯수 또는 행갯수와 열갯수가 같아야 함
# numpy 에서 행과 열이 다른 백터끼리도 연산이 가능하도록 지원함=> 이 기능을 브로드캐스팅이라고 함
# 크기가 작은 백터가 자동으로 크기가 큰 백터의 행과 열 갯수와 맞춰짐(확장)

# 확인 1 :
x = np.arange(5)
print(x) # [0 1 2 3 4]
y = np.ones_like(x)
print(y) # [1 1 1 1 1]

print(x+y) # [1 2 3 4 5]
print(x+1) # [1 2 3 4 5]

# 다차원배열에도 적용
dx = np.vstack([range(7)[i:i+3] for i in range(5)])   # 리스트 내포
print(dx)
'''
[[0 1 2]
 [1 2 3]
 [2 3 4]
 [3 4 5]
 [4 5 6]]
'''
dy = np.arange(5)[:,np.newaxis]  # 열이 행이 됨, 차원 1 증가됨
print(dy)
'''
[[0]
 [1]
 [2]
 [3]
 [4]]
'''

# 행과 열 갯수가 다른 경우
print(dx + dy) # 열 갯수가 다른 2차원배열 더하기 연산 : 브로드캐스팅 적용됨
'''
[[ 0  1  2]
 [ 2  3  4]
 [ 4  5  6]
 [ 6  7  8]
 [ 8  9 10]]
'''

# 차원 축소 연산
# 배열의 가로 행(줄) 또는 세로 열(칸) 전체를 하나의 값으로 보고 연산해서
# 하나의 결과를 만드는 것을 축소 연산 (demension reduction) 이라고 함
# 1차원 배열은 축소연산의 결과는 값 1개
# 2차원 배열은 축소연산의 결과가 1차원 배열이 됨
# 사용되는 함수 : max(최대값), min(최소값), argmax(최대값의 index), argmin(최소값의 index)
#               sum(합계), mean(평균), median(중간값), std(표준편차), var(분산)
#               boolean 값 : all, any

x = np.array([1,2,3,4])
print(x) # [1 2 3 4]
print(np.sum(x)) # 10
print(x.sum()) # 10

x2 = np.array([1,3,2])
print(x2.max())  # 3
print(x2.min())  # 1
print(x2.argmax())  # 최대값의 인덱스 : 1
print(x2.argmin())  # 최소값의 인덱스 : 0

x3 = np.array([1,3,2,1])
print(x3.mean()) # 평균값 : 1.75
print(np.median(x3)) # 최소와 최대값의 중간값 : 1.5

print(np.all([True,True,False]))  # 모든 값이 True인지 : False
print(np.any([True,True,False]))  # 값중 True 가 있는지 : True

ar = np.zeros((100,100),dtype=np.int_)
print(ar)
'''
[[0 0 0 ... 0 0 0]
 [0 0 0 ... 0 0 0]
 [0 0 0 ... 0 0 0]
 ...
 [0 0 0 ... 0 0 0]
 [0 0 0 ... 0 0 0]
 [0 0 0 ... 0 0 0]]
'''
print(type(ar[0][0]))  # <class 'numpy.int64'>
print(np.any(ar != 0))  # False, 배열 안에 0이 아닌 값이 하나라도 있느냐?
print(np.all(ar == ar)) # True, 배열의 각 인덱스 끼리의 값들이 모두 같으냐?

a = np.array([1,2,3,2])
b = np.array([2,2,3,2])
c = np.array([6,4,4,5])

print(((a<=b) & (b<=c)).all()) # True
# & : [T,T,T,T].all() => 모두 다 True냐?

# 중간값(median) 확인-----------------------------------------------------------------
data = [1,3,5,7,9]
median_value = np.median(data)
print(median_value)  # 출력 : 5.0, 배열의 값이 홀수개이면 배열값들중 중간에 해당되는 값 선택

data = [1,7,5,2]
median_value = np.median(data)
print(median_value) # 출력 : 3.5, 배열의 값이 짝수개이면 중간에 해당되는 값 2개를 골라서 나누기 2 한 값

# 정렬 : sort()
# 1차원 배열은 값들의 오름 | 내림차순정렬 처리함
# 2차원 배열은 행별(가로값들)로 정렬, 열별로 (세로값들)로 정렬 처리할 수 있음 ( axis 매개변수 사용함 )
# axis = 0 : 열별로 정렬, axis = 1 | -1 (기본값임, 행별로 정렬)
dar = np.array([[4,5,23,521],[789,524,2,4],[5,7,80,1]])
print(dar)
'''
[[  4   5  23 521]
 [789 524   2   4]
 [  5   7  80   1]]
'''
print(np.sort(dar)) #  dar을 사용해서 정렬된 별도의 배열 결과를 만듦
'''
[[  4   5  23 521]
 [  2   4 524 789]
 [  1   5   7  80]]
'''
print(np.sort(dar, axis=0))
'''
[[  4   5   2   1]
 [  5   7  23   4]
 [789 524  80 521]]
'''

# 정렬하면 해당 배열의 구조를 바꿈 : 사용시 주의 필요함
dar.sort(axis=1) # 해당 배열 자체의 값의 순서를 바꿈
print(dar)
'''
[[  4   5  23 521]
 [  2   4 524 789]
 [  1   5   7  80]]
'''

# argsort() 함수
# 데이터를 정렬한 다음, 인덱스를 출력함
ear = np.array([2,3,4,4,5,5,3,34,7,12,22])
print(ear) # [ 2  3  4  4  5  5  3 34  7 12 22]
far = np.argsort(ear) # 정렬된 index를 반환함 => 인덱서로 이용할 수 있음
print(far) # [ 0  1  6  2  3  4  5  8  9 10  7]
print(ear[far]) # 인덱서로 이용 #[ 2  3  3  4  4  5  5  7 12 22 34]
print(np.sort(ear)) # [ 2  3  3  4  4  5  5  7 12 22 34]

