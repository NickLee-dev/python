# image_show.py
# opencv 로 이미지파일 불러오기

import cv2
import sys

# 상대경로 사용 가능함
img = cv2.imread('./images/jinny.jpg')

if img is None:
    print('image load fail')
    sys.exit()

# fx와 fy는 각각 x축과 y축의 비율을 나타냅니다.
resized_img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

print(img.shape)    # (480, 640, 3) => (height, width, channel) 행렬임
print(type(img))    # <class 'numpy.ndarray'> (이미지가 행렬로 읽혀짐)

# 이미지(영상) 화면 출력
cv2.namedWindow('imgshow')      # 실행시 나타날 윈도우 창 이름 지정
#cv2.imshow('imgshow',img)   # 창이름이 imgshow 인 창에 img 띄우기
cv2.imshow('imgshow',cv2.Canny(resized_img,100,200))   # 창이름이 imgshow 인 창에 img 띄우기

cv2.waitKey()            # 키보드 입력이 있을 때까지 기다림(매개변수가 비어잇으면 아무키나 누르면 창 닫아짐)

# 창 닫으면서 프로그램 종료 처리
cv2.destroyAllWindows()

