# path : testdb/test_mysql.py
# module : testdb.test_mysql

# 파이썬 외부 모듈(패키지) 설치와 사용
# 파이썬 외부 모듈은
# 1. 프로젝트에 직접 설치해서 사용하는 방법(venv)
# 2. Anaconda 에 별도로 콘다 가상환경을 만들고, 필요한 패키지를 설치한 다음에 프로젝트에 콘다가상환경을 연결 사용
#    외부모듈은 버전을 타기때문에 사용할 모듈에 맞춰 conda 가상환경을 이용해 패키지별로 세팅 해둘수 있음

# 프로젝트에 직접 설치하는 방법
# 첫번째 :
# 파이참 툴 왼쪽 아래의 'Python Packages' 탭을 클릭 > 뷰가 아래쪽에 보여짐
# 뷰의 왼쪽에 검색영역에 설치할 패키지 명을 입력
# 검색에 나온 리스트는 pypi 웹 사이트에 등록된 module을 보여줌
# 검색되면 패키지 명을 왼쪽에서 클릭하면 오른쪽에 패키지 정보가 표시됨
# 오른쪽 패키지 정보 위에 'Install Packages' 버튼 클릭함
# 설치가 완료되면 버전 숫자 표시됨(latest 선택시 최신버전 선택)
# 만약, 설치가 실시하면 오류 메세지에서 에러 이유를 찾아내서 해결해야 됨

# 두번째 :
# 모든 파이썬 개발툴에서 공통으로 사용하는 방법임
# 'Terminal'(터미널) 탭 (파이참에선 왼쪽 아래 위치) 클릭
# 프롬프트 표시됨 : (가상환경종류/.venv) 터미널종류(ps : power shell) 현제 프로젝트 경로>
# 프롬프트에 설치 명령어를 직접 입력해서 패키지 설치함
# ......> pip install 설치할 패키지명
# 주의사항 : pip 버전을 먼저 upgrade 해야 되는 경우가 있음
# ......> python -m install -- upgrade pip
# ......> pip --version
# 패키지 설치와 pip 업그레이드 동시에 수행할 수도 있음
# ......> python -m pip install --upgrade 설치할 패키지명

# 세번째 : 파이참에서 사용가능한 세팅법
# File 메뉴 > Settings... > 왼쪽 항목에 'Project: 프로젝트명' 표시찾음
# > 프로젝트명 부분을 아래로 확장시킴
# 오른쪽 아래에 'python interpreter' (파이썬 인터프리터) 선택
# => 현재 프로젝트에 설치된 패키지 모듈을 볼 수 있음
# > 위쪽의 '+' 클릭 > 새 창 열림
# 설치할 패키지 검색 > 검색한 패키지 이름 선택 > 아래쪽의 '설치' 버튼 클릭
# 설치 성공 메세지 확인하고 창 닫음

# 데이터베이스 연결에 필요한 파이썬 패키지 ------------------------------------------

# RDBMS : 관계(Relationship)을 사용하는 데이터베이스 -------------------------------
# mysql db : pymysql
# oracle db : cx-Oracle => 에러 발생시 선행 조치 내용을 확인하고 해결함
# SQLite : 파이썬 내장 라이브러리임 (설치 필요 없음), 파일 기반의 경량 데이터베이스임
# PostgreSQL : psycopg2 | pg8000
# MS SQL Server : pyodbc | pymssql

# noSQL 기반 : 관계 (Relationship) 이 없는 데이터베이스 ----------------------------
# Redis : redis-py
# mongoDB : pymongo  # 대용량 처리를 위한 nosql
# casandra : casandra-driver
# mariaDB : mariadb


# 1. 연결할 db에 대한 패키지를 설치한 다음에 import 선언하고 사용함
import pymysql

# 2. 해당 데이터베이스에 연결하기 위한 코드 작성
# db 서버의 ip주소(URL), 포트번호, 사용자 계정, 암호

dbURL = 'localhost' #dbURL = '192.168.120.34'
dbPORT  = 3306
dbUSER = 'root'
dbPASS = '1234'

# 3. 데이터베이스 연결
# 임포트한 모듈에서 제공하는 메소드 사용함 : pymysql.connect()
conn = pymysql.connect( host=dbURL,port=dbPORT,user=dbUSER,passwd=dbPASS\
                        ,db='testdb',charset='utf8',use_unicode=True)
# 연결이 실패하면, conn = null(None) 임
# 연결이 성공하면에 대해 조건식으로 표현하면, if conn != null:

# 4. DB 연결 성공했다면, 필요한 쿼리문(CRUD C:insert, R:select, U:update, D:delete) 작성
# 예 : select 쿼리문 작성해서 실행 처리


query = 'select * from employee'

cursor= conn.cursor() # 자바의 Statement| PreparedStatement
cursor.execute(query) # 연결된 db로 쿼리문 보내서 실행
result = cursor.fetchall() # 조회된 모든 결과를 받음, 반환 자료형은 tuple
# 이후 결과 매핑 처리 : 반복문으로 각 행의 컬럼값들을 vo(dto) 클래스 객체의 필드(property)에 저장 처리

# 5. 쿼리문이 dml 이면 트랜젝션 처리가 필수임
if result>0:
    conn.commit()
else:
    conn.rollback()

# 6.db 사용이 끝나면 반드시 닫음
conn.close()
