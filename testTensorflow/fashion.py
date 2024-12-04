# fashion.py
# 딥러닝 DNN 적용 패션 아이템 구분하기

import numpy as np
import matplotlib.pyplot as plt
from time import time

from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import f1_score, confusion_matrix

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dropout, Dense
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import InputLayer
from tensorflow.keras.layers import Conv2D, MaxPool2D


# 하이퍼 파라미터
M_EPOCH = 20
M_BATCH = 300

### 데이터 준비 ###
# 데이터 읽어들이기
(X_train,Y_train),(X_test,Y_test) = fashion_mnist.load_data()
# 결과 타입은 numpy 의 n-차원 배열임

# 4분할된 데이터 형태 출력 확인
print('학습용 입력 데이터 모양 : ', X_train.shape)
print('학습용 출력 데이터 모양 : ', Y_train.shape)
print('평가용 입력 데이터 모양 : ', X_test.shape)
print('평가용 출력 데이터 모양 : ', Y_test.shape)

# 샘플 이미지 데이터 출력 확인
print(X_train[0])
plt.imshow(X_train[0], cmap='gray')
plt.show()
print('샘플 데이터 라벨 : ', Y_train[0])

# 샘플 데이터 스케일링 ( 데이터 전처리 ) : [0, 1] <= [0,255] 값 범위의 축소
X_train = X_train / 255.0
X_test = X_test / 255.0

# 스케일링 후 확인
print(X_train[0])
plt.imshow(X_train[0], cmap='gray')
plt.show() # 이미지 그대로 출력됨

# 채널 정보 추가
# 케라스 CNN 에서는 4차원 정보가 필요함 : Tensor 타입임
train = X_train.shape[0] # X_train.shape : [60000,28,28] , 60000 대입됨
X_train = X_train.reshape(train, 28, 28, 1) # 차원 늘림
test = X_test.shape[0] # 10000
X_test = X_test.reshape(test, 28, 28, 1) # 차원 늘림

# Tensor (4차원 매트릭스) 로 변환 후 확인
print(X_train[0]) # 데이터 기록 구조는 변경됨
plt.imshow(X_train[0], cmap='gray')
plt.show() # 이미지 그대로 출력

# 출력 데이터 (라벨 정보 인덱스) : One-hot encoding
# 찾고자 하는 특징값에 1, 아닌 값에 0 처리하는 것임
print('One-hot encoding 전 : ', Y_train[0])
Y_train = to_categorical(Y_train, 10)
print('One-hot encoding 후 : ', Y_train[0])

Y_test = to_categorical(Y_test, 10)
print('학습용 출력 데이터 모양 : ', Y_train.shape)
print('평가용 출력 데이터 모양 : ', Y_test.shape)

## 인공 신경망(순차적 방법))
model = Sequential()
# Sequential 모델 :
# 각 레이어에서 정확히 하나의 입력 텐서와 하나의
# 출력 텐서가 있는 일반 레이어 스택을 구성하는 모델임

# 입력층
model.add(InputLayer(input_shape=(28, 28, 1)))

# 첫번째 합성곱 블럭
# kernel_size : filter 사이즈를 의미함, 2 : (2,2), 5 : (5,5)
# channel 갯수 : 32
model.add(Conv2D(32, kernel_size=2, padding='same', activation='relu'))
model.add(MaxPool2D(pool_size=2))

# 두번째 합성곱 블럭
model.add(Conv2D(64, kernel_size=2, padding='same', activation='relu'))
model.add(MaxPool2D(pool_size=2))

# fully-conneted 층으로 마무리
model.add(Flatten())  # 1차원으로 변환
model.add(Dense(128, activation='relu'))  # 가중치를 적용해서 특징값을 찾음
model.add(Dense(10, activation='softmax'))  # softmax : 클래스 분류 문제에 사용

print('CNN 요약')
model.summary()

## 인공 신경망 학습 ##

# 최적화 함수와 손실 함수 지정
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
begin =time()
print('CNN 학습시작')

model.fit(X_train, Y_train, epochs=M_EPOCH, batch_size=M_BATCH, verbose=1)
end = time()
print('총 합습시간 : {:.1f}초'.format(end - begin))

## 인공 신경망 모델 평가 ##
_, score = model.evaluate(X_test, Y_test, verbose=1)
print('최종 정확도 : {:.2f}%'.format(score*100))

# CNN 예측 평가
pred = model.predict(X_test)
pred = np.argmax(pred, axis=1) # 제일 큰 값(1)의 인덱스 리턴
truth = np.argmax(Y_test, axis=1) # 제일 큰 값(1)의 인덱스 리턴

# 혼동 행력(정확도, 정밀도, 재현율, F1 점수 라고 함)
# 모델의 성능을 평가할 때 사용하는 지표임
print('혼동행렬')
print(confusion_matrix(truth, pred)) # 예측값과 정답 사용
# 실제값과 예측값이 일치할 때 값 출력됨(대각선)

# F1 점수
# 정밀도(precision)와 재현율(recall) 의 조화 평균임
# 모델 예측 성능을 수치화 한 값
# 1에 가깔울수록 모델의 예측성 능력은 좋다임
f1 = f1_score(truth, pred, average='macro')
print('F1 점수 : {:.3f}'.format(f1))

# 결론 : M_EPOCH = 3
# 총 학습 시간 : 39.3초
# 최종 정확도 : 88.73%
# F1 점수 : 0.885

# 실험 : M_EPOCH = 0
# 총 학습 시간 : 0.1초
# 최종 정확도 : 14.11%
# F1 점수 : 0.109  => 0에 가까움 (모델 성능 나쁨)

# 실험 : M_EPOCH = 20
# 총 학습 시간 : 271.7초
# 최종 정확도 : 91.08%
# F1 점수 : 0.911 # 1에 가까움(메돌 성능 아주 좋음)

