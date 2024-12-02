# tensor_test.py

# 텐서플로우 불러오기
import tensorflow as tf


# MNIST(손글씨 숫자(0-9) 이미지 데이터셋) 데이터를 사용한 DNN 학습예 (딥뉴럴네트워크)
# 손글씨 숫자 이미지 분류하기 --------------------------------------
# MNIST 손글씨 데이터 가져오기
# import tensorflow.keras # MNIST 관련 에러 발생시에 추가함
mnist = tf.keras.datasets.mnist

# MNIST 4분할 데이터로 나누기 처리
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()
# 훈련용 과 테스트용으로 구분
# X 입력데이터 Y 출력데이터
print('학습용 입력 데이터 모양 : ', X_train.shape) # 학습용 입력 데이터 모양 :  (60000, 28, 28)
print('학습용 출력 데이터 모양 : ', Y_train.shape) # 학습용 출력 데이터 모양 :  (60000,)
print('평가용 입력 데이터 모양 : ', X_test.shape) # 평가용 입력 데이터 모양 :  (10000, 28, 28)
print('평가용 출력 데이터 모양 : ', Y_test.shape) # 평가용 출력 데이터 모양 :  (10000,)

import matplotlib.pyplot as plt

plt.imshow(X_train[0],cmap='gray')
#plt.show()

print('첫번째 학습용 데이터 입력값 : ', X_train[0])
print('첫번째 학습용 데이터 출력값 : ', Y_train[0])

# 이미지 데이터 [0,1] 스케일잉 : 값의 범위를 축소함
# 각 픽셀의 색상값이 0 ~ 255로 기록되어 있음 => 0과 1사이의 값으로 바꿈
X_train = X_train/255.0
X_test = X_test/255.0

print('첫번째 학습용 데이터 입력값 : ', X_train[0])
print('첫번째 학습용 데이터 출력값 : ', Y_train[0])

# 인공신경망 구현
# 신경망 층(레이어,layer)을 순서대로 배치하는 모델 객체임
model = tf.keras.models.Sequential() # 레이어 구성때 순차 처리하는 모델
# 텐서플로우 안의 케라스가 제공하는 레이어 사용을 선언함
layers = tf.keras.layers # 레이어를 구축하는 함수

# 준비된 모델 객체에 레이어를 하나씩 추가(연결)해 나감 => 모델 설계
# 입력층 (input layer)
model.add(layers.Flatten(input_shape=(28,28))) # Flatten : 입력용 레이어로 주로 사용
model.add(layers.Dense(128,activation='relu')) # 히든 레이어 1
model.add(layers.Dropout(0.2)) # 히든 레이어 2
model.add(layers.Dense(10, activation='softmax')) # 출력층 (output layer)

# 인공신경망 요약
model.summary() # 요약보고서가 나옴

# 인공신경망 설계된 모델에 대한 환경 설정
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

# 설계된 모델을 가지고 인공신경망 학습 (Training) : 학습 횟수(epoch)
model.fit(X_train,Y_train,epochs=5) # 5번 학습진행
# 손글씨 숫자 이미지 분류하기 ----------------------------------------------------

# 모델 평가 (인공신경망 평가)
model.evaluate(X_test,Y_test)

# 완성된 모델에 분류해 놓은 테스트 데이터를 적용해서, 정확도가 유지 되는지 확인
# 인공신경망 예측
pick = X_test[9999].reshape(1,28,28) # 면 행 열 # 테스트할 손글씨 이미지 하나 골라냄
pred = model.predict(pick) # 골라낸 테스트 이미지를 모델에 적용함
answer = tf.argmax(pred, axis=1)  # 평가된 각 손숫자의 확률값 중 가장 큰 값의 인덱스를 리턴함

print('인공신경망 추측 결과(원본) : ', pred)
print('인공신경망 추측 결과(해석) : ', answer)
print('정답 : ',Y_test[9999])
