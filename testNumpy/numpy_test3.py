# numpy_test3.py

import numpy as np

# 데이터샘플링(표본추출) : choice() 함수 사용
# np.random.choice(a, size=None, replace=True, p=None)
# a : 배열변수(배열값 사용) 정수숫자(range(정수숫자) 범위의 랜덤값 만들어줌) ex: a값이 10이면 0~9값 랜덤출력
# size : 정수숫자, 추출할 값 갯수 지정
# replace : True|False, 같은값 여러번 선택 가능(True) | 같은값 여러번 선택 불가능(False)
# p : 배열변수나 배열 표기, 각 값의 선택확률을 지정(값의 합계가 1이어야함(100%로 맞추기)

ch1 = np.random.choice(5,5,replace=False) # shuffle 과 같음
# 0~4까지의 값을 생성해서 5개를 추출 (중복 선택 안됨)
print(ch1)
print(type(ch1))    # <class 'numpy.ndarray'>  # 배열임

ch2 = np.random.choice(5,3,replace=False)
print(ch2)
print(type(ch2))

ch3 = np.random.choice(5,10)
# 0~4 까지의 값을 생성해서 10개를 추출(중복선택) replace 매개변수 미사용시 True
print(ch3)
print(type(ch3))

ch4 = np.random.choice(5,10,p=[0.1,0,0.3,0.6,0])
# 0~4 까지의 값을 생성해서 10개를 추출 (중복선택)
# p=[0.1(인덱스0의 선택 확률),0(인덱스1의 선택 확률),0.3(인덱스2의 선택 확률),0.6(인덱스3의 선택 확률),0(인덱스4의 선택 확률)]
print(ch4)
print(type(ch4))

# numpy 에서 난수 생성함수 3가지 제공함 : rand, randn, randint
# rand(갯수) : 0.0 <= 난수 < 1.0 사이의 균일한 확률 분포로 실수 난수를 갯수만큼 발생함
r1 = np.random.rand(10)     # 1차원 배열로 10개
print(type(r1))     # <class 'numpy.ndarray'>
print(r1)           # [0.62424127 0.60794165 0.16791126 0.81961549 0.20620459 0.09331151
                    # 0.23113099 0.21476453 0.31465562 0.97500588]

r2 = np.random.rand(3,5)    # 2차원 배열로 3행 5열로 15개의 난수 발생함
print(type(r2)) # <class 'numpy.ndarray'>
print(r2.shape) # (3, 5)
print(r2)
'''
[[0.64880216 0.56305739 0.75670409 0.27769333 0.65556369]
 [0.13660267 0.41333596 0.05736586 0.88012854 0.38650091]
 [0.83633172 0.57959875 0.35184202 0.41659411 0.90549136]]
'''

# randn(갯수)
# 기댓값이 0이고 표준편차가 1인 표준정규분포를 따르는 난수를 생성함
# 기댓값 : 가장 대표적인 평균값임, 그래프의 가운데 값임, 0을 기준으로 양수, 음수가 대칭적으로 발생
#           즉, 0에 가까운 값들이 많이 발생하는 형태임
# 표준편차 : 숫자들이 기대값에서 떨어져 있는 정도, 즉 1만큼 떨어진 값으로 발생한다는 뜻임
# 표준정규분포 : 기대값 0에 값이 많이 몰려있고, 양 옆으로 갈수록 점점 낮아지는 종모양의 그래프가 됨
r3 = np.random.randn(10)    # 1차원배열 10개의 값
print(type(r3))     # <class 'numpy.ndarray'>
print(r3.shape)     # (10,)
print(r3)           # [-0.12268415  0.90127934  0.69791621  0.93120844  0.53881854  1.76211282
                    #  -1.96105694  1.00362054 -2.07229103 -1.62514025]

r4 = np.random.randn(3,5)   # 2차원 배열 3행 5열로 값 15
print(type(r4))
print(r4.shape)
print(r4)

# randint(low, high=None, size = None)
# low <= 난수 < high 사이의 size 갯수 만큼의 정수 난수를 발생시킴
# high 가 생략되면 0~low 까지의 범위에서 값이 발생함
r5 = np.random.randint(10, size=10)    # 0~10 사이의 정수 10개 발생
print(r5)

r6 = np.random.randint(10,20,size=10)   # 10~ 20 사이의 정수 10개 발생
print(r6)
print(type(r6))
print(r6.shape)

r7 = np.random.randint(10,20,size=(3,5))   # 10~ 20 사이의 정수 15개 발생, 2차원배열
print(r7)
print(type(r7))
print(r7.shape)

