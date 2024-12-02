# pandas_test5.py

import pandas as pd
import numpy as np
import pandas_datareader as pdr # pip install pandas_datareader
from numpy.ma.core import reshape

# 인터넷 상의 데이터베이스 자료 읽어오기
# 추가 설치 패키지 : pandas-datareader(임포트시 모듈명 : pandas_datareader)
# 데이터베이스 자료 제공하는 사이트 확인 필요함(유료 사이트 주의)
'''
참조 : https://pandas-datareader.readthedocs.io/en/latest/index.html
사이트 종류 확인 : https://pandas-datareader.readthedocs.io/en/latest/readers/index.html
사이트 종류 : 
AlphaVantage
Federal Reserve Economic Data (FRED)
Fama-French Data (Ken French’s Data Library)
Bank of Canada
Econdb
Enigma
Eurostat
The Investors Exchange (IEX)
Moscow Exchange (MOEX)
NASDAQ
Naver Finance
Organisation for Economic Co-operation and Development (OECD)
Quandl
Stooq.com
Tiingo
Thrift Savings Plan (TSP)
World Bank
Yahoo Finance
'''

# 데이터 검색을 위한 날짜 지정할 때 datetime 모듈을 이용할 수 있음
import datetime

# 날짜는 datetime 함수를 이용해도 되고, 문자열로 지정해도 됨
# 내부적으로 자동으로 dateutil 패키지가 사용되어 날짜가 됨
# dt_start = datetime.datetime(2015,1,1)
# dt_end = '2016, 6, 30'  # dateutil 에 의해 자동 날짜가 됨
# print(dt_start, dt_end)
dt_start = datetime.datetime(2023,1,1)
dt_end = datetime.datetime(2024,11,25)

# data_source = '읽어올 웹사이트 url' 지정할 수 있음
# 제공되는 데이터 코드는 해당 웹사이트에 가서 직접 확인 필요함
# pandas_datareader 패키지가 제공하는 기본 웹사이트 정보 읽어오기 함수가 있음

# FRED 사이트의 데이터베이스에서
# 미국 국가총생산(GDP), 모든 항목이 포함된 소비자가격지수(CPAUCSL),
# 식료품 및 연료를 제외한 소비자가격지수(CPILFESL) 를 가져온다면,
# data_source 에 각 데이터에 대한 url 을 지정하면 됨
#  https://fred.stlouisfed.org/series/GDP
#   https://fred.stlouisfed.org/series/CPIAUCSL
#   https://fred.stlouisfed.org/series/CPILFESL
# pdr.get_data_fred() 함수 사용하면, 자동 data_source 가 FRED 로 설정됨

gdp = pdr.get_data_fred("GDP",start=dt_start,end=dt_end)
# print(gdp)
'''
                  GDP
DATE                 
2023-01-01  27164.359
2023-04-01  27453.815
2023-07-01  27967.697
2023-10-01  28296.967
2024-01-01  28624.069
2024-04-01  29016.714
2024-07-01  29349.924
'''
# print(gdp.head())
'''
                  GDP
DATE                 
2023-01-01  27164.359
2023-04-01  27453.815
2023-07-01  27967.697
2023-10-01  28296.967
2024-01-01  28624.069
'''

# 데이터 코드에 리스트를 넣으면, 여러 개의 항목별 데이터를 동시에 가져옴
# inflation = pdr.get_data_fred(['CPIAUCSL','CPILFESL'],start=dt_start,end=dt_end)
# print(inflation)
'''
            CPIAUCSL  CPILFESL
DATE                          
2023-01-01   300.356   302.709
2023-02-01   301.509   304.124
2023-03-01   301.744   305.112
2023-04-01   303.032   306.539
2023-05-01   303.365   307.646
2023-06-01   304.003   308.245
2023-07-01   304.628   308.945
2023-08-01   306.187   309.656
2023-09-01   307.288   310.644
2023-10-01   307.531   311.390
2023-11-01   308.024   312.349
2023-12-01   308.742   313.209
2024-01-01   309.685   314.438
2024-02-01   311.054   315.565
2024-03-01   312.230   316.698
2024-04-01   313.207   317.622
2024-05-01   313.225   318.140
2024-06-01   313.049   318.346
2024-07-01   313.534   318.872
2024-08-01   314.121   319.768
2024-09-01   314.686   320.767
2024-10-01   315.454   321.666
'''

# 데이터 프레임의 고급 인덱싱
# 데이터 프레임은 2차원 배열임 + ( 행인덱싱라벨, 열 인덱스 라밸)

# loc 인덱서(인덱싱 속성)
# 라벨 기반의 2차원 인덱싱에 사용
# 데이터 프레임 변수.loc[행라벨] 또는 [행라벨, 열라벨]
df = pd.DataFrame(np.arange(10,22).reshape(3,4),index = ['a','b','c'], columns = ['A','B','C','D'])
print(df)
'''
    A   B   C   D
a  10  11  12  13
b  14  15  16  17
c  18  19  20  21
'''
print(df.loc['a']) # 한 행 인덱싱, 세로로 출력
'''
A    10
B    11
C    12
D    13
Name: a, dtype: int64
'''
print(type(df.loc['a'])) # <class 'pandas.core.series.Series'>
print(df.loc['b':'c']) # 슬라이싱, 가로로 출력 : DataFrame
'''
    A   B   C   D
b  14  15  16  17
c  18  19  20  21
'''
print(df['b':'c']) # 슬라이싱에는 인덱서를 사용 안 해도 됨
'''
    A   B   C   D
b  14  15  16  17
c  18  19  20  21
'''

# print(df[['b','c']]) # 슬라이싱이 아닌 행라벨을 리스트로 나열한 인덱싱시에는 KeyError 발생함
print(df.loc[['b','c']])
'''
    A   B   C   D
b  14  15  16  17
c  18  19  20  21
'''

print(df.A > 15) # 비교연산 결과인 True,False 로 출력됨, A열 인덱싱(추출) : 시리즈임
print(type(df.A > 15)) # <class 'pandas.core.series.Series'>
'''
a    False
b    False
c     True
Name: A, dtype: bool
'''
print(df.loc[df.A > 15]) # 조건의 결과가 True인 갓만 출력
'''
    A   B   C   D
c  18  19  20  21
'''

# 인덱스 값을 반환하는 함수를 사용할 수도 있음
# 예 : A열의 값이 12보다 큰 행들만 선택 하는 경우
def select_row(df):
    return df.A > 12

# 함수사용
print(select_row(df))  #  True,False 추출
'''
a    False
b     True
c     True
Name: A, dtype: bool
'''
print(df.loc[select_row(df)]) # True 가 리턴된 행의 값들이 출력됨
'''
    A   B   C   D
b  14  15  16  17
c  18  19  20  21
'''

# 인덱싱에 행과 열을 적용한 경우
print(df.loc['a','A']) # 10 # 값 하나 출력, a행A열 위치의 값을 의미함
print(df.loc['a',:])  # print(df.loc['a']) 와 같음
'''
A    10
B    11
C    12
D    13
Name: a, dtype: int64
'''
print(df.loc[['a','b'],['B','D']])
'''
    B   D
a  11  13
b  15  17
'''

# boolean 값으로 인덱싱할 수도 있음
print(df.loc[df.A > 10,['C','D']])  # 비교결과가 True 인 행의 C열과 D열을 추출
'''
    C   D
b  16  17
c  20  21
'''
# iloc 인덱서
# 순서를 나타내는 정수 기반의 2차원 인덱싱에 사용함
print(df.iloc[0,1]) # 11 # 0행 1열 위치의 값
print(df.iloc[:2,2]) # 0행과 1행의 2열값 추출
'''
a    12
b    16
Name: C, dtype: int64
'''
print(df.iloc[0,-2:]) # 0행 3열, 0행 4열 인덱싱
'''
C    12
D    13
Name: a, dtype: int64
'''
print(df.iloc[2:3, 1:3]) # 2행 1열과, 2행 2열 인덱싱
'''
    B   C
c  19  20
'''
print(df.iloc[-1]) # 2차원배열인데 인덱스가하나면 행을 선택함. -1 : 끝에서 부터 첫전째(마지막행)
'''
A    18
B    19
C    20
D    21
Name: c, dtype: int64
'''
df.iloc[-1] = df.iloc[-1]*2  # 마지막행 값들에 *2 한 결과를 마지막행에 대입함
print(df)
'''
    A   B   C   D
a  10  11  12  13
b  14  15  16  17
c  36  38  40  42
'''