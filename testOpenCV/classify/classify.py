# path : classify/classify.py
# module : classify.classify
# caffemodel 에서 제공하는 학습된 ai모델을 사용해서, 사진에서 사물을 분류 처리하는 테스트 스크립트
# 분류할 사물의 종류는 클래스파일에 이름이 1000개 자성되어 제공되고 있음
# 구글에서 다운받음 : ai 학습모델파일(.caffemodel), 구성파일(.prototxt), 클래스파일(class_...... .txt) 3개


import numpy as np
import cv2
import sys

filename='space_shuttle.jpg'
# filename='beagle.jpg'
# filename='cup.jpg'
# filename='pineapple.jpg'
# filename='scooter.jpg'


# 실행시 외부에서(cmd | terminal | power shell) 전달오는 인자(파일명.확장자)가 있다면
if len(sys.argv) > 1 : # ... > 실행파일명 전달인자1 전달인자2  ....  엔터
#                                   0       1       2       ...
# 위에 구문을 해석하자면 전달인자가 1개라도 있다면

    filename = sys.argv[1]

img = cv2.imread(filename)  # 파일을 읽어와 봣을때 img를 받지 못했다면
if img is None:
    print('image load failed!')
    sys.exit()

# ai 학습모델 load
net = cv2.dnn.readNet('bvlc_googlenet.caffemodel', 'deploy.prototxt')
# 매개변수는 모델파일명 구성파일명 2개임

if net.empty():  # net이 비어있냐 # 다운은 받았는데 모델이 비어 있을 수도 있다
    print('dnn model load failed!')
    sys.exit()

# 분류할 사물이름이 등록된 클래스이름 파일 읽어들이기
classNames = None
with open('classification_classes_ILSVRC2012.txt','rt') as f:  # 파일 읽기
    classNames = f.read().rstrip('\n').split('\n')
# print(classNames) # 읽어들인 파일 확인

# ai 모델 실행 <= 읽어들인 이미지 파일을 적용
inputBlob = cv2.dnn.blobFromImage(img, 1, (224, 224), (104,177,123))
# scalefator : 불러올 데이터 사이즈(백분율), size : 창크기, mean : 중간값
# size, mean => 모델이 정한 size, mean 값을 확인하고 적용함
net.setInput(inputBlob,'data')
prob = net.forward()  # ai 실행 코드
# print('prob : ',prob.shape)
# print('prob : \n',prob)

# 분류 결과 확인 출력
out = prob.flatten()  # 결과물 출력하는 마지막 단계
classid = np.argmax(out) # 일치율이 제일큰 결과값을 출력
confidence = out[classid]

# 결과 문장 출력
text = '%s (%4.2f%%)' % (classNames[classid], confidence*100)
cv2.putText(img, text, (10,30), cv2.FONT_HERSHEY_SIMPLEX,
            0.8, (0,255,255), 1,cv2.LINE_AA)

cv2.imshow('img', img)
cv2.waitKey() # 빈괄호 아무키가 눌리기 전까지 대기
cv2.destroyAllWindows()