# numpy_test8.py

import numpy as np

# 배열 연결
# 두 개 이상의 배열들을 연결(concatenate) 해서 하나의 큰 배열을 만듦
# 사용 함수 : hstack, vstack, dstack, r_, c_, tile

# hstack (horizental stack)
# 행의 갯수가 같은 2차원 배열들을 옆으로(가로로, 수평) 합칠 때 사용 => 열 갯수가 늘어나게 됨
ar1 = np.ones((2,3))
print(ar1)
'''
[[1. 1. 1.]
 [1. 1. 1.]]
'''
ar2 = np.zeros((2,2))
print(ar2)
'''
[[0. 0.]
 [0. 0.]]
'''
print(np.hstack([ar1,ar2]))
'''
[[1. 1. 1. 0. 0.]
 [1. 1. 1. 0. 0.]]
'''

# vstack(vertical stack)
# 열의 갯수가 같은 2차원 배열들을 위 아래로(세로로, 수직) 합칠 때 사용 => 행 갯수가 늘어나게 됨
ar3 = np.ones((2,3))
print(ar3)
'''
[[1. 1. 1.]
 [1. 1. 1.]]
'''
ar4 = np.zeros((3,3))
print(ar4)
'''
[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
'''
print(np.vstack([ar3,ar4]))
'''
[[1. 1. 1.]
 [1. 1. 1.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
'''

# dstack (depth stack)
# 행과 열이 같은 2차원 배열 여러 개를 깊이(depth, z축, 채널) 방향으로 합칠 때 사용함
# a행 b열 배열들의 갯수가 n개 합치면, 결과는 a면b행n열 이 됨
ar5 = np.ones((3,4))
print(ar5)
'''
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]]
'''
ar6 = np.zeros((3,4))
print(ar6)
'''
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
'''
bar = np.dstack([ar5,ar6])
print(bar.shape)  # (3, 4, 2)
print(bar)
'''
[[[1. 0.]
  [1. 0.]
  [1. 0.]
  [1. 0.]]

 [[1. 0.]
  [1. 0.]
  [1. 0.]
  [1. 0.]]

 [[1. 0.]
  [1. 0.]
  [1. 0.]
  [1. 0.]]]
'''

# stack() 함수 : 기본적으로 dstack() 과 같음
bar2 = np.stack([ar5,ar6], axis=1) # 합쳐지는 갯수(2개)를 행에 적용하라는 뜻임
print(bar2.shape)  # (3, 2, 4)
print(bar2)
'''
[[[1. 1. 1. 1.]
  [0. 0. 0. 0.]]

 [[1. 1. 1. 1.]
  [0. 0. 0. 0.]]

 [[1. 1. 1. 1.]
  [0. 0. 0. 0.]]]
'''

bar2 = np.stack([ar5,ar6])  # == axis = 0
print(bar2.shape)  # (2, 3, 4)
print(bar2)
'''
[[[1. 1. 1. 1.]
  [1. 1. 1. 1.]
  [1. 1. 1. 1.]]

 [[0. 0. 0. 0.]
  [0. 0. 0. 0.]
  [0. 0. 0. 0.]]]
'''

bar2 = np.stack([ar5,ar6], axis=2) # 합쳐지는 갯수(2개)를 열에 적용하라는 뜻임
print(bar2.shape)  # (3, 4, 2)
print(bar2)
'''
[[[1. 0.]
  [1. 0.]
  [1. 0.]
  [1. 0.]]

 [[1. 0.]
  [1. 0.]
  [1. 0.]
  [1. 0.]]

 [[1. 0.]
  [1. 0.]
  [1. 0.]
  [1. 0.]]]
'''

# r_ : hstack 과 유사하게 좌우로 배열을 합침
# 함수인데 소괄호(parenthesis, ())를 사용하지 않고, 인덱싱처럼 대괄호(braket,[])를 사용함
# 특수 메서드라고 함, 인덱서라고 함
# np.r_[배열생성구문 | 배열변수, 배열생성구문 | 배열변수,..........]
bar3 = np.r_[np.array([1,2,3]), np.array([4,5,6])]
print(bar3.shape) # (6,)
print(bar3) # [1 2 3 4 5 6]

# c_ : indexer 임
# 배열의 차원을 증가시킨 후, 좌우로 연결하는 인덱서임
# 1차원 배열을 연결하면 2차원배열이 됨 : 배열의 값 갯수가 행, 합쳐지는 배열갯수가 열이 됨
bar4 = np.c_[np.array([1,2,3]), np.array([4,5,6])]
print(bar4.shape) # (3, 2)
print(bar4)
'''
[[1 4]
 [2 5]
 [3 6]]
'''

# tile() 함수 : 배열을 지정한 횟수만큼 복사해서 연결함
# tile(배열변수, 열반복횟수), tile(배열변수, (행반복, 열반복))
bar5 = np.array([[1,2,3],[4,5,6]]) # 2행 3열
bar6 = np.tile(bar5,2)  # 각 행의 열이 2번 반복됨 => 2행 6열
print(bar6.shape) # (2, 6)
print(bar6)
'''
[[1 2 3 1 2 3]
 [4 5 6 4 5 6]]
'''

bar7 = np.tile(bar5,(3,2))
print(bar7.shape)   # (6, 6)
print(bar7)
'''
[[1 2 3 1 2 3]
 [4 5 6 4 5 6]
 [1 2 3 1 2 3]
 [4 5 6 4 5 6]
 [1 2 3 1 2 3]
 [4 5 6 4 5 6]]
'''

# 2차원 그리드 포인트 생성
# 변수가 2개인 2차원 함수의 그래프를 그리거나 표를 작성하려면,
# 2차원 영역에 대한 (x,y)좌표값 쌍, 즉 그리드 포인트(grid point)가 필요함
# meshgrid() 함수로 x,y 좌료를 구성할 배열을 생성할 수 있음

# 예 : x 값이 0, 1, 2 이고, y 값이 0, 1, 2, 3, 4 라면, meshgrid()로 사각형 영역을 구성할
# 가로축의 점들과 세로축의 점들을 조합해서 결과로 그리드 포인트 x 행렬과  y 행렬을 만들어줌
x = np.arange(3)
print(x) # [0 1 2]
y = np.arange(5)
print(y) # [0 1 2 3 4]

metrix_x, metrix_y = np.meshgrid(x,y)
print(metrix_x)
print(metrix_y)

# (x, y) 조합 : 리스트 내포 사용
grid_xy = [list(zip(x,y)) for x,y in zip(metrix_x,metrix_y)]
print(grid_xy)