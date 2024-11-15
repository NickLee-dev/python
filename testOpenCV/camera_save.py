# camera_save.py
# camera_save
# 카메라로 들어오는 영상 프레임을 저장 처리

import cv2
import sys

# 시스템 기본 카메라로 부터 cv2.VideoCapture 객체 생성함
cap = cv2.VideoCapture(0) # 매개변수 : 컴퓨터에서의 기본 카메라는 0번째이다. # 카메라 열기함

if not cap.isOpened():      # 카메라 열기가 실패했다면
    print('Camera not opened')  # 카메라가 없거나, 카메라 드라이버 미설정, 다른 어플리케이션이 사용중일 때
    sys.exit()   # 프로그램 종료

# 카메라 프레임 해상도 출력
print('Frame width : ', round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))       # 가로 픽셀수
print('Frame height : ', round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))     # 세로 픽셀수
# 초당 프레임수 (fps : frame per second)
print('FPS : ', round(cap.get(cv2.CAP_PROP_FPS)))                       # 초당 Frame수

# 동영상 저장을 위한 cv2.VideoWriter 객체 생성
fw = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))           # 가로 크기
fh = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))          # 세로 크기
fps = round(cap.get(cv2.CAP_PROP_FPS))                  # 프레임수
fourcc = cv2.VideoWriter_fourcc(*'DIVX') # *'DIVX' == 'D','I','V','X'

out = cv2.VideoWriter('./multi/result.avi', fourcc, fps, (fw, fh))
out2 = cv2.VideoWriter('./multi/result2.avi', fourcc, fps, (fw, fh))

# 매 프레임 처리 및 화면 출력, 동영상 저장 처리
while True:
    ret, frame = cap.read()
    # frame : 카메라로 부터 읽은 프레임 정보 저장
    # ret(return) : 읽기 성공 여부 저장 (성공시 True, 실패시 False)
    if ret == False:    # if not ret: 와 같음
        break           # 반복 종료

    edge = cv2.Canny(frame, 50 , 150)
    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)
    out.write(edge) # 파일로 저장
    out2.write(frame)

    cv2.imshow('edge', edge)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == 27:   # 27번 -> esc 키 임 -> 누르면
        break
# while end -------------------------------------------------------------------------

# 카메라 사용 해제
cap.release()  # 카메라 점유 해제(리소스 해재)
out.release()  #
cv2.destroyAllWindows()  # 프로그램 종료시 모든창 닫기