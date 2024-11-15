# path : testdb\\test_oracle.py
# module : testdb.test_oracle
# 파이썬과 오라클 연동 테스트 스크립트

# cx-Oracle 오류
# https://visualstudio.microsoft.com/visual-cpp-build-tools/
# MicroSoft C++ build Tools 다운로드
# 설치 : 주의사항 : 설치시 워크로드 C++를 사용한 데스크톱 개발 체크

# https://www.oracle.com/database/technologies/instant-client/winx64-64-downloads.html
# Oracle Instant Client Downloads for Microsoft Windows (x64) 64-bit 다운받기


# 패키지 설치 : cx-Oracle
# 설치 실패시 에러메세지 확인해 봄 : Microsoft C++ builder Tool 관련 메세지이면
# https://visualstudio.microsoft.com/visual-cpp-build-tools/ 접속함
# Microsoft C++ Build Tools 다운 , exe 다운확인 > 설치함
# 주의 : 설치시 왼쪽 위 항목 'C++를 사용한 데스크톱 개발' 반드시 체크함 > 설치 버튼 클릭
# 만약 체크를 놓쳤다면 설치 후 '수정'으로 추가해도 됨

# 패키지 설치 후에 추가 설치 :
# 파이썬에서 오라클 서버에 접속하기 위한 Oracle사가 제공하는 드라이버 파일을 다운받음
# https://www.oracle.com/database/technologies/instant-client/winx64-64-downloads.html
# 오라클 서버 버전에서 windows 64bit 용으로 zip 다운받음 > 압출풀기
# 해당 폴더 경로를 짧게 하기 위해 복사함
# D:\\instantclient_18_5

# 1. 사용할 패키지 임포트함
import cx_Oracle
import os

from pandas.core.computation.common import result_type_many

# 2. 오라클 드라이브(instantclient) 등록
# 자바의 ojdbc.jar 같은 드라이브의 역할
location = 'D:\\instantclient_18_5'

# 드라이브 등록 방법 1 : 환경변수 path에 등록 (파이썬 코드로 path 에 등록시킴)
os.environ['PATH'] = location + ';' + os.environ['PATH'] # environ 환경변수 입력용 메소드 / 원래 경로에 드라이브 경로 추가

# 드라이브 등록 방법 2 : 코드 구문으로 오라클 초기 설정 지정
# 주의 : 애플리케이션 전체 실행시 딱 한번 구동되게 해야함
cx_Oracle.init_oracle_client(lib_dir=location)

# 3. 오라클과 연결하기 위한 값 준비하고 연결 설정
url = 'localhost:1521/xe'  # localhost 는 ip 주소로 대체 가능
user = 'c##testweb'
passwd = 'testweb'

# conn 이라는 변수에 설정값 입력
conn = cx_Oracle.connect(user, passwd, url)
# conn = cx_Oracle.connect('c##testweb', 'testweb', 'localhost:1521/xe')    <- 바로 스트링 입력가능
# conn = cx_Oracle.connect('c##testweb/testweb@localhost:1521/xe')          <- 하나의 스트링으로도 입력가능
print('conn : ', conn)    # 연결 확인  # conn :  <cx_Oracle.Connection to c##testweb@localhost:1521/xe>

# 4. 쿼리문 준비하기
query = 'select * from c##testweb.member'   # c##testweb안에잇는 member 테이블 출력

# 5. 쿼리문 실행을 위한 문장 객체 준비하고, 쿼리문 실행처리 (cursor)
# cursor : 준비된 쿼리문을 연결된 db로 전송하고 실행시키는 객체임
cursor = conn.cursor()      # db 연결 정보로 커서 객체를 생성함
cursor.execute(query)       # 쿼리문을 db로 전송하고 실행한 결과를 커서가 받음
# 커서가 실행된 결과를 가지고 있음

# select 쿼리문 실행의 결과인 resultSet 을 커서가 받음
# dml 문(insert, update, delete)은 처리된 행갯수를 커서가 받음
print('cursor : ', cursor)      # cursor :  <cx_Oracle.Cursor on <cx_Oracle.Connection to c##testweb@localhost:1521/xe>>

# 6. 커서가 받은 결과 처리
# select 결과는 결과 매핑 처리 필요하고, dml 문은 트랜잭션(commit, rollback) 처리 필요함
# resultSet = cursor.fetchall()   # 커서가 가르키는 결과 행들을 모두 변수에 옮김
# 커서 객체를 fetchall() 하고 나면 cursor는 비워짐
# print('resultSet : ', resultSet)
# print(type(resultSet))   # list # list [(tuple),(tuple),...]
# print(type(resultSet[0]))   # tuple
# print(len(resultSet))    # 회원이 있는 만큼 출력
# resultSet :  [('user02', '$2a$10$CM9GN73sq5m2ogX4kZlH0uAsbZ4xJYMoB6EyWvXGQfvWoy879/jkm', '이상무', 'M', 25, '010-4567-4899', 'tkdan@naver.com', datetime.datetime(2024, 10, 30, 0, 0), datetime.datetime(2024, 10, 30, 0, 0), 'direct', 'N', 'Y', None), ('user03', '$2a$10$re8Lx8J5zqbmpA5FBTs7Tu7H9sAb.qle9O21rTAZOiqckcu1tiNmi', '이상무', 'M', 20, '010-4567-4567', 'dltkdan7373@hanmail.net', datetime.datetime(2024, 10, 30, 0, 0), datetime.datetime(2024, 10, 30, 0, 0), 'direct', 'N', 'Y', None), ('user04', '$2a$10$zUvATdKd3L3el7BXMwajf.pRL/aUX93IH/k2sLI1PZ.Sea1XfLVsG', '이상무', 'M', 20, '010-4000-0000', 'test@test.org', datetime.datetime(2024, 10, 22, 0, 0), datetime.datetime(2024, 10, 22, 0, 0), 'direct', 'N', 'Y', None), ('admin', '$2a$10$6s09iY1ndPjF0DN8YmK4QeCGn4kWj.4FmFpsO7MjWyQw7QGKgiy2a', '무무', 'M', 24, '010-4444-4444', 'test@test.or', datetime.datetime(2024, 10, 22, 0, 0), datetime.datetime(2024, 11, 5, 0, 0), 'direct', 'Y', 'Y', 'admin_스크린샷 2024-10-28 212605.png'), ('user01', '$2a$10$FxhpFoE3lOsM5gRye/QpUOB5IcbA0.5lgIAgU0fzA9OQdelz0vsMC', '쌈무', 'M', 24, '010-4444-4444', 'test@test.org', datetime.datetime(2024, 10, 22, 0, 0), datetime.datetime(2024, 11, 1, 0, 0), 'direct', 'N', 'Y', 'user01_스크린샷 2024-10-31 150545.png')]
# 전체는 리스트로 묶이고 각 행들은 튜플로 출력

# 커서가 가진 select 쿼리 결과를 한 행씩 처리한다면
for row in cursor:
    print('행이 가진 컬럼 갯수 : ',len(row),type(row))
    # 컬럼별로 데이터 하나씩 추출
    USERID=row[0]
    USERPWD=row[1]
    USERNAME=row[2]
    GENDER=row[3]
    AGE=row[4]
    PHONE=row[5]
    EMAIL=row[6]
    ENROLL_DATE=row[7]
    LASTMODIFIED=row[8]
    SIGNTYPE=row[9]
    ADMIN_YN=row[10]
    LOGIN_OK=row[11]
    PHOTO_FILENAME=row[12]

    # print(USERID,USERPWD,USERNAME)
    # index 를 이용한 출력 처리
    for idx in range(len(row)): # range(13) : 0 ~ 12
        print(row[idx],end=", ") # , 로 구분지음
    print() # 줄바꿈 처리

# 작업이 끝나면 반드시 닫음
cursor.close()
conn.close()




