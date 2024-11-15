# path : model\\tour_model.py
# module : model.tour_model
# 오라클 db에 TourInfo 객체 정보를 CRUD 처리하는 클래스 정의 스크립트

import common.dbConnectTemplate as dbtemp
import cx_Oracle

class TourModel:
    # field : private
    __conn = ''

    # constructor
    def __init__(self):
        dbtemp.oracle_init()   # 드라이버 등록 : 딱 한번 실행

    # method
    # insert method ------------------------------------------------
    def insert_tour(self, tp_tour):
        query = 'insert into tour values (:1, :2, :3, :4)'
        self.__conn = dbtemp.connect()
        print(self.__conn, tp_tour)  # 확인
        try:
            # 자동 close 되게 처리 : try with resource 문 이용
            with self.__conn.cursor() as cursor:
                cursor.execute(query, tp_tour)
            dbtemp.commit(self.__conn)
        except Exception as e:
            dbtemp.rollback(self.__conn)
            print('insert_tour 실패 : ', e)
        finally:
            dbtemp.close(self.__conn)
    # insert method ------------------------------------------------

    # update method ------------------------------------------------
    def update_tour(self, tp_tour):
        query = 'update tour set name=:1, description=:2, catagory=:3 where rank=:4' # tp_tour 저장순서 주의할 것
        self.__conn = dbtemp.connect()
        print(self.__conn, tp_tour)  # 확인
        try:
            # 자동 close 되게 처리 : try with resource 문 이용
            with self.__conn.cursor() as cursor:
                cursor.execute(query, tp_tour)
            dbtemp.commit(self.__conn)
        except Exception as e:
            dbtemp.rollback(self.__conn)
            print('update_tour 실패 : ', e)
        finally:
            dbtemp.close(self.__conn)
    # update method ------------------------------------------------

    # delete all method ------------------------------------------------
    def delete_tour(self):
        query = 'delete from tour'
        self.__conn = dbtemp.connect()
        try:
            # 자동 close 되게 처리 : try with resource 문 이용
            with self.__conn.cursor() as cursor:
                cursor.execute(query)
            dbtemp.commit(self.__conn)
        except Exception as e:
            dbtemp.rollback(self.__conn)
            print('delete_tour 실패 : ', e)
        finally:
            dbtemp.close(self.__conn)
    # delete method ------------------------------------------------

    # select all method ------------------------------------------------
    def select_all_tour(self):
        query = 'select * from tour'
        self.__conn = dbtemp.connect()
        try:
            # 자동 close 되게 처리 : try with resource 문 이용
            with self.__conn.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()  # list 반환됨
        except Exception as e:
            print('select_all_tour 실패 : ', e)
        finally:
            dbtemp.close(self.__conn)
    # select all method ------------------------------------------------

    # select one method ------------------------------------------------
    def select_one_tour(self, tp_tour):
        query = 'select * from tour where rank=:1'
        self.__conn = dbtemp.connect()
        print(self.__conn, tp_tour)  # 확인
        try:
            # 자동 close 되게 처리 : try with resource 문 이용
            with self.__conn.cursor() as cursor:
                cursor.execute(query, tp_tour)
                return cursor.fetchone()
        except Exception as e:
            print('select_one_tour 실패 : ', e)
        finally:
            dbtemp.close(self.__conn)
    # select one method ------------------------------------------------
# TourModel-------------------------------------------------------
