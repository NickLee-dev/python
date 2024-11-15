# path : sign.py
# module : sign
# 간판 사진에서 상호와 전화번호 추출 테스트 스크립트

import numpy as np # 행렬처리용   pip install numpy
import cv2  # opencv 모듈명임  pip install opencv-python
import sys  # 시스템에 있는 정보 추출용
import pytesseract  # 사진판독용  pip install pytesseract
import common.dbConnectTemplate as dbtemp # pip install cx_Oracle



def reorderPts(pts):
    idx = np.lexsort((pts[:, 1], pts[:, 0]))  # 컬럼 0 -> 컬럼 1 순으로 정렬한 인덱스를 반환
    pts = pts[idx]  # x좌표로 정렬

    if pts[0, 1] > pts[1, 1]:
        pts[[0, 1]] = pts[[1, 0]]

    if pts[2, 1] < pts[3, 1]:
        pts[[2, 3]] = pts[[3, 2]]

    return pts

def camerain():
    filenames = ['./images/sample01.jpg', './images/sample02.jpg', './images/sample03.jpg']

    data_list = []

    for filename in filenames:
        print(f'파일이름 : {filename}')
        src = cv2.imread(filename)
        if src is None:
            print('image load failed')
            sys.exit()

        # 출력 영상 설정
        dh, dw = src.shape[:2]
        srcQuad = np.array([[0, 0], [0, 0], [0, 0], [0, 0]], np.float32)
        dstQuad = np.array([[0, 0], [0, dh], [dw, dh], [dw, 0]], np.float32)
        dst = np.zeros((dh, dw), np.uint8)

        # 입력 영상 전처리
        src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        th, src_bin = cv2.threshold(src_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        # 외곽선 검출 및 명함 검출
        contours, _ = cv2.findContours(src_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        for pts in contours:
            # 너무 작은 객체는 제외
            if cv2.contourArea(pts) < 10:
                continue

            # 외곽선 근사화 : 0.02의 오차범위 지정
            approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True) * 0.02, True)
            # print('approx : ', len(approx))

            # 컨벡스(닫혀진 다각형)가 아니고, 사각형이 아니면 제외
            if not cv2.isContourConvex(approx) or len(approx) != 4:
                continue

            # 골라낸 컨벡스에 테두리 그리기(다각형 도형 그리기)
            cv2.polylines(src, [approx], True, (0, 255, 0), 2, cv2.LINE_AA)
            srcQuad = reorderPts(approx.reshape(4, 2).astype(np.float32))

            # 명함 이미지 사각형 이미지 만들기
            pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
            dst = cv2.warpPerspective(src, pers, (dw, dh), flags=cv2.INTER_CUBIC)

            dst_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
            result = pytesseract.image_to_string(dst_rgb, lang='Hangul+eng')
            print(result)

        cv2.waitKey()
        cv2.destroyAllWindows()

        list = [item for item in result.split('\n') if item != ""]
        data = {}
        for i in range(len(list)):
            if i == len(list) - 1:
                data['phone'] = list[i]
            elif 'name' not in data:
                data['name'] = list[i]
            else:
                data['name'] = data['name'] + list[i]
        print(f'data : {data}')
        data_list.append(data)

    print(f'data_list : {data_list}')
    outputDB(data_list)

def outputDB(data_list):
    # 결과 DB에 저장

    # vision 테이블 비우기
    delete_query = 'delete from vision'
    conn = dbtemp.connect()
    cursor = conn.cursor()

    try:
        cursor.execute(delete_query)
        dbtemp.commit(conn)
        print(f'vision 테이블 데이터 삭제 성공')
    except:
        dbtemp.rollback(conn)
        print(f'vision 테이블 데이터 삭제 실패')
    finally:
        cursor.close()
        dbtemp.close(conn)

    # DB 삽입 쿼리
    insert_query = 'insert into vision values (:1, :2)'
    for data in data_list:
        conn = dbtemp.connect()
        cursor = conn.cursor()

        tp_data = (data.get('name'), data.get('phone'))
        print(f'{ data.get("name") } 데이터 삽입 중')

        try:
            cursor.execute(insert_query, tp_data)
            dbtemp.commit(conn)
            print(f'{ data.get("name") } 데이터 삽입 성공')
        except:
            dbtemp.rollback(conn)
            print(f'{data.get("name")} 데이터 삽입 실패')
        finally:
            cursor.close()
            dbtemp.close(conn)

if __name__ == '__main__':
    dbtemp.oracle_init()  # 딱 한번만 실행
    camerain()

# python exe 만들기
# > pip install pyinstaller
# > pyinstaller sign.py => 실행파일 하나만 생성하려면 pyinstaller -w -F sign.py
# 프로젝트 안의 dist 폴더 생겨있음 > dist 폴더 안에 exe 파일 확인함