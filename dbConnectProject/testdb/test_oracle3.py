# path : testdb\\test_oracle3.py
# module : testdb.test_oracle3
# 오라클 연동과 update 쿼리문 실행 테스트

# 1. 필요한 모듈 import
import cx_Oracle
import os
import common.dbConnectTemplate as dbtemp

# 2. db드라이브 등록 및 연결
dbtemp.oracle_init()
conn = dbtemp.connect()

# 3. update 처리
# query = "update member set userpwd='pass04',username='파이참',phone='010-1234-4444',email='test2@test.org'\
# where userid='user04'"

# update 쿼리문에 사용할 값이 키보드로 입력받거나, 외부 입력 데이터로 읽어와서 적용하는 경우
# 주의 : 쿼리문에 적용할 외부 값은 반드시 튜플로 저장해야 함
# 키보드로 값을 입력 받아서 튜플에 저장처리 :
userid = input('사용자 아이디 : ')
userpwd = input('암호 : ')
phone = input('핸드폰번호(- 포함) : ')
email = input('이메일 : ')

tp_value = (userpwd, phone, email, userid)

# 튜플을 쿼리문에 적용할 때, 순서번호를 사용함 (순서대로 적용해야 함)
query = "update member set userpwd=:1, phone=:2, email=:3 where userid=:4"

# 4.
cursor = conn.cursor()

try:
    # cursor.execute(query)
    cursor.execute(query,tp_value)
    dbtemp.commit(conn)
except Exception as e:
    dbtemp.rollback(conn)
finally:
    cursor.close()
    dbtemp.close(conn)