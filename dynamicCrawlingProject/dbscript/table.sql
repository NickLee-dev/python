-- dbscript\\table.sql
-- ���� �� ũ�Ѹ����� ������ �˻� ��� ����� ���̺� ���� ��ũ��Ʈ

DROP TABLE TOUR CASCADE CONSTRAINTS;

CREATE TABLE TOUR (
    RANK VARCHAR2(100),
    NAME VARCHAR2(100),
    DESCRIPTION VARCHAR2(2000),
    CATEGORY VARCHAR2(100)
);



COMMIT;