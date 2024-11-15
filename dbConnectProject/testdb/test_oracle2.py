# path : testdb\\test_oracle2.py
# module : testdb.test_oracle2
# 오라클 연동과 insert 쿼리문 실행 테스트

# 1. 필요한 모듈 import
import cx_Oracle
import os
import common.dbConnectTemplate as dbtemp

# 2. db드라이브 등록 및 연결
dbtemp.oracle_init()
conn = dbtemp.connect()

# 3. insert 처리
# query = "insert into member values ('user07','pass04','파이선','M',33,'010-1234-5678','test@test.org'\
# ,default,default,default,default,default,null)"

# insert 쿼리문에 사용할 값이 키보드로 입력받거나, 외부 입력 데이터로 읽어와서 적용하는 경우
# 주의 : 쿼리문에 적용할 외부 값은 반드시 튜플로 저장해야 함
# 키보드로 값을 입력 받아서 튜플에 저장처리 :
userid = input('사용자 아이디 : ')
userpwd = input('암호 : ')
username = input('이름 : ')
gender = input('성별(남:M/여:F) : ').upper()
age = int(input('나이 : '))
phone = input('핸드폰번호(- 포함) : ')
email = input('이메일 : ')

tp_value = (userid, userpwd, username, gender, age, phone, email)

# 튜플을 쿼리문에 적용할 때, 순서번호를 사용함 (순서대로 적용해야 함)
query = "insert into member values (:1,:2,:3,:4,:5,:6,:7,default,default,default,default,default,null)"

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