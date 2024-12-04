# airline.py
# RNN 이용한 항공 여행자수 예측하기
# CNN-RNN : 이미지 캡션 달기 AI 프로그램 대회(구글)

# RNN(Recurrent Neural Network, 순환 신경망)
# 앞서의 신경망들은(DNN, CNN) 모두 은닉층에서 활성화함수(relu)를 가진 값들을 출력층으로 내보냄
# (피드 포워드 신경망, Feed Forword 신경망)
# 입력층 --> 히든레이어 (활성화 함수) --> .... --> 출력층

# RNN 은 은닉층의 노드에서 활성화 함수를 통해 나온 결과값을 출력층 방향으로 보내면서
# 다시 다음 은닉층 노드의 입력값으로 보내는 특징이 있음
# 이전 노드의 값을 기억하는 셀(메모리셀, RNN 셀이라고 함)

# 파이썬 패키지 임포트
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from time import time

from pyexpat.errors import XML_ERROR_TEXT_DECL
from sklearn.preprocessing import MinMaxScaler

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import InputLayer, Dense
from tensorflow.keras.layers import LSTM # RNN에 사용되는 저장공간
from tensorflow.python.ops.sparse_ops import sparse_split_v2

# 하이퍼 파라미터
# LSTM 에서 사용할 파라미터
M_PAST = 12
M_SPLIT = 0.8
M_UNIT = 300
M_SHAPE = (M_PAST,1) # (12,1) : 2차원 선언

M_EPOCH = 300 # 모델이 학습할 횟수
M_BATCH = 64 # 가중치 셈플의 갯수 (weight값 조절용 자료수)

np.set_printoptions(precision=3) # 실수형 값 출력시 소수점아래 셋째자리까지 출력을 정함

## 데이터 준비 ##

# 제공된 airline.csv 파일 읽기
# 읽은 결과가 pandas의 DataFrame 형식으로 하려면
raw = pd.read_csv('./data/airline.csv', header=None, usecols=[1])
# usecols : 불러올 파일의 컬럼 인덱스 순번이나 이름 지정
# usecols=[1] : 데이터에서 두번째 열만 읽어들임

# print(raw) :  1번 컬럼값 가져옴
# 데이터프레임 시각화 (시계열데이터 : 시간과 연결된 데이터)
# plt.plot(raw)   # 년-월별 비행기 이용자수
# plt.show()  # 시간이 진행될 수록 증가됨 확인

# 원본 데이터 통계
# print(raw.describe())

# MinMax 데이터 정규화
# MinMaxScaler 는 값의 범위를 조정할 때 사용함
# 모든 데이터를 0과 1사이의 값으로 조정함
# 최소값이 0이고 최대값이 1이됨
scaler = MinMaxScaler()
s_data = scaler.fit_transform(raw)
# print(s_data)
# print(type(s_data)) # <class 'numpy.ndarray'>

# 정규화된 데이터 출력 : array 를 DataFrame 으로 변환함
df = pd.DataFrame(s_data)
# print('정규화된 데이터 샘플 : ', df.head(12))
# print('정규화된 데이터 통계 : ', df.describe())

# 데이터를 13개씩 각 묶음으로 데이터 분할
# 결과형은 list임
bundle=[]
for i in range(len(s_data) - M_PAST):
    bundle.append(s_data[i:i+M_PAST+1])

# 데이터 분할 (년단위로 묶음) 결과 확인
print('총 묶음 갯수 : ', len(bundle))
print('0번째 묶음 : ',bundle[0])
print('1번째 묶음 : ',bundle[1])
print('분할 데이터 타입 : ', type(bundle)) # <class 'list'>

# numpy의 array 로 바꿈
bundle=np.array(bundle)
print('분할 데이터 모양 : ', bundle.shape) # (132, 13, 1) 행렬 132면, 13행, 1열 3차원

# 데이터를 입력과 출력으로 분할함
X_data = bundle[:, 0:M_PAST] # 모든행의 0열에서 ~ 11열(12개)
Y_data = bundle[:, -1] #모든행의 마지막열(12열,1개,13번째 값 시작

# 132개 묶음을  학습용(0.8))과 평가용 (0.2)))으로 분리
split = int(len(bundle)*M_SPLIT)
X_train=X_data[:split] # X_data에서 80%가 학습데이터로 분리
X_test=X_data[split:] # X_data에서 20%가 평가데이터로 분리
Y_train=Y_data[:split] # Y_data 에서 80%가 학습데이터로 분리
Y_test=Y_data[split:] # Y_data 에서 20%가 평가데이터로 분리

# 최종데이터 모양 확인
print('학습용 입력 데이터 모양 : ',X_train.shape)
print('학습용 출력 데이터 모양 : ',Y_train.shape)
print('평가용 입력 데이터 모양 : ',X_test.shape)
print('평가용 출력 데이터 모양 : ',Y_test.shape)

## 인공 신경망 구축 및 학습 ##

# RNN 구현
# 케라스 RNN은 2차원 입력만 허용
model = Sequential()
model.add(InputLayer(input_shape=M_SHAPE))
model.add(LSTM(units=M_UNIT))
model.add(Dense(1, activation='sigmoid'))

print('RNN 요약')
model.summary()

## 인공 신경망 학습(훈련) ##
# 최적화 함수와 손실 함수 지정
model.compile(optimizer='rmsprop', loss='mse')
# 최적화 알고리즘 : adam, momentum, adagrad, rmsprop 등
# rmsprop : 기울기를 단순 누적하지 않고 지수 가중 이동 평균을 사용해서
#           최신 기울기들이 더크게 반영하도록 하는 알고리즘임

# 손실함수 : 실제 값과 예측값의 차이를 계산하는 함수
# mse (평균 제곱 오차), crossEntropy(cee, 교차 엔트로피 오차) 함수

begin = time()
print('학습 시작')
model.fit(X_train, Y_train, epochs=M_EPOCH, batch_size=M_BATCH,verbose=2)
end = time()
print('총 학습 시간 : {:.1f}초'.format(end-begin))

## 인공신경망 평가 ##
# RNN 평가
loss = model.evaluate(X_test, Y_test, verbose=2)

print('최종 MSE 손실값 : {:.3f}'.format(loss))

## RNN 예측값 확인 (테스트) ##
pred = model.predict(X_test)
# (0,1) 값을 원래 값으로 변환 : inverse_transform()
pred = scaler.inverse_transform(pred)
# 1차원배열로, 정수값으로 변환
pred = pred.flatten().astype(int)
print('예측 결과 데이터 : ', pred)

# 실제 데이터도 역전환 : 0~1 값에서 실제값으로 변환
truth = scaler.inverse_transform(Y_test)
truth = truth.flatten().astype(int)
print('실제 데이터 : ', truth)

# 선 그래프(line plot)로 시각화 처리
axes = plt.gca() # 그래프 영역
axes.set_ylim([0,650])
sns.lineplot(data=pred,label='pred', color='blue') # 예측 데이터
sns.lineplot(data=truth,label='truth', color='red') # 실제 데이터
plt.show()