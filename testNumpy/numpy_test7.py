# numpy_test7.py
# 배열의 차원 변환과 관련된 함수 및 속성 테스트

import numpy as np

# 전치연산 : T 속성 사용함 => 2차월배열.T
# 2차원배열의 행과 열을 바꿀 때 사용함 : 2행3열.T => 3행2열이 됨
ar = np.array([[1,2,3],[4,5,6]])
print(ar)
print(ar.shape) # (2,3)
print(ar.T)
print(ar.T.shape) # (3,2)

# 1차원 배열을 다차원 배열로 바꿀 수 있음 : reshape() 함수 사용함 => 전체 크기(갯수)는 바뀌지 않음
ar = np.arange(12) # 0~11로 초기화됨 : 12개
print(ar)  # [ 0  1  2  3  4  5  6  7  8  9 10 11]
print(len(ar)) # 12
# 3행 4열의 2차원 배열로 바꾸기
bar = ar.reshape(3,4)
print(bar)
print(len(bar) * len(bar[0])) # 3행 * 4열 => 12

# reshape() 사용시 면, 행, 열의 갯수를 지정하지 않고 -1 로 표기할 수 있음
# -1로 표시된 항목은 계산에 의해 갯수가 결정됨
bar2 = ar.reshape(3,-1)
print(bar2)
print(bar2.shape)   # (3, 4)

# 1차원 배열을 3차원 배열로 바꾸기
bar3 = ar.reshape(2,2,-1)
print(bar3)
print(bar3.shape)  # (2, 2, 3)

bar4 = ar.reshape(2,-1,2)
print(bar4)
print(bar4.shape)  # (2, 3, 2)

# flatten() 함수, ravel() 함수
# 다차원배열을 1차원배열로 바꿀 때 사용함
print('bar : ', bar.shape)  # bar :  (3, 4)
print(bar.flatten())    # [ 0  1  2  3  4  5  6  7  8  9 10 11]  2차원배열 => 1차원배열
print(bar.ravel())  # [ 0  1  2  3  4  5  6  7  8  9 10 11]  2차원배열 => 1차원배열

print('bar3 : ', bar3.shape)  # bar :  bar3 :  (2, 2, 3)
print(bar3.flatten())    # [ 0  1  2  3  4  5  6  7  8  9 10 11]  3차원배열 => 1차원배열
print(bar3.ravel())  # [ 0  1  2  3  4  5  6  7  8  9 10 11]  3차원배열 => 1차원배열

# newaxis 함수
# 배열의 차원을 1증가 시키는 함수
# 1차원 배열 => 2차원 배열로, 2차원 배열 => 3차원 배열로
# 값의 갯수가 5개인 1차원 배열을 2차원 배열로 바꿀 때 (5,1) | (1,5)로 변경 가능함
# 총 값의 갯수가 5개지만, 1차원배열과 2차원배열 (1행,5열)은 엄연히 다른 배열 객체임
xar = np.arange(5)  # 0~4 초기화 하는 1차원 배열 생성
print(xar)  # [0 1 2 3 4]
print(xar.shape) # (5,)
print(xar.reshape(1,5))  # [[0 1 2 3 4]]
print(xar.reshape(5,1))
'''
[[0]
 [1]
 [2]
 [3]
 [4]]
'''

# 총 값의 갯수가 같은 배열에 대해 차원만 1 증가시키는 경우, newaxis 사용할 수 있음
print(xar[:, np.newaxis])   # 열이 행이 됨
print(xar[:, np.newaxis].shape)   # 5열 -> 5행 1열이 됨
