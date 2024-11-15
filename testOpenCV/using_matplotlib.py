# using_matplotlib.py
# 이미지 읽어올 때 색상 채널 바꾸기

import matplotlib.pyplot as plt
import cv2

# 컬러 이미지 읽어 들이기 ( 절대경로도 사용가능함, \\ 2개, / 1개 사용함)
imgBGR = cv2.imread('D:\\python_workspace\\testOpenCV\\images\\cat.bmp')  # BGR 순으로 읽음
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)  # COLOR_BGE2RGB => BGR을 RGB로 변경
# 영상 출력
plt.axis('off')
# plt.imshow(imgBGR)
plt.imshow(imgRGB)
plt.show()

# 그레이스케일로 이미지를 읽어 들이기
imgGray = cv2.imread('./images/cat.bmp',cv2.IMREAD_GRAYSCALE) # IMREAD_GRAYSCALE => 흑백으로 변경
# 영상 출력
plt.axis('off') # 축제목 제거
plt.imshow(imgGray, cmap='gray')  # 색상맵을 gray로 변경
plt.show()

# axes 영역에 두 개의 영상을 함께 출력
plt.subplot(121), plt.axis('off'), plt.imshow(imgRGB)  # 1행 2열로 배치할건데 1번째 자리에 들어갈꺼임
plt.subplot(122), plt.axis('off'), plt.imshow(imgGray,cmap='gray')  # 1행 2열로 배치할건데 1번째 자리에 들어갈꺼임
plt.show()