-- OpenCV �� tesseract-ocr �̿��ؼ� ������ ��ȣ�� ��ȭ��ȣ ����� ���̺� ��ũ��Ʈ
-- vision\\dbscript\\table.sql

DROP TABLE VISION CASCADE CONSTRAINTS;

CREATE TABLE VISION (
    NAME VARCHAR2(100) NOT NULL,
    TEL VARCHAR2(25) NOT NULL
);

COMMENT ON COLUMN VISION.NAME IS '��ȣ��';
COMMENT ON COLUMN VISION.TEL IS '��ȭ��ȣ';

COMMIT;