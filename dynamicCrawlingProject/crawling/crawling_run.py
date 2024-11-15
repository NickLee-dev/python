# path : crawling\\crawling_run.py
# module : crawling.crawling_run
# 동적 웹 크롤링 구동하는 파이썬 스크립트

# 동적 웹 크롤링 : selenium 모듈 사용함 => 외부 모듈이므로 설치해야 함
# selenium 설치되면서 추가설치 되는 모듈 있음
'''
selenium 모듈은 웹 브라우저를 실행시키고, 실행시킨 브라우저와 연동해서
입력한 웹사이트에 접속하게 하고
접속한 웹사이트에서 검색 필드와 검색 키워드를 파이썬에서 전송해서
입력 실행되게 함 : 원격 검색 작동
검색 결과 페이지에서 필요한 데이터에 대한 html 정보를 읽어와서
데이터 추출하고 분석에 사용함
동작 순서 :
브라우저 구동 => 사이트 접속 => 검색 필드 태그 찾음 => 검색할 키워드를 검색 필드에 입력
=> enter키나 버튼 클릭 event 실행 => 검색 실행 => 잠시 대기 => 브라우저에 검색 결과가 출력
=> 해당 페이지에서 필요한 데이터가 기록된 html 태그 정보를 읽어옴
=> 태그에서 데이터 추출함 => 분석 => 파일 또는 데이터베이스에 저장 처리
=> 분석 결과 시각화 처리
'''

# import 방법
# import 모듈명 [as 줄임말] => 모듈이 가진 전체 내용이 임포트 됨(메모리에 로딩됨)
# import 한다는건 모듈을 받아와 메모리에 올려서 쓴다는 의미( 용량을 차지함)
# 모듈이 가진 일부 항목만 선택해서 임포트 할 수도 있음
# from 모듈명 import 선택항목(하위 모듈명 or 함수 or 클래스) [as 줄임말]

from selenium import webdriver as wd  # 하위 모듈
from selenium.webdriver.chrome.service import Service   # 클래스
from bs4 import BeautifulSoup as bs # 클래스
from selenium.webdriver.common.by import By     # 클래스
# 명시적 대기를 위해 (waiting 을 명시함)
from selenium.webdriver.support.ui import WebDriverWait   # 클래스
from selenium. webdriver.support import expected_conditions as EC  # 하위 모듈
import time

from unicodedata import category

# db 저장 처리용 모듈
from model.tour import TourInfo
from model.tour_model import TourModel

# selenium 과 연결할 브라우저 선택 : 크롬(Chrome)
# 현재 설치해서 사용중인 크롬 브라우저 버전 확인함
#  >> 브라우저 우측 상단 점3개 > 도움말 > Chrome 정보 > 버전정보 확인 : 130.0.6723.117(최신 버전으로)
# 웹에서 '크롬 드라이버' 검색 > 확인된 버전과 같은 드라이버 .zip 파일 다운
# 압축 풀어서 폴더 안의 exe 파일을 현재 프로젝트 폴더로 복사함


def run():
    # 크롬 드라이버 등록
    # Mac 용 :
    # driver = wd.Chrome('./chromedriver')
    # window 용 : (./ : 현재 폴더, ../ : 상위 폴더)
    driver = wd.Chrome(service=Service('./chromedriver.exe')) # 크롬 브라우저 실행

    # 접속할 테스트 사이트 url 연결 확인
    main_url = 'https://www.naver.com'
    # 키보드로 입력받아서 연결처리한다면
    # main_url = input('연결할 사이트 url 입력 : ')

    # 열린 브라우저로 사이트 접속
    driver.get(main_url)    # 실행
    # time.sleep(3)           # 3초 멈춤

    # 해당 페이지의 검색 태그에 전달할 검색 키워드 정하기 : 입력을 통해서 지정해도 됨
    keyword = '로마여행'
    # keyword = input('검색할 키워드 : ')

    # 검색 결과 저장할 리스트 준비
    tour_list = []

    # 접속한 페이지의 검색 입력 필드 찾아서 검색 키워드 전송해서 자동 입력해서 실행되게 처리함
    # 검색 필드 태그(element)는 브라우저 '개발자 도구' > 'Elements' 탭에서 찾음
    # 찾은 앨리먼트 태그에서 마우스 우클릭 > copy > copy selector 선택함
    # input 태그 id 명 : #query 확인
    input_tag = driver.find_element(By.ID,'query')
    print(input_tag)
    input_tag.send_keys(keyword) # 해당 웹페이지 검색 input 에 '로마 여행' 자동 입력됨

    # time.sleep(2)

    # 검색 버튼 클릭 자동
    # button 태그 선택자 복사해 옴 : #sform > fieldset > button

    driver.find_element(By.CSS_SELECTOR, '#sform > fieldset > button').click()
    time.sleep(2)

    # 잠시 대기 => 검색 결과 페이지가 브라우저에 출력되고 나서 바로 데이터를 획득하는 행위는
    # 명시적으로 (코드상으로 표기) 대기 시켜야함
    # 획들할 데이터가 발견될 때까지 대기시킴
    # 대기방법 : 명시적 대기와 암묵적 대기 2가지 있음

    # 명시적 대기 : 요구한 앨리먼트를 찾을 때까지 대기시킴
    # 로마 가볼만한 곳 글자 출력될 때까지 기다리게 설정
    # selector: #nxTsOv > div > div.MainContainer._travel_header.MainContainer-vjtko > div.content-qIit7 > div > div > div > div.panel > div.pois-Xuo3A > ul > li:nth-child(1) > div > div > div > a > div > div > span
    try:
        element = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#nxTsOv > div > div.MainContainer._travel_header.MainContainer-vjtko > div.content-qIit7 > div.SummaryTopPoiContainer-qpzcR > div > div.head-xMGxp > div > h3')))
        # 지정한 앨리먼트 위치를 확인하면 대기 종료됨
    except Exception as e:
        print('대기 요청 타임아웃 : ', e)

    # 암묵적 대기 :
    # DOM ( Document object Model : 태그 사용 계층 구조 ) 이 전부 다 브라우저에 로드 될 때까지 (모두 읽어들일때까지)
    # 대기하게 하고, 로드된 후에 바로 태그 앨리먼트를 찾도록 진행함
    # 앨리먼트 찾을 시간(초)을 지정하면, 지정 시간동안 DOM 풀링을 지시할 수 있음
    driver.implicitly_wait(10)

    # 절대적 대기 :
    # time.sleep(10) # 10초 대기

    # 로마 가볼만한 곳 : -> 클릭 > 새 페이지에서 정보 표시 확인
    # selector : #nxTsOv > div > div.MainContainer._travel_header.MainContainer-vjtko > div.content-qIit7 > div.SummaryTopPoiContainer-qpzcR > div > div.head-xMGxp > div > a
    # driver.find_element(By.CSS_SELECTOR, '#nxTsOv > div > div.MainContainer._travel_header.MainContainer-vjtko > div.content-qIit7 > div.SummaryTopPoiContainer-qpzcR > div > div.head-xMGxp > div > a').click()
    # time.sleep(2)

    # 해당 페이지 영역에서 데이터를 가져올 때, 혹시 로그인이 필요한 경우에는 로그인 세션 관리 필요함
    # 데이터가 많으면 로그인 세션 타임아웃에 의해 자동 로그아웃될 수 있으므로,
    # 특정 단위별로 읽어들인 다음 로그아웃하고, 다시 로그인하는 처리가 필요함
    # loop 문을 돌려서 일괄적으로 접근 처리 필요함 : 메타 정보 획득

    # 가볼만한 곳 항목들 추출
    # li 태그들의 클래스 명 : TopPoiItem-MgXeO
    item_list = driver.find_elements(By.CLASS_NAME, 'TopPoiItem-MgXeO')
    print(len(item_list))
    print(item_list)

    # 가볼만한 곳 항목에서 데이터 추출하기
    # 추출할 값 : 순위(rank), 장소이름(name), 장소설명(description), 장소구분(category)
    tm = TourModel()  # db 저장 처리를 위한 객체 생성
    # 기존 테이블에 저장된 정보 모두 지우기
    tm.delete_tour()

    # item_list 에서 하나씩 인덱싱해서 db에 기록 저장 처리
    for item in item_list:
        # #nxTsOv > div > div.MainContainer._travel_header.MainContainer-vjtko > div.content-qIit7 > div.SummaryTopPoiContainer-qpzcR > div > div.SummaryTopPoiList-Vpaz0 > div > div > div.information-Mr2HB._scroller > ul > li.item-aDXTr.as_first-iEfrg > div > div > div > a > figure > span
        rank = item.find_element(By.CSS_SELECTOR, 'a > figure > span').text
        # #nxTsOv > div > div.MainContainer._travel_header.MainContainer-vjtko > div.content-qIit7 > div.SummaryTopPoiContainer-qpzcR > div > div.SummaryTopPoiList-Vpaz0 > div > div > div.information-Mr2HB._scroller > ul > li.item-aDXTr.as_first-iEfrg > div > div > div > a > div > span.subject-G1Fz6 > b
        name = item.find_element(By.CSS_SELECTOR, 'b.name-icVvV').text
        # #nxTsOv > div > div.MainContainer._travel_header.MainContainer-vjtko > div.content-qIit7 > div.SummaryTopPoiContainer-qpzcR > div > div.SummaryTopPoiList-Vpaz0 > div > div > div.information-Mr2HB._scroller > ul > li.item-aDXTr.as_first-iEfrg > div > div > div > a > div > span.desc-tw973
        description = item.find_element(By.CSS_SELECTOR, 'span.desc-tw973').text
        # #nxTsOv > div > div.MainContainer._travel_header.MainContainer-vjtko > div.content-qIit7 > div.SummaryTopPoiContainer-qpzcR > div > div.SummaryTopPoiList-Vpaz0 > div > div > div.information-Mr2HB._scroller > ul > li.item-aDXTr.as_first-iEfrg > div > div > div > a > div > div > span
        category = item.find_element(By.CSS_SELECTOR, 'span.text-Y6pAX').text
        print(rank, name, description, category)

        # 튜플로 저장 처리
        tp_info = (rank, name, description, category)
        # db 에 저장 : insert_tour
        tm.insert_tour(tp_info)
    # for loop-----------------------------------------------------------------------

    # db에 저장된 정보 조회 출력 확인
    resultset = tm.select_all_tour()
    # 리턴된 정보들을 한행씩 TourInfo 객체에 저장 처리하고 리스트에 추가
    tour_list = []
    for row in resultset:
        tourinfo = TourInfo(row[0],row[1],row[2],row[3])
        tour_list.append(tourinfo)
    print(tour_list)

    # 브라우저 종료
    driver.close() # 크롬 브라우저 닫기
    driver.quit() # 드라이버 종료

    return # main으로 리턴 : 프로세스 종료

# run()------------------------------------------------------------------------------------------