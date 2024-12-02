# numpy_test1.py
# 패키지 추가 설치 필요 : pip install numpy
# numpy 모듈 : 배열(행렬, matrix)을 다루는 모듈임

'''
배열의 특징 (리스트와 다른 점)
1. 처음부터 저장할 갯수를 저장 (리스트는 저장 갯수에 제한 없음)
2. 한 가지 종류만 저장함 (리스트는 여러 종류를 저장함)
3. 리스트와 동일하게 저장 순번(index)를 사용함
'''
from os import getcwd

import numpy as np

# 1차원 배열 다루기 : numpy array([한가지 종류로만 저장된 리스트]) 함수 사용
# 리스트를 배열로 바꿈
# 배열변수 = np.array([list])
# 배열변수는 할당된 배열공간의 주소를 가짐 : 배열 레퍼런스임 (주소 저장 변수)
# 배열로 만들 리스트는 정수|실수 값들로만 구성되어야 함
ar = np.array([1,2,3,4,5,6,7,7,6])
print(ar)   # [1 2 3 4 5 6 7 7 6]
print(type(ar))  # <class 'numpy.ndarray'>  => n차원 배열이다라는 뜻임
print(len(ar))  # 9
print(ar.dtype) # int64   => 값들의 자료형 출력

# 배열은 백터화(각 인덱스값 별로) 연산이 가능하다.
# 리스트일 때의 백터화 연산처리 예 :
datalist=[1,2,3,4,5,6,7,7,6]
print(type(datalist))  # <class 'list'>

# 리스트 안의 각 값을 2배로 증가처리한다면
double_datalist = []  # list()
for data in datalist:
    double_datalist.append(data*2)
print(double_datalist)  # [2, 4, 6, 8, 10, 12, 14, 14, 12]

# 위의 처리를 배열로 바꿔서 백터화 연산을 처리한다면
ar_datalist = np.array(datalist)
print(ar*2)  # [ 2  4  6  8 10 12 14 14 12] # ndarray 에서 내부적으로 각 인덱스 값들에 대해 *2 연산이 수행됨

# 리스트에 *2 를 적용하면
print(datalist*2)   # [1, 2, 3, 4, 5, 6, 7, 7, 6, 1, 2, 3, 4, 5, 6, 7, 7, 6] # 리스트 2번 출력됨

# 배열의 백터와 연산은 비교연산, 논리연산, 산술연산이 가능
# ndarray 클래스에 각 연산자에 대한 연산자 오버로딩 함수가 작성 제공이 되고 있음
ar1 = np.array([1,2,3])
br1 = np.array([10,20,30])

print(2*ar1+br1)  # [12 24 36]  # 2 * ar1[0] + br1[0], 2*ar1[1] + br1[1], 2*ar1[2]+br1[2]
print(ar1 == 2)  # [False  True False]  # ar1[0]==2 : false, ar1[1]==2 : true, ar1[2]==2 : false
print(br1 > 10)  # [False  True  True]  # br1[0]>10 : false, br1[1]>10 : true, br1[2]>10 : true
print((ar1 == 2) & (br1 > 10)) # [False  True False]  # [False  True False] & [False  True  True]
print((ar1 == 2) | (br1 > 10)) # [False  True  True]  # [False  True False] | [False  True  True]

# 1차원배열의 각 값에 접근하려면, 배열변수[인덱스순번]
for index in range(0,len(ar)):  # range(start,end) : start ~ end - 1 범위의 값들 , 0 ~ 8
    print(index," : ",ar[index])

