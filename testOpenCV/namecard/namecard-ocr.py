# path : namecard\\namecard_ocr.py
# module : namecard.namecard_ocr

# 명함 사진에서 글자 추출하기
"""
Tesseract-ocr 설치하기

1. tesseract-ocr-w64-setup-v5.0.1-alpha.20220118.exe 파일 다운로드
   (https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.1-alpha.20220118.exe)
2. 설치 시 "Additional script data" 항목에서 "Hangul Script", "Hangul vertical script" 항목 체크,
   "Additional language data" 항목에서 "Korean" 항목 체크.
3. 설치 후 시스템 환경변수 PATH에 Tesseract 설치 폴더 추가
   (e.g.) c:\Program Files\Tesseract-OCR
4. 설치 후 시스템 환경변수에 TESSDATA_PREFIX를 추가하고,
   변수 값을 <Tesseract-DIR>\tessdata 로 설정
5. <Tesseract-DIR>\tessdata\script\ 폴더에 있는
  Hangul.traineddata, Hangul_vert.traineddata 파일을
   <Tesseract-DIR>\tessdata\ 폴더로 복사
6. 명령 프롬프트 창에서 pip install pytesseract 명령 입력
"""

import sys
import numpy as np      # numpy
import cv2              # opencv-python
import pytesseract      # pytesseract

# 함수 만들기 ----------------------------------------------------------------------------
def reorderPts(pts):
    idx = np.lexsort((pts[:, 0], pts[:, 1]))        # 컬럼0  -->  컬럼1 순으로 정렬한 인덱스가 반환
    pts = pts[idx]  # x 좌료로 정렬

    if pts[0, 1] > pts[1, 1]:
        pts[[0, 1]] = pts[[1, 0]]

    if pts[2, 1] < pts[3, 1]:
        pts[[2, 3]] = pts[[3, 2]]

    return pts
# ---------------------------------------------------------------------------------------

# 명함 이미지 들어있는 사진 파일 불러오기
filename = '../images/namecard1.jpg'

# namecard_ocr.py 파일을 실행파일로 만들어서 실행
# 명령프롬프트에서 > 실행파일명 전달값 전달값 전달값 ......  형태로 실행파일로 값을 전달한다면
# 즉, 실행파일 (namecard_ocr.exe) 실행할 때 명함사진 파일명을 전달한다면
# >> namecard_ocr namecard1.jpg
# 소스 코드로 이런 식으로 전달 들어오는 값도 받아서 처리하도록 구현하면 됨
if len(sys.argv) > 1 : # 가변 매개변수 들어오는 값이 있는지 확인
    filename = sys.argv[1]  # 받아온 매개변수 를 파일이름으로 저장

# 파일 읽어오기
src = cv2.imread(filename)

# 읽어올 파일이 없다면 시스템종료처리
if src is None:
    print('image not found')
    sys.exit()

# 출력 영상 설정
dw, dh = 720, 400
# 사진 이미지 4개의 꼭지점 좌표값 저장용 행렬 만들기
srcQuad = np.array([[0,0],[0,0],[0,0],[0,0]],np.float32)  # 왼쪽위에서부터 시계방향으로 4모서리 좌표값 행렬 생성
# 출력 영상 크기 저장용 행렬 만들기
dstQuad = np.array([[0,0],[dw,0],[dw,dh],[0,dh]],np.float32)

# 입력 영상 전처리
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 흑백이미지를 흰색 검정색으로 바꿈
th, src_bin = cv2.threshold(src_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) # 임계값에 대해 OTSU 알고리즘으로 결정
# print('사용된 임계값 : ', th)

# 외곽선 검출 및 명함 검출
contours, _ = cv2.findContours(src_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print(type(contours))  # tuple
print(contours)     # (array([[[],...],...]))

# 명함 사각형 좌표값 추출
for pts in contours:
    # print('pts :', pts)
    # 너무 작은 면적의 도형은 제외함
    if cv2.contourArea(pts) < 10:
        continue
    # 외곽선 근사치 처리 (근사화) : 0.02 의 오차범위 지정
    approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True)*0.02, True)
    # print('approx : ', len(approx))  # 추출한 도형의 좌표값 출력 (꼭지점 갯수)

    # 컨백스(닫혀진 일반 다각형)가 아니고, 4각형이 아니면 제외함
    if not cv2.isContourConvex(approx) or len(approx) != 4:  # 컨백스가 아니냐
        continue

    # 골라낸 컨백스에 테두리 그리기 (다각형 도형 그리기)
    cv2.polylines(src, [approx], True, (0, 255, 0), 2, cv2.LINE_AA)  # 라인그리기
                # 원사진, 좌료, 연결된 선이 닫혀잇는것들, 선의 색상, 선의 굵기, 선의종류
    # 위에 작성된 함수로 도형 좌표값 전달해서 좌표값 정리
    srcQuad = reorderPts(approx.reshape(4,2).astype(np.float32))

    # 명함 이미지 사각형 이미지 만들기
    per = cv2.getPerspectiveTransform(srcQuad,dstQuad)
    dst = cv2.warpPerspective(src, per, (dw,dh), flags=cv2.INTER_CUBIC)

    # 명함에서 글자 추출
    dst_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
    str = pytesseract.image_to_string(dst_rgb, lang='Hangul+eng')
    print(str)

# 처리된 이미지 출력 확인
# cv2.imshow('src', src)
# cv2.imshow('src_gray', src_gray)
# cv2.imshow('src_bin', src_bin)
cv2.imshow('dst', dst)

cv2.waitKey() # 창이 안 닫히고 대기시킴, 아무 키나 누르면 대기 종료됨
cv2.destroyAllWindows()   # 열린 창들 모두 닫기


