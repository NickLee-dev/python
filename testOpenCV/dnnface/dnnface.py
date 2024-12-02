# path : dnnface/dnnface.py
# module : dnnface.dnnface

# 딥러닝 ai 학습모델 다운받아서, 카메라 영상에서 얼굴 인식 처리 테스트 스크립트

import cv2
import numpy as np
import sys

# 영상 이미지에서 얼굴을 인식하는 ai 학습모델 (caffemodel 에서 다운받음)
model = 'res10_300x300_ssd_iter_140000_fp16.caffemodel'  # 학습모델 파일 이름 변수로 지정
config = 'deploy.prototxt'   #  구성파일 이름 변수로 지정

# 화면 캡처
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('Cannot open camera')
    sys.exit()

# opencv 가 제공하는 dnn 모델 사용
net = cv2.dnn.readNet(model, config) # dnn 딥러닝 신경망
if net.empty(): # 신경망을 오픈 못 시켰다면
    # print('Cannot load network')
    sys.exit()

# 카메라 영상에서 얼굴 인식 출력 확인
while True:
    ret, frame = cap.read() # 카메라 자료 불러오기  # frame이 영상정보
    if not ret:    # ret(리턴값)이 false이면 카메라로 읽어오는걸 실패했다는 의미
        break

    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104,177,123))
    # print(blob)
    net.setInput(blob)
    detect = net.forward()  # ai 실행
    # print('detect shape : ', detect.shape)
    # print(frame.shape)
    (h, w) = frame.shape[:2]
    detect = detect[0,0,:,:]

    # 얼굴 위치에서 계산 처리
    for i in range(detect.shape[0]):
        confidence = detect[i, 2]
        if confidence < 0.5:
            break

        x1=int(detect[i,3]*w)
        y1=int(detect[i,4]*h)
        x2=int(detect[i,5]*w)
        y2=int(detect[i,6]*h)

        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)  # 얼굴 위치에 초록색 사각형 선 표시

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == 27:     # 27번키 Esc 키임 # ESC키 누르면
        break
# while --------------------------------------------------

cv2.destroyAllWindows()
