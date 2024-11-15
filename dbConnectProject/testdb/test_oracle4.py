# path : testdb\\test_oracle4.py
# module : testdb.test_oracle4
# 오라클 연동과 update 쿼리문 실행 테스트

# 1. 필요한 모듈 import
import cx_Oracle
import os
import common.dbConnectTemplate as dbtemp

# 2. db드라이브 등록 및 연결
dbtemp.oracle_init()
conn = dbtemp.connect()

# 3. delete 처리
# query = "delete from member where userid='user07'"

# delete 쿼리문에 사용할 값이 키보드로 입력받거나, 외부 입력 데이터로 읽어와서 적용하는 경우
# 주의 : 쿼리문에 적용할 외부 값은 반드시 튜플로 저장해야 함
# 키보드로 값을 입력 받아서 튜플에 저장처리 :
userid = input('사용자 아이디 : ')

tp_value = (userid, )

# 튜플을 쿼리문에 적용할 때, 순서번호를 사용함 (순서대로 적용해야 함)
query = "delete from member where userid=:1"

# 4.
cursor = conn.cursor()

try:
    # cursor.execute(query)
    cursor.execute(query,tp_value)
    dbtemp.commit(conn)
except:
    dbtemp.rollback(conn)
finally:
    cursor.close()
    dbtemp.close(conn)