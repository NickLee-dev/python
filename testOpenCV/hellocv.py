# hellocv.py
# hellocv
# opencv 패키지 설치 : opencv-python
# opencv 모듈명 : cv2

import cv2
import sys

# print(cv2.__version__)   # 4.10.0

# 시스템 기본 카메라로 부터 cv2.VideoCapture 객체 생성함
cap = cv2.VideoCapture(0) # 매개변수 : 컴퓨터에서의 기본 카메라는 0번째이다. # 카메라 열기함

if not cap.isOpened():      # 카메라 열기가 실패했다면
    print('Camera not opened')  # 카메라가 없거나, 카메라 드라이버 미설정, 다른 어플리케이션이 사용중일 때
    sys.exit()   # 프로그램 종료

# 카메라 프레임 해상도 출력
print('Frame width : ', round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))       # 가로 픽셀수
print('Frame height : ', round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))     # 세로 픽셀수

# 매 프레임 처리 및 화면 출력

while True:
    ret, frame = cap.read()
    # frame : 카메라로 부터 읽은 프레임 정보 저장
    # ret(return) : 읽기 성공 여부 저장 (성공시 True, 실패시 False)
    if ret == False:    # if not ret: 와 같음
        break           # 반복 종료

    #edge = cv2.Canny(frame, 50,150)         # 경계선 검출 함수 : 이미지의 경계선만 리턴함
    # cv2.Canny(프레임, threshold1, threshold2)
    # threshold1 : minVal 임계값 ( 값이 크면 엣지 검출이 어렵고, 적을수록 엣지 검사가 쉽다. )
    #               ( 값이 작으면 경계선들이 이어짐, 크면 경계선이 끊어짐)
    # threshold2 : maxVal 임계값 ( 경계선인지 아닌지를 판단하는 임계값, 작을수록 엣지가 많아짐)
    edge = cv2.Canny(frame, 50 , 70)


    cv2.imshow('edge', edge)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == 27:   # 27번 -> esc 키 임 -> 누르면
        break
# while end -------------------------------------------------------------------------

# 카메라 사용 해제
cap.release()  # 카메라 점유 해제(리소스 해재)
cv2.destroyAllWindows()  # 프로그램 종료시 모든창 닫기





