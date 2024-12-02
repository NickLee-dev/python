# housing.py
# 보스톤 주택가격 예측하는 딥러닝 모델 설계 및 테스트

import pandas as pd  # 전처리용
import matplotlib.pyplot as plt # 그래프 출력
import seaborn as sns #
from time import time # 시간관련

# from tensorflow.keras.models import Sequential
import tensorflow as tf
# pip install tensorflow==2.12.0 으로 재 설치할 것

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

# 하이퍼 파라미터 (모델링 작업에 사용할때 변수와 값들)
# 모델에 사용할 핵심 값들을 변수로 선언하고 사용하면 편리함
M_EPOCH = 500 # 학습할 훈련 횟수 (정확도와 오차율(손실율, error, loss) 판단 기준임)
# M_EPOCH = 0 # 오차율 증가됨
# M_EPOCH = 2000  # 500 : 0.19 3.5초 , 2000 : 0.19 13.2초
# DNN 딥러닝 학습 시작
# 총 딥러닝 학습시간 : 3.4초
# DNN 평균제곱오차(MSE) : 0.13
# DNN 딥러닝 학습 시작
# 총 딥러닝 학습시간 : 13.2초
# DNN 평균제곱오차(MSE) : 0.12
M_BATCH = 64  # 가중치를 적용할 샘플의 갯수 (학습 시간 판단 기준임)
# M_BATCH = 16 # 64 : 0.19 3.5초, 16 : 0.15 26.8초
# M_BATCH = 64 # 354 : 0.10 6.4초

# 데이터 준비--------------

# 데이터 파일 읽기 -------------------
# 결과형은 pandas.DataFrame 이어야 한다.
raw = pd.read_csv('./data/housing.csv')
heading=['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','LSTAT','MEDV']

# 읽어들인 데이터 확인
print('원본 데이터 샘플 10개 출력 확인')
print(raw.head(10))

# 원본 데이터 통계
print(raw.describe())

# Z-점수 정규화 : 13개 항목의 기록된 값들의 분포 범위가 제각각임 => 비슷한 값의 범위로 조정
# 예 : a항목은 값이 1~100, b항목은 0.1~1.0 , c항목은 -30~30 으로 값이 분포된 경우
# 모든 항목의 값들을 -1 ~ 1 상이의 값으로 통일시킨다는 개념임
# 결과는 numpy 의 n-차원 행렬임
scaler = StandardScaler()
Z_data = scaler.fit_transform(raw) # 계산 결과가 컬럼라벨이 없는 데이터로만 구성된 행렬

# numpy --> pandas 로 전환(matrix -> DataFrame)
# heading(컬럼라벨) 이용함
Z_data = pd.DataFrame(Z_data,columns=heading)

# 정규화된 데이터 출력 확인
print(Z_data.head(10))

# 정규화된 데이터 통계
print(Z_data.describe())

# 데이터 입력과 출력, 학습용, 평가용으로 분리
print('분리전 데이터 모양 : ', Z_data.shape)
# 입력과 출력(이미지와 연결된 라벨데이터임)으로 분리
X_data = Z_data.drop('MEDV',axis=1)  # 'MEDV' 을 제외한 모든 값(12열)
Y_data = Z_data['MEDV'] # 'MEDV' 컬럼값들(1열)

# 학습용, 평가용으로 분리
X_train, X_test, Y_train, Y_test = train_test_split(X_data, Y_data, test_size=0.3)


print('학습용 입력 데이터 모양 : ', X_train.shape)
print('학습용 출력 데이터 모양 : ', Y_train.shape)
print('평가용 입력 데이터 모양 : ', X_test.shape)
print('평가용 출력 데이터 모양 : ', Y_test.shape)

# box plot (상자 그래프) 출력
sns.set(font_scale=1)
sns.boxplot(data=Z_data,palette='dark')
#sns.boxplot(data=raw,palette='dark')
plt.show()

# 인공 신경망 설계 구현

# 케라스 DNN 구현
model = Sequential()
input = X_train.shape[1] # 입력층 뉴런 12개 지정
model.add(Dense(200,activation='relu',input_dim=input))
model.add(Dense(1000,activation='relu'))
# 히든 레이어 2개 추가함
# model.add(Dense(500,activation='relu'))
# model.add(Dense(500,activation='relu'))
# 학습시간 늘어남, 오차율 늘어남
model.add(Dense(1))

print('DNN 요약')
model.summary()

# 인공신경망 학습

# 최적화 함수 (가중치 보정)와 손실 함수(오차율) 지정
model.compile(loss='mse',optimizer='sgd')
# sgd : 경사하강법(gradient descent)
# Gradient Descent 방법은 1차 미분계수를 이용해 함수의 최소값을 찾아가는 iterative 한 방법임
# 머신러닝 및 딥러닝 알고리즘을 학습시킬 때 사용하는 방법중 하나임
# 1차 근사값 발견용 최적화 알고리즘임
# mse : 평균제곱오차(Mean Square Error)
# 단순히 실제 데이터와 예측 데이터 편차의 제곱합이었던 오차제곱합(SSE)을
# 데이터의 크기로 나눠 평균으로 만든 것
# 머신러닝 뿐만 아니라 영상처리 영역에서도 자주 사용되는 추축값에 대한 정확성 측정 방법임
# 간단히 하면, 오차의 제곱에 대해 평균을 취한 것임
# 0에 가까울수록 원본과의 오차가 적은 것이므로 추측한 값의 정확성이 높은 것임

print('DNN 딥러닝 학습 시작')
begin = time()

model.fit(X_train,Y_train,epochs=M_EPOCH,batch_size=M_BATCH, verbose=0)
# verbose mode : 0 (slient : 안보임), 1(progress bar), 2(one line per epoch)
# 학습 진행을 표시하는 모드임
# betch_size : 몇개의 샘플로 가중치를 갱신할것인지를 설정
# epochs : 전체 데이터셋을 몇 번 반복 학습할지 횟수를 설정

end = time()
print('총 딥러닝 학습시간 : {:.1f}초'.format(end-begin))

#  인공신경망 모델 평가 및 활용

# 신경망 모델 평가 및 손실값 계산
loss = model.evaluate(X_test,Y_test,verbose=0)
print('DNN 평균제곱오차(MSE) : {:.2f}'.format(loss))

# 신경망 활용 및 산포도 출력
pred = model.predict(X_test)
sns.regplot(x=Y_test, y=pred) # 회귀선 그래프

plt.xlabel('정답')
plt.ylabel('예측값')
plt.show()

# 주택가격(MEDV) 확인
# print(pd.DataFrame(pred).head(10))

