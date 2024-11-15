# test3.py
# 공공데이터포털(https://data.go.kr) 에서 csv 파일 다운받기
# csv 파일 읽어 들이기
# 읽어 들인 데이터에서 가장 많이 사용된 명사 찾기


import codecs
import csv
from konlpy.tag import Okt

okt = Okt()             # Okt
word_dic = {}           # dict() 단어의 총 갯수가 담길 딕셔너리
lines = []              # list() 파일에서 추출한 값을 담을 리스트

# 파일 스트링열기
# 파일변수 = open('파일명.확장자','열기모드')
# 읽기 or 쓰기
# 파일변수.read(), 파일변수.write()
# 처리가 완료되면 반드시 닫기
# 파일변수.close()

# csv 파일에서 데이터를 읽어옴 : codecs 모듈이 제공하는 함수 사용
# 파일 입출력이 끝나면 자동 close 되게 하려면, with resource 문 사용함
with open('./data/sample2.csv','r') as raws:   #
    reader = csv.reader(raws)
    for raw in reader:
        lines.append(raw) # raw(한줄의 데이터)를 리스트에 저장함
        # print(raw) # ['연도', '부처명', '담당부서명', '세부사업명', '사업내용', '훈련기관', '훈련대상']

# 저장구조 : [[],[],[],......]
for line in lines:
    mal_list = okt.pos(' '.join(line))   # '구분자'.join(리스트) => 공백으로 구분해서 하나의 문자열 만듦
    # 리스트 안의 글자들을 하나의 문자열로 만들고, 형태소 분석과 태깅 처리
    # print(mal_list)

    # 명사들을 수집해서 반속되는 명사를 count를 진행 처리
    for word in mal_list:
        # print(word)  # 튜플로 출력('단어', '태그') => (인덱스0, 인덱스1)
        if word[1] == 'Noun':  # 태그가 명사(Noun) 만 추출
            # 명사에 해당되는 단어가 사전에 저장되어 있지 않다면, 사전에 저장 처리함
            if word[0] not in word_dic:
                word_dic[word[0]] = 0   # {단어:0}
                # 단어가 없으면 처음값 0으로 넣기
            word_dic[word[0]] += 1      # 단어(key)의 카운트를 1증가 처리

# print(word_dic)
# 단어 빈도수에 대해 내림차순 정렬처리
keys = sorted(word_dic.items(), key=lambda x: x[1], reverse=True)
# item을 을 기준으로 아이탬의 빈도수를 가지고 정렬하며 내림차순으로 정렬한다(reverse=True)
# 50개 까지 정렬 결과 출력
#for word, count in keys[:50]:
    # print(f'{word}: {count}', end=", ")

# wordcloud(차트) 만들기
# wordcloud 패키지 설치하고 사용함 = matplotlip 도 자동 설치됨
from wordcloud import WordCloud   # Class 매체
import matplotlib.pyplot as plt

# wordcloud = WordCloud(font_path="./fonts/malgun.ttf",background_color="white",width=1000,height=800)
# wordcloud.generate_from_frequencies(word_dic)
#
# plt.figure(figsize = (10,10)) #차트생성
# plt.imshow(wordcloud)
# plt.axis('off')
# plt.show()

# wordcloud 모양(기본은 사각형)을 원하는 도형 모양으로 변경하기
# wordcloud mask 옵션 이용 : 이미지 파일 필요
from PIL import Image   # 이미지 파일 열기용 클래스
import numpy as np  # 배열을 다루는 모듈

img = Image.open('./images/heart.png')         # 이미지 파일 오픈
imgArray = np.array(img)                        # 이미지의 각 픽셀을 수치로 변환함
# print(imgArray.shape,imgArray) # imgArray : (400, 400, 3)

wordcloud = WordCloud(font_path="./fonts/malgun.ttf",background_color="white",width=400,height=400,max_font_size=100,mask=imgArray)
# max_font_size=100 : 빈도수가 가장 큰 글자의 크기 지정
# mask=imgArray : 사용하고자 하는 도형 이미지 수치 배열
wordcloud.generate_from_frequencies(word_dic)

plt.figure(figsize = (10,10)) #차트생성
plt.imshow(wordcloud)
plt.axis('off')
plt.show()




