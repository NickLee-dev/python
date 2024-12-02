# path : numpy_test2.py
# module : numpy_test2

# numpy 는 ndarray 클래스 사용함 : C언어로 만든 내부 로직을 제공함
# type 을 확인하면 배열의 자료형은 numpy.ndarray
# ndarray : N-Dimension Array / N차원 배열
# 1차원부터 다차원 배열을 다룰 수 있음

import numpy as np

# 2차원 배열 만들기
# 1차원 배열 여러개(가진 값 갯수가 같아야 함)를 하나로 묶으면 => 2차원 배열
# 1차원 배열 == 백터(Vector)
# 2차원 배열 == 매트릭스(Matrix) : 행과 열로 구성된 행렬 형태
# [[...],[...],[...],[...],[...],......] : list of list 형태임
tar = np.array([[0,1,2],[3,4,5]]) # 2행 3열 matrix
print(tar)
'''
[[0 1 2]
 [3 4 5]]
'''
print(len(tar))         # 행갯수 : 2
print(len(tar[0]))      # 0행 안의 값 갯수(열갯수)
print(tar[0]*tar[1])    # [ 0  4 10]

# 리스트일 경우
tar2 = [[0,1,2],[3,4,5]]
print(tar2) # [[0, 1, 2], [3, 4, 5]]
# print(tar2[0]*tar2[1])  # 에러

# 2차원배열의 각 값에 접근 : 배열변수[행순번][열순번]
# 행(row) : 세로방향 ( 줄, 높이, height )
# 열(column) : 가로방향 ( 칸, 너비, width )
# 2중 for문으로 각 인덱스 위치의 값을 처리함
for row_index in range(len(tar)):           # 0,1 : 행 반복
    for col_index in range(len(tar[row_index])):    # 0,1,2 : 열 반복
        print('tar[{}][{}] : {}'.format(row_index,col_index,tar[row_index][col_index]))

# 3차원배열 만들기
# 값의 종류가 같고, 행과 열 갯수가 같은 2차원 배열들의 묶음
# 면(깊이, depth, z축, channal), 행(줄, row, y축, height), 열(칸, column, x축, width)
thar = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],  #0면
                 [[13,14,15,16],[17,18,19,20],[21,22,23,24]]]) #1면
print(thar)
'''
[[[ 1  2  3  4]
  [ 5  6  7  8]
  [ 9 10 11 12]]

 [[13 14 15 16]
  [17 18 19 20]
  [21 22 23 24]]]
'''
print(len(thar))    # 면갯수 : 2
print(len(thar[0]))  # 0면안의 행 갯수 : 3
print(len(thar[0][0]))  # 0면안의 0행안의 열갯수 : 4

# 3차원 배열 안의 각 값을 다루려면, 배열변수[면순번][행순번][열순번]
# 3중 for문 사용해야 함
for didx in range(len(thar)):  # 면 반복 : 0,1
    for ridx in range(len(thar[didx])): # 행 반복 : 0,1,2
        for cidx in range(len(thar[didx][ridx])): # 열 반복 : 0,1,2,3
            print('thar[{}][{}][{}] : {} '.format(didx,ridx,cidx,thar[didx][ridx][cidx]))
        print()
    print("=============================================================")
# for ------------------------------------------------------------------------------

# 배열의 차원(ndim)과 크기(shape) 알아내기
# 배열변수.ndim, 배열변수.shape
print(tar.ndim)         # 2
print(tar.shape)        # (2, 3)
print(thar.ndim)        # 3
print(thar.shape)       # (2, 3, 4)

# 1차원 배열의 ndim, shape 확인
ar = np.array([1,2,3])
print(ar.ndim)      # 1
print(ar.shape)     # (3,)

# 배열의 인덱싱 : 값에 접근하기 위한 인덱스를 표시
# 1차원배열의 인덱싱은 리스트와 같음
print('index 1 : ', ar[1])  # index 1 :  2
print('뒤에서부터 첫번째 위치의 값 : ', ar[-1])     # 뒤에서부터 첫번째 위치의 값 :  3

# 2차원배열의 인덱싱 : 배열변수[행순번][열순번]
# 콤마(,)를 이용할 수도 있음 : 배열변수[행순번,열순번] <= 축(axis) 이라고 함
# 행(x축), 열(y축)이 됨
print('0행0열의 값 : ',tar[0][0], tar[0,0])                     # 0행0열의 값 :  0 0
print('1행 0열의 값 : ',tar[1][0], tar[1,0])                    # 1행 0열의 값 :  3 3
print('마지막행, 마지막열의 값 : ', tar[-1][-1], tar[-1,-1])      # 마지막행, 마지막열의 값 :  5 5