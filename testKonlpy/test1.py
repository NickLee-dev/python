# path : test1.py
# module : test1
# 한글 형태소 분석 테스트 스크립트
# python3.11 로 설치해야 함 => python3.13 설치시 외부모듈 설치 또는 사용 에러 발생함
# 프로젝트에 사용된 python interpreter (파이썬 버전) 변경 방법 :
# File 메뉴> Settings... > Project: 프로젝트이름 > python interpreter 선택 > 우측의 Add Interpreter... 클릭
# > 새 창의 왼쪽 System Interpreter 선택 > 사용할 python버전 확인하고 선택 > Ok >Apply

# 패키지 설치
# konlpy

from konlpy.tag import Hannanum         # 클래스만 임포트함
# Hannanum : KAIST 말뭉치를 이용해서 생성된 사전 객체임
# KAIST 에서 만든 한글 형태소 분석기임

# 레퍼런스변수 = 클래스생성자(전달할초기값) => 객체(instance) 생성
hannanum = Hannanum()

# 제공하는 메소드 : 레퍼런스.메소드(전달인자)
# hannanum.analyze() : 구(phrase) 분석
# hannanum.morphs() : 형태소 분석(품사별로 분류)
# hannanum.nouns() : 명사 분석
# hannanum.pos() : 형태소 분석 결과에 태깅(tagging/분석된 각 단어 옆에 품사표시)

# 사용 예시
print('Hannanum 이용 ---------------------------------------------------------')
text1 = u'롯데마트의 흑마늘 양념 치킨이 논란이 되고 있다.'
print(hannanum.analyze(text1))  # 구 분석
print(hannanum.morphs(text1))  # 형태소 분석(품사별로 분류)
print(hannanum.nouns(text1))  # 명사 분석
print(hannanum.pos(text1))  # 형태소 분석 결과에 태깅(tagging/분석된 각 단어 옆에 품사표시)

# KKma : 서울대에서 만든 세종 말뭉치를 이용하는 한글 형태소 분석기
from konlpy.tag import Kkma

kkma = Kkma()
# 메소드 정리:
# kkma.sentences() : 문장 분석
# kkma.morphs() : 형태소 분석
# kkma.nouns() : 명사 분석
# kkma.pos() : 형태소 분석 태깅

print('KKma 이용 ------------------------------------------')
print(kkma.sentences(text1))
print(kkma.morphs(text1))
print(kkma.nouns(text1))
print(kkma.pos(text1))

# Komoran : Java로 만든 오픈소스 한글 형태소 분석기
from konlpy.tag import Komoran

komoran = Komoran()
# 메소드 정리 :
# komoran.morphs() : 형태소 분석
# komoran.nouns() : 명사 분석
# komoran.pos() : 형태소 분석 태깅

print('Komoran 이용 ------------------------------------------')
print(komoran.morphs(text1))
print(komoran.nouns(text1))
print(komoran.pos(text1))

# Twitter(Okt) : 오픈소스 한글 형태소 분석기
from konlpy.tag import Twitter

twitter = Twitter()
# 제공하는 메소드 : 레퍼런스.메소드(전달인자)
# twitter.phrases() : 구(phrase) 분석
# twitter.morphs() : 형태소 분석(품사별로 분류)
# twitter.nouns() : 명사 분석
# twitter.pos() : 형태소 분석 결과에 태깅(tagging/분석된 각 단어 옆에 품사표시)

# 사용 예시
print('Twitter 이용 ---------------------------------------------------------')
print(twitter.phrases(text1))  # 구 분석
print(twitter.morphs(text1))  # 형태소 분석(품사별로 분류)
print(twitter.nouns(text1))  # 명사 분석
print(twitter.pos(text1))  # 형태소 분석 결과에 태깅(tagging/분석된 각 단어 옆에 품사표시)

# stem : 각 단어에서 어간 추출 처리 매개변수
print("Okt method stem parameter using ---------------------------")
print(twitter.morphs(text1, stem=True))